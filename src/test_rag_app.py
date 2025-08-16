#!/usr/bin/env python3
"""
Comprehensive Test Program for Farm Financial Data RAG Application
Tests all components: OpenAI API, database, SQL generation, and response generation.
"""

import os
import sys
import time
import json
from dotenv import load_dotenv

# Load environment variables from parent directory
load_dotenv('../.env')

def test_environment():
    """Test environment configuration."""
    print("🔧 Testing Environment Configuration...")
    
    # Check OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key and api_key.startswith('sk-'):
        print(f"✅ OpenAI API key configured: {api_key[:20]}...")
        return True
    else:
        print("❌ OpenAI API key not configured or invalid format")
        return False

def test_openai_connection():
    """Test OpenAI API connection with actual API call."""
    print("\n🤖 Testing OpenAI API Connection...")
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        # Test with a simple completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hello, OpenAI is working!'"}],
            max_tokens=10
        )
        
        if response.choices[0].message.content:
            print("✅ OpenAI API connection successful")
            print(f"✅ Response: {response.choices[0].message.content}")
            return True
        else:
            print("❌ OpenAI API returned empty response")
            return False
            
    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return False

def test_database():
    """Test database connection and data."""
    print("\n🗄️ Testing Database...")
    
    try:
        import sqlite3
        
        db_path = "finbin_farm_data.db"
        if not os.path.exists(db_path):
            print(f"❌ Database file not found: {db_path}")
            return False
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        if tables:
            print(f"✅ Database connected successfully")
            print(f"✅ Found {len(tables)} tables:")
            
            # Check data in key tables
            key_tables = ['hdb_main_data', 'fm_genin', 'fm_guide']
            for table_name in key_tables:
                try:
                    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                    count = cursor.fetchone()[0]
                    print(f"   - {table_name}: {count} rows")
                except:
                    print(f"   - {table_name}: table not found")
        
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

def test_rag_import():
    """Test if RAG application can be imported."""
    print("\n🧠 Testing RAG Application Import...")
    
    try:
        from farm_rag_app import FarmDataRAG
        print("✅ RAG application imports successfully")
        return True
    except Exception as e:
        print(f"❌ RAG import error: {e}")
        return False

def test_rag_instance():
    """Test RAG application instance creation."""
    print("\n🏗️ Testing RAG Instance Creation...")
    
    try:
        from farm_rag_app import FarmDataRAG
        rag_app = FarmDataRAG()
        print("✅ RAG application instance created successfully")
        
        # Test database schema retrieval
        if hasattr(rag_app, 'db_schema') and rag_app.db_schema:
            print("✅ Database schema retrieved successfully")
            print(f"✅ Schema length: {len(rag_app.db_schema)} characters")
        else:
            print("❌ Database schema retrieval failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ RAG instance error: {e}")
        return False

def test_sql_generation():
    """Test SQL generation with OpenAI."""
    print("\n🔍 Testing SQL Generation...")
    
    try:
        from farm_rag_app import FarmDataRAG
        rag_app = FarmDataRAG()
        
        # Test question
        test_question = "How many farms are in the database?"
        
        print(f"   Testing question: '{test_question}'")
        
        # Generate SQL
        sql_query = rag_app._generate_sql_query(test_question)
        
        if sql_query and sql_query.strip():
            print("✅ SQL generation successful")
            print(f"✅ Generated SQL: {sql_query[:100]}...")
            return True
        else:
            print("❌ SQL generation returned empty result")
            return False
        
    except Exception as e:
        print(f"❌ SQL generation error: {e}")
        return False

def test_sql_execution():
    """Test SQL execution against database."""
    print("\n⚡ Testing SQL Execution...")
    
    try:
        from farm_rag_app import FarmDataRAG
        rag_app = FarmDataRAG()
        
        # Simple test query
        test_sql = "SELECT COUNT(*) as farm_count FROM hdb_main_data"
        
        print(f"   Testing SQL: '{test_sql}'")
        
        # Execute query
        result = rag_app._execute_sql_query(test_sql)
        
        if result.success:
            print("✅ SQL execution successful")
            print(f"✅ Rows returned: {result.row_count}")
            print(f"✅ Execution time: {result.execution_time:.3f}s")
            return True
        else:
            print(f"❌ SQL execution failed: {result.error_message}")
            return False
        
    except Exception as e:
        print(f"❌ SQL execution error: {e}")
        return False

def test_full_rag_workflow():
    """Test complete RAG workflow."""
    print("\n🔄 Testing Complete RAG Workflow...")
    
    try:
        from farm_rag_app import FarmDataRAG
        rag_app = FarmDataRAG()
        
        # Test question
        test_question = "How many farms are in each state?"
        
        print(f"   Testing question: '{test_question}'")
        
        # Start timing
        start_time = time.time()
        
        # Process question
        result = rag_app.ask_question(test_question)
        
        # End timing
        end_time = time.time()
        total_time = end_time - start_time
        
        if result["success"]:
            print("✅ RAG workflow successful")
            print(f"✅ Total time: {total_time:.2f}s")
            print(f"✅ SQL generated: {result['sql_query'][:80]}...")
            print(f"✅ Response length: {len(result['response'])} characters")
            print(f"✅ Rows returned: {result['query_result']['row_count']}")
            return True
        else:
            print(f"❌ RAG workflow failed: {result.get('error', 'Unknown error')}")
            return False
        
    except Exception as e:
        print(f"❌ RAG workflow error: {e}")
        return False

