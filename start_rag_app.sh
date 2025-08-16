#!/bin/bash

# Farm Financial Data RAG Application Startup Script

echo "🌾 Starting Farm Financial Data RAG Application..."
echo "=================================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first."
    echo "   Run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Please create it with your OpenAI API key."
    echo "   Copy .env.example to .env and add your API key."
    exit 1
fi

# Check if database exists
if [ ! -f "src/finbin_farm_data.db" ]; then
    echo "❌ Database not found. Please run the database creation script first."
    echo "   Run: cd src && python create_database.py"
    exit 1
fi

# Install/upgrade dependencies
echo "📦 Installing/upgrading dependencies..."
pip install -r requirements.txt

echo ""
echo "🚀 Starting RAG API server..."
echo "   API will be available at: http://localhost:8000"
echo "   Web interface will be available at: http://localhost:8000/web_interface.html"
echo "   API documentation at: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the API server
cd src
python farm_rag_api.py
