#!/usr/bin/env python3
"""
Farm Financial Data RAG API
FastAPI web service for farm financial data analysis using OpenAI LLM.
"""

import os
import logging
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from farm_rag_app import FarmDataRAG

# Load environment variables from parent directory
load_dotenv('../.env')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Farm Financial Data RAG API",
    description="AI-powered farm financial data analysis using OpenAI LLM",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="."), name="static")

# Initialize RAG application
try:
    rag_app = FarmDataRAG()
    logger.info("RAG application initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize RAG application: {e}")
    rag_app = None

# Pydantic models
class QuestionRequest(BaseModel):
    question: str
    include_data_preview: bool = True
    max_preview_rows: int = 10

class QuestionResponse(BaseModel):
    success: bool
    question: str
    sql_query: str
    response: str
    query_result: Dict[str, Any]
    data_preview: Optional[list] = None
    error: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    rag_app_status: str
    database_path: str
    openai_model: str

@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Farm Financial Data RAG API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
        "web_interface": "/web_interface.html"
    }

@app.get("/web_interface.html")
async def web_interface():
    """Serve the web interface HTML file."""
    try:
        return FileResponse("web_interface.html", media_type="text/html")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Web interface not found")

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    rag_status = "healthy" if rag_app else "unhealthy"
    
    return HealthResponse(
        status="healthy",
        rag_app_status=rag_status,
        database_path=os.getenv('DATABASE_PATH', 'unknown'),
        openai_model=os.getenv('OPENAI_MODEL', 'unknown')
    )

@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """Ask a question about farm financial data."""
    
    if not rag_app:
        raise HTTPException(status_code=503, detail="RAG application not available")
    
    try:
        # Process the question
        result = rag_app.ask_question(request.question)
        
        # Prepare response
        response = QuestionResponse(
            success=result["success"],
            question=result["question"],
            sql_query=result["sql_query"],
            response=result["response"],
            query_result=result["query_result"],
            data_preview=result.get("data_preview") if request.include_data_preview else None,
            error=result.get("error")
        )
        
        return response
        
    except Exception as e:
        logger.error(f"Error processing question: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/schema")
async def get_database_schema():
    """Get database schema information."""
    
    if not rag_app:
        raise HTTPException(status_code=503, detail="RAG application not available")
    
    try:
        return {
            "schema": rag_app.db_schema,
            "database_path": rag_app.database_path
        }
    except Exception as e:
        logger.error(f"Error getting schema: {e}")
        raise HTTPException(status_code=500, detail=f"Error retrieving schema: {str(e)}")

@app.get("/examples")
async def get_example_questions():
    """Get example questions users can ask."""
    
    examples = [
        {
            "category": "Financial Performance",
            "questions": [
                "Which farms have the highest current ratio?",
                "What is the average working capital by state?",
                "Show me farms with the best debt-to-equity ratios",
                "Which farms had the highest net farm income?"
            ]
        },
        {
            "category": "Geographic Analysis",
            "questions": [
                "How many farms are in each state?",
                "What's the average financial performance by county?",
                "Compare farm performance between Minnesota and Wisconsin"
            ]
        },
        {
            "category": "Trends and Changes",
            "questions": [
                "How did net worth change from beginning to end of year?",
                "Which farms had the biggest increase in working capital?",
                "Show me farms with significant changes in debt levels"
            ]
        },
        {
            "category": "Benchmarking",
            "questions": [
                "What's the 75th percentile for current ratio?",
                "How do farms rank by return on assets?",
                "Which farms are in the top 10% for profitability?"
            ]
        }
    ]
    
    return {"examples": examples}

if __name__ == "__main__":
    import uvicorn
    
    # Run the API server
    uvicorn.run(
        "farm_rag_api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
