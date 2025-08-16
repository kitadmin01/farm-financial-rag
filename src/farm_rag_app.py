#!/usr/bin/env python3
"""
Farm Financial Data RAG Application
Uses OpenAI LLM to understand questions, generate SQL, execute queries, and provide intelligent responses.
"""

import os
import sqlite3
import json
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from dotenv import load_dotenv
import openai
import pandas as pd

# Load environment variables from parent directory
load_dotenv('../.env')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class QueryResult:
    """Container for query results and metadata."""
    success: bool
    data: Optional[pd.DataFrame]
    sql_query: str
    error_message: Optional[str] = None
    row_count: int = 0
    execution_time: float = 0.0

class FarmDataRAG:
    """RAG application for farm financial data analysis."""
    
    def __init__(self):
        """Initialize the RAG application."""
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = os.getenv('OPENAI_MODEL', 'gpt-4-turbo-preview')
        self.database_path = os.getenv('DATABASE_PATH', 'finbin_farm_data.db')
        self.max_tokens = int(os.getenv('MAX_TOKENS', 4000))
        self.temperature = float(os.getenv('TEMPERATURE', 0.1))
        self.system_prompt = os.getenv('SYSTEM_PROMPT', 'You are a financial analyst assistant for farm data.')
        
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        # Initialize OpenAI client
        openai.api_key = self.api_key
        
        # Database schema information for context
        self.db_schema = self._get_database_schema()
        
    def _get_database_schema(self) -> str:
        """Get database schema information for LLM context."""
        try:
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()
            
            # Get all tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            
            schema_info = []
            for table in tables:
                table_name = table[0]
                cursor.execute(f"PRAGMA table_info({table_name})")
                columns = cursor.fetchall()
                
                table_schema = f"Table: {table_name}\n"
                table_schema += "Columns:\n"
                for col in columns:
                    col_name, col_type, not_null, default_val, pk = col[1], col[2], col[3], col[4], col[5]
                    pk_marker = " (PRIMARY KEY)" if pk else ""
                    table_schema += f"  - {col_name}: {col_type}{pk_marker}\n"
                
                schema_info.append(table_schema)
            
            conn.close()
            return "\n".join(schema_info)
            
        except Exception as e:
            logger.error(f"Error getting database schema: {e}")
            return "Database schema information unavailable"
    
    def _generate_sql_query(self, user_question: str) -> str:
        """Use OpenAI to generate SQL query from user question."""
        
        prompt = f"""
You are a SQL expert specializing in farm financial data analysis. Based on the user's question, generate a SQL query to extract the relevant information.

Database Schema:
{self.db_schema}

User Question: {user_question}

Instructions:
1. Analyze the question to understand what data is needed
2. Generate a SQL query that will answer the question
3. Use ONLY the table names and column names from the schema above
4. Use appropriate JOINs to connect related tables
5. Include WHERE clauses for filtering when relevant
6. Use ORDER BY for ranking or sorting when appropriate
7. Limit results to reasonable amounts (use LIMIT 10-50)
8. Return ONLY the SQL query, no explanations
9. IMPORTANT: Do not use table names that don't exist in the schema

Available tables: hdb_main_data, fm_genin, fm_guide, fm_stmts, fm_prf_lq, fm_cap_ad, fm_hhold, fm_nf_ie, fm_fm_exp, fm_fm_inc, fm_beg_bs_end_bs

SQL Query:
"""
        
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key)
            
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a SQL expert. Generate only SQL queries, no explanations."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            sql_query = response.choices[0].message.content.strip()
            
            # Clean up the response to extract just the SQL
            if sql_query.startswith('```sql'):
                sql_query = sql_query[7:]
            if sql_query.endswith('```'):
                sql_query = sql_query[:-3]
            
            sql_query = sql_query.strip()
            
            logger.info(f"Generated SQL: {sql_query}")
            return sql_query
            
        except Exception as e:
            logger.error(f"Error generating SQL: {e}")
            raise Exception(f"Failed to generate SQL query: {e}")
    
    def _execute_sql_query(self, sql_query: str) -> QueryResult:
        """Execute the SQL query and return results."""
        import time
        
        start_time = time.time()
        
        try:
            conn = sqlite3.connect(self.database_path)
            
            # Execute query
            df = pd.read_sql_query(sql_query, conn)
            conn.close()
            
            execution_time = time.time() - start_time
            
            return QueryResult(
                success=True,
                data=df,
                sql_query=sql_query,
                row_count=len(df),
                execution_time=execution_time
            )
            
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"SQL execution error: {e}")
            
            return QueryResult(
                success=False,
                data=None,
                sql_query=sql_query,
                error_message=str(e),
                execution_time=execution_time
            )
    
    def _generate_response(self, user_question: str, query_result: QueryResult) -> str:
        """Use OpenAI to generate a natural language response based on query results."""
        
        if not query_result.success:
            prompt = f"""
The user asked: {user_question}

I tried to execute this SQL query: {query_result.sql_query}

But encountered an error: {query_result.error_message}

Please provide a helpful response explaining what went wrong and suggest how the user might rephrase their question.
"""
        else:
            # Convert DataFrame to readable format
            if query_result.row_count > 0:
                data_summary = query_result.data.head(20).to_string(index=False)
                if query_result.row_count > 20:
                    data_summary += f"\n... and {query_result.row_count - 20} more rows"
            else:
                data_summary = "No data found matching the criteria."
            
            prompt = f"""
The user asked: {user_question}

I executed this SQL query: {query_result.sql_query}

Query Results:
- Rows returned: {query_result.row_count}
- Execution time: {query_result.execution_time:.3f} seconds

Data:
{data_summary}

Please provide a clear, insightful response that:
1. Directly answers the user's question
2. Highlights key insights from the data
3. Provides context about what the numbers mean
4. Suggests follow-up questions if relevant
5. Uses financial terminology appropriately for farm data analysis

Response:
"""
        
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key)
            
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return f"I apologize, but I encountered an error while processing your request: {e}"
    
    def ask_question(self, user_question: str) -> Dict[str, Any]:
        """Main method to process a user question and return a comprehensive response."""
        
        try:
            logger.info(f"Processing question: {user_question}")
            
            # Step 1: Generate SQL query
            sql_query = self._generate_sql_query(user_question)
            
            # Step 2: Execute SQL query
            query_result = self._execute_sql_query(sql_query)
            
            # Step 3: Generate natural language response
            response = self._generate_response(user_question, query_result)
            
            # Step 4: Return comprehensive result
            result = {
                "success": True,
                "question": user_question,
                "sql_query": sql_query,
                "response": response,
                "query_result": {
                    "success": query_result.success,
                    "row_count": query_result.row_count,
                    "execution_time": query_result.execution_time,
                    "error_message": query_result.error_message
                }
            }
            
            if query_result.success and query_result.data is not None:
                result["data_preview"] = query_result.data.head(10).to_dict('records')
            
            return result
            
        except Exception as e:
            logger.error(f"Error in ask_question: {e}")
            return {
                "success": False,
                "question": user_question,
                "error": str(e),
                "response": f"I apologize, but I encountered an error while processing your request: {e}"
            }

