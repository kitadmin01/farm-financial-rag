#!/usr/bin/env python3
"""
Quick Test Script for Farm Financial Data RAG Application
Simple tests to verify basic functionality is working.
"""

import os
from dotenv import load_dotenv

# Load environment variables from parent directory
load_dotenv('../.env')

def quick_test():
    """Run a quick test of the RAG application."""
    print("🌾 Quick Test - Farm Financial Data RAG Application")
    print("=" * 50)
    
    # Test 1: Environment
    print("\n1. Testing Environment...")
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key and api_key.startswith('sk-'):
        print("✅ OpenAI API key found")
    else:
        print("❌ OpenAI API key not found or invalid")
        return False
    
    # Test 2: Database
    print("\n2. Testing Database...")
    db_path = "finbin_farm_data.db"
    if os.path.exists(db_path):
        print("✅ Database file exists")
    else:
        print("❌ Database file not found - run create_database.py first")
        return False
    
    # Test 3: Import RAG app
    print("\n3. Testing RAG Import...")
    try:
        from farm_rag_app import FarmDataRAG
        print("✅ RAG application imported successfully")
    except Exception as e:
        print(f"❌ RAG import failed: {e}")
        return False
    
    # Test 4: Create RAG instance
    print("\n4. Testing RAG Instance...")
    try:
        rag_app = FarmDataRAG()
        print("✅ RAG instance created successfully")
    except Exception as e:
        print(f"❌ RAG instance creation failed: {e}")
        return False
    
    # Test 5: Simple question
    print("\n5. Testing Simple Question...")
    try:
        question = "How many farms are in the database?"
        print(f"   Asking: '{question}'")
        
        result = rag_app.ask_question(question)
        
        if result["success"]:
            print("✅ Question processed successfully")
            print(f"   SQL: {result['sql_query'][:60]}...")
            print(f"   Response: {result['response'][:100]}...")
            print(f"   Rows: {result['query_result']['row_count']}")
        else:
            print(f"❌ Question processing failed: {result.get('error', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ Question test failed: {e}")
        return False
    
    print("\n🎉 Quick test completed successfully!")
    print("Your RAG application is working correctly.")
    return True

if __name__ == "__main__":
    success = quick_test()
    if success:
        print("\n🚀 Ready to use the RAG application!")
        print("Run: python farm_rag_app.py (CLI) or python farm_rag_api.py (API)")
    else:
        print("\n⚠️  Quick test failed. Check the errors above.")