def test_api_endpoints():
    """Test FastAPI endpoints."""
    print("\n🌐 Testing API Endpoints...")
    
    try:
        from farm_rag_api import app
        from fastapi.testclient import TestClient
        
        client = TestClient(app)
        
        # Test health endpoint
        response = client.get("/health")
        if response.status_code == 200:
            print("✅ Health endpoint working")
            health_data = response.json()
            print(f"✅ API Status: {health_data['status']}")
            print(f"✅ RAG Status: {health_data['rag_app_status']}")
        else:
            print(f"❌ Health endpoint failed: {response.status_code}")
            return False
        
        # Test examples endpoint
        response = client.get("/examples")
        if response.status_code == 200:
            examples_data = response.json()
            print(f"✅ Examples endpoint working: {len(examples_data['examples'])} categories")
        else:
            print(f"❌ Examples endpoint failed: {response.status_code}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ API testing error: {e}")
        return False

def run_performance_test():
    """Run performance test with multiple questions."""
    print("\n🚀 Running Performance Test...")
    
    try:
        from farm_rag_app import FarmDataRAG
        rag_app = FarmDataRAG()
        
        test_questions = [
            "How many farms are in the database?",
            "What is the average working capital?",
            "Which state has the most farms?",
            "Show me farms with highest current ratio"
        ]
        
        results = []
        for i, question in enumerate(test_questions, 1):
            print(f"   Question {i}: {question}")
            start_time = time.time()
            
            try:
                result = rag_app.ask_question(question)
                end_time = time.time()
                
                if result["success"]:
                    response_time = end_time - start_time
                    results.append({
                        "question": question,
                        "success": True,
                        "response_time": response_time,
                        "rows_returned": result["query_result"]["row_count"]
                    })
                    print(f"      ✅ Success in {response_time:.2f}s, {result['query_result']['row_count']} rows")
                else:
                    results.append({
                        "question": question,
                        "success": False,
                        "error": result.get("error", "Unknown error")
                    })
                    print(f"      ❌ Failed: {result.get('error', 'Unknown error')}")
                    
            except Exception as e:
                results.append({
                    "question": question,
                    "success": False,
                    "error": str(e)
                })
                print(f"      ❌ Exception: {e}")
        
        # Performance summary
        successful_results = [r for r in results if r["success"]]
        if successful_results:
            avg_response_time = sum(r["response_time"] for r in successful_results) / len(successful_results)
            print(f"\n   Performance Summary:")
            print(f"   - Successful queries: {len(successful_results)}/{len(test_questions)}")
            print(f"   - Average response time: {avg_response_time:.2f}s")
            print(f"   - Total rows returned: {sum(r['rows_returned'] for r in successful_results)}")
        
        return len(successful_results) > 0
        
    except Exception as e:
        print(f"❌ Performance test error: {e}")
        return False

def main():
    """Run all tests."""
    print("🌾 Farm Financial Data RAG Application - Comprehensive Test")
    print("=" * 70)
    
    # Test configuration
    tests = [
        ("Environment Configuration", test_environment),
        ("OpenAI API Connection", test_openai_connection),
        ("Database Connection", test_database),
        ("RAG Application Import", test_rag_import),
        ("RAG Instance Creation", test_rag_instance),
        ("SQL Generation", test_sql_generation),
        ("SQL Execution", test_sql_execution),
        ("Complete RAG Workflow", test_full_rag_workflow),
        ("API Endpoints", test_api_endpoints),
        ("Performance Test", run_performance_test)
    ]
    
    results = []
    start_time = time.time()
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            result = test_func()
            results.append((test_name, result))
            time.sleep(1)  # Small delay between tests
        except Exception as e:
            print(f"❌ {test_name} test failed with exception: {e}")
            results.append((test_name, False))
    
    total_time = time.time() - start_time
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 COMPREHENSIVE TEST RESULTS SUMMARY")
    print("=" * 70)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\nOverall Results: {passed}/{total} tests passed")
    print(f"Total test time: {total_time:.2f} seconds")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Your RAG application is fully functional!")
        print("\n🚀 Ready to use:")
        print("1. Start API server: ./start_rag_app.sh")
        print("2. Web interface: http://localhost:8000/web_interface.html")
        print("3. CLI version: cd src && python farm_rag_app.py")
        print("4. API docs: http://localhost:8000/docs")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please review the issues above.")
        
        # Provide specific guidance based on failures
        failed_tests = [name for name, result in results if not result]
        print(f"\nFailed tests: {', '.join(failed_tests)}")
        
        if "Environment Configuration" in failed_tests:
            print("- Check your .env file and OpenAI API key")
        if "Database Connection" in failed_tests:
            print("- Run database creation: cd src && python create_database.py")
        if "OpenAI API Connection" in failed_tests:
            print("- Verify OpenAI API key and internet connection")
        if "RAG Application Import" in failed_tests:
            print("- Check Python dependencies: pip install -r requirements.txt")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