def main():
    """Main function for testing the RAG application."""
    
    try:
        # Initialize the RAG application
        rag_app = FarmDataRAG()
        print("=== Farm Financial Data RAG Application ===")
        print("Type 'quit' to exit")
        print()
        
        while True:
            # Get user input
            user_question = input("Ask a question about farm financial data: ").strip()
            
            if user_question.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_question:
                continue
            
            print("\nProcessing your question...")
            
            # Process the question
            result = rag_app.ask_question(user_question)
            
            # Display results
            if result["success"]:
                print(f"\nSQL Query: {result['sql_query']}")
                print(f"\nResponse: {result['response']}")
                
                if "data_preview" in result and result["data_preview"]:
                    print(f"\nData Preview (showing {len(result['data_preview'])} rows):")
                    for i, row in enumerate(result["data_preview"], 1):
                        print(f"Row {i}: {row}")
                
                print(f"\nQuery executed in {result['query_result']['execution_time']:.3f} seconds")
                print(f"Rows returned: {result['query_result']['row_count']}")
            else:
                print(f"\nError: {result['error']}")
                print(f"Response: {result['response']}")
            
            print("\n" + "="*50 + "\n")
    
    except Exception as e:
        print(f"Application error: {e}")
        logger.error(f"Application error: {e}")

if __name__ == "__main__":
    main()
