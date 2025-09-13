# Farm Financial Data RAG Application - Run Script (PowerShell)
# This script will run the RAG application.

# Set console title and colors
$Host.UI.RawUI.WindowTitle = "Farm Financial Data RAG Application"
$Host.UI.RawUI.ForegroundColor = "Green"

Write-Host ""
Write-Host "========================================"
Write-Host "  Farm Financial Data RAG Application"
Write-Host "========================================"
Write-Host ""
Write-Host "This script will run the RAG application."
Write-Host "Make sure you have Python installed."
Write-Host ""

# Check if we're in the right directory
if (!(Test-Path "src\farm_rag_api.py")) {
    Write-Host "[ERROR] Please run this script from the project root directory." -ForegroundColor Red
    Write-Host "Make sure you're in the folder containing the 'src' folder."
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if Python is installed
Write-Host "[CHECK] Checking Python installation..."
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] Python found: $pythonVersion" -ForegroundColor Green
    } else {
        throw "Python not found"
    }
} catch {
    Write-Host "[ERROR] Python not found. Please install Python first." -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/downloads/"
    Write-Host "Make sure to check 'Add Python to PATH' during installation."
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if virtual environment exists
if (!(Test-Path "venv")) {
    Write-Host "[SETUP] Creating Python virtual environment..."
    
    try {
        python -m venv venv
        Write-Host "[OK] Virtual environment created" -ForegroundColor Green
    } catch {
        Write-Host "[ERROR] Failed to create virtual environment" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# Activate virtual environment
Write-Host "[SETUP] Activating virtual environment..."
try {
    & "venv\Scripts\Activate.ps1"
    Write-Host "[OK] Virtual environment activated" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Failed to activate virtual environment" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Install Python dependencies
Write-Host "[SETUP] Installing Python dependencies..."
try {
    pip install -r requirements.txt
    Write-Host "[OK] Dependencies installed successfully" -ForegroundColor Green
} catch {
    Write-Host "[WARN] Standard pip install failed, trying alternative method..."
    try {
        python -m pip install -r requirements.txt
        Write-Host "[OK] Dependencies installed successfully" -ForegroundColor Green
    } catch {
        Write-Host "[ERROR] Failed to install dependencies" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

# Check if .env file exists
if (!(Test-Path ".env")) {
    Write-Host "[SETUP] Creating environment configuration file..."
    Write-Host ""
    Write-Host "You need to add your OpenAI API key to the .env file"
    Write-Host "Get your API key from: https://platform.openai.com/api-keys"
    Write-Host ""
    
    # Create .env file template
    @"
OPENAI_API_KEY=your_api_key_here
DATABASE_PATH=finbin_farm_data.db
OPENAI_MODEL=gpt-3.5-turbo
MAX_TOKENS=1000
TEMPERATURE=0.7
"@ | Out-File -FilePath ".env" -Encoding UTF8
    
    Write-Host "[OK] .env file created" -ForegroundColor Green
    Write-Host "[IMPORTANT] You must edit the .env file and add your actual OpenAI API key!" -ForegroundColor Yellow
    Write-Host ""
    
    # Open .env file for editing
    notepad .env
    
    Read-Host "Press Enter after you've added your API key"
}

# Navigate to src directory
Set-Location "src"

# Check if database exists
if (!(Test-Path "finbin_farm_data.db")) {
    Write-Host "[SETUP] Creating database with sample data..."
    
    try {
        python create_database.py
        Write-Host "[OK] Database created successfully" -ForegroundColor Green
    } catch {
        Write-Host "[ERROR] Failed to create database" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
} else {
    Write-Host "[OK] Database already exists" -ForegroundColor Green
}

# Verify database has data
Write-Host "[CHECK] Verifying database contents..."
try {
    python check_database.py
    Write-Host "[OK] Database verification successful" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Database verification failed" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "========================================"
Write-Host "           APPLICATION READY!"
Write-Host "========================================"
Write-Host ""
Write-Host "Your Farm Financial Data RAG Application is ready!" -ForegroundColor Green
Write-Host ""
Write-Host "[LAUNCH] Starting web interface..."
Write-Host "Web interface: http://localhost:8000/web_interface.html"
Write-Host "API docs: http://localhost:8000/docs"
Write-Host ""
Write-Host "Press Ctrl+C to stop the server when you're done"
Write-Host ""

# Start the web interface
try {
    python farm_rag_api.py
} catch {
    Write-Host "[ERROR] Failed to start web server: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "[INFO] Web server has stopped" -ForegroundColor Yellow
Write-Host ""
Write-Host "To run the application again, just double-click this file."
Write-Host ""
Read-Host "Press Enter to exit"
