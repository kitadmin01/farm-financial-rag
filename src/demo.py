#!/usr/bin/env python3
"""
Demo Script for Farm Financial Data RAG Application
Showcases the application with example questions and responses.
"""

import os
import time
from dotenv import load_dotenv

# Load environment variables from parent directory
load_dotenv('../.env')

def run_demo():
    """Run a demonstration of the RAG application."""
    print("🌾 Farm Financial Data RAG Application - Demo")
    print("=" * 60)
    
    # Check if we can import the RAG app
    try:
        from farm_rag_app import FarmDataRAG
        print("✅ RAG application loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load RAG application: {e}")
        return
    
    # Create RAG instance
    try:
        rag_app = FarmDataRAG()
        print("✅ RAG instance created")
    except Exception as e:
        print(f"❌ Failed to create RAG instance: {e}")
        return
    
    # Demo questions
    demo_questions = [
        {
            "question": "How many farms are in the database?",
            "description": "Basic count query"
        },
        {
            "question": "Which farms have the highest current ratio?",
            "description": "Financial performance ranking"
        },
        {
            "question": "What is the average working capital by state?",
            "description": "Geographic analysis with aggregation"
        },
        {
            "question": "Show me farms with debt-to-equity ratio above 2.0",
            "description": "Filtering and financial analysis"
        },
        {
            "question": "How did net worth change from beginning to end of year?",
            "description": "Trend analysis across time periods"
        }
    ]
    
    print(f"\n📊 Running {len(demo_questions)} demo questions...")
    print("=" * 60)
    
    results = []
    
    for i, demo in enumerate(demo_questions, 1):
        question = demo["question"]
        description = demo["description"]
        
        print(f"\n🔍 Question {i}: {question}")
        print(f"   Description: {description}")
        print("-" * 40)
        
        try:
            # Start timing
            start_time = time.time()
            
            # Process question
            result = rag_app.ask_question(question)
            
            # End timing
            end_time = time.time()
            response_time = end_time - start_time
            
            if result["success"]:
                print("✅ Success!")
                print(f"   ⚡ Response time: {response_time:.2f}s")
                print(f"   📊 Rows returned: {result['query_result']['row_count']}")
                print(f"   🔍 SQL Query: {result['sql_query'][:80]}...")
                print(f"   💬 AI Response: {result['response'][:150]}...")
                
                # Store result for summary
                results.append({
                    "question": question,
                    "success": True,
                    "response_time": response_time,
                    "rows": result['query_result']['row_count']
                })
                
            else:
                print(f"❌ Failed: {result.get('error', 'Unknown error')}")
                results.append({
                    "question": question,
                    "success": False,
                    "error": result.get('error', 'Unknown error')
                })
                
        except Exception as e:
            print(f"❌ Exception: {e}")
            results.append({
                "question": question,
                "success": False,
                "error": str(e)
            })
        
        # Small delay between questions
        time.sleep(1)
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 DEMO RESULTS SUMMARY")
    print("=" * 60)
    
    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]
    
    print(f"✅ Successful: {len(successful)}/{len(results)}")
    print(f"❌ Failed: {len(failed)}/{len(results)}")
    
    if successful:
        avg_time = sum(r["response_time"] for r in successful) / len(successful)
        total_rows = sum(r["rows"] for r in successful)
        print(f"⚡ Average response time: {avg_time:.2f}s")
        print(f"📊 Total rows returned: {total_rows}")
    
    if failed:
        print(f"\n❌ Failed questions:")
        for result in failed:
            print(f"   - {result['question']}: {result['error']}")
    
    print("\n" + "=" * 60)
    
    if len(successful) == len(results):
        print("🎉 All demo questions completed successfully!")
        print("🚀 Your RAG application is working perfectly!")
    else:
        print("⚠️  Some demo questions failed. Check the errors above.")
    
    print("\n💡 Try these additional questions:")
    print("   - 'Which state has the most farms?'")
    print("   - 'What is the 75th percentile for current ratio?'")
    print("   - 'Compare farm performance between Minnesota and Wisconsin'")
    print("   - 'Show me farms with the best return on assets'")

def interactive_demo():
    """Run an interactive demo where user can ask questions."""
    print("\n🎮 Interactive Demo Mode")
    print("Ask your own questions about farm financial data!")
    print("Type 'quit' to exit")
    print("-" * 40)
    
    try:
        from farm_rag_app import FarmDataRAG
        rag_app = FarmDataRAG()
        
        while True:
            question = input("\n🌾 Your question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not question:
                continue
            
            print("🤔 Processing your question...")
            
            try:
                start_time = time.time()
                result = rag_app.ask_question(question)
                end_time = time.time()
                
                if result["success"]:
                    print(f"\n✅ Response (in {end_time - start_time:.2f}s):")
                    print(f"📊 Rows: {result['query_result']['row_count']}")
                    print(f"🔍 SQL: {result['sql_query']}")
                    print(f"💬 AI: {result['response']}")
                else:
                    print(f"❌ Error: {result.get('error', 'Unknown error')}")
                    
            except Exception as e:
                print(f"❌ Exception: {e}")
    
    except Exception as e:
        print(f"❌ Interactive demo failed: {e}")

def main():
    """Main demo function."""
    print("Choose demo mode:")
    print("1. Automated demo (recommended)")
    print("2. Interactive demo")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            run_demo()
            break
        elif choice == "2":
            interactive_demo()
            break
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
