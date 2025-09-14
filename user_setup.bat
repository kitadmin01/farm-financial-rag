@echo off
title Farm Financial Data RAG Application
color 0A

echo.
echo ========================================
echo   Farm Financial Data RAG Application
echo ========================================
echo.
echo This script will run the RAG application.
echo Make sure you have Python and Git installed.
echo.

REM Check if we're in the right directory
if not exist "src\farm_rag_api.py" (
    echo [ERROR] Please run this script from the project root directory.
    echo Make sure you're in the folder containing the 'src' folder.
    echo.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo [SETUP] Creating Python virtual environment...
    python -m venv venv
    if %errorLevel% neq 0 (
        echo [ERROR] Failed to create virtual environment.
        echo Make sure Python is installed and in your PATH.
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
)

REM Activate virtual environment
echo [SETUP] Activating virtual environment...
call "venv\Scripts\activate.bat"
if %errorLevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment.
    pause
    exit /b 1
)

REM Install dependencies
echo [SETUP] Installing Python dependencies...
pip install -r requirements.txt
if %errorLevel% neq 0 (
    echo [WARN] Standard pip install failed, trying alternative method...
    python -m pip install -r requirements.txt
    if %errorLevel% neq 0 (
        echo [ERROR] Failed to install dependencies.
        pause
        exit /b 1
    )
)

REM Check if .env file exists
if not exist ".env" (
    echo [SETUP] Creating environment configuration file...
    echo.
    echo You need to add your OpenAI API key to the .env file
    echo Get your API key from: https://platform.openai.com/api-keys
    echo.
    
    echo OPENAI_API_KEY=your_api_key_here > .env
    echo DATABASE_PATH=finbin_farm_data.db >> .env
    echo OPENAI_MODEL=gpt-3.5-turbo >> .env
    echo MAX_TOKENS=1000 >> .env
    echo TEMPERATURE=0.7 >> .env
    
    echo [OK] .env file created
    echo [IMPORTANT] You must edit the .env file and add your actual OpenAI API key!
    echo.
    
    notepad .env
    echo Press any key after you've added your API key...
    pause
)

REM Navigate to src directory
cd /d "src"

REM Check if database exists
if not exist "finbin_farm_data.db" (
    echo [SETUP] Creating database with sample data...
    python create_database.py
    if %errorLevel% neq 0 (
        echo [WARN] Standard python failed, trying python3...
        python3 create_database.py
        if %errorLevel% neq 0 (
            echo [ERROR] Failed to create database with both python and python3.
            echo Please ensure Python is installed and accessible.
            pause
            exit /b 1
        )
    )
    echo [OK] Database created successfully
) else (
    echo [OK] Database already exists
)

REM Verify database has data
echo [CHECK] Verifying database contents...
python check_database.py
if %errorLevel% neq 0 (
    echo [WARN] Standard python failed for verification, trying python3...
    python3 check_database.py
    if %errorLevel% neq 0 (
        echo [ERROR] Database verification failed with both python and python3.
        pause
        exit /b 1
    )
)

echo.
echo ========================================
echo           APPLICATION READY!
echo ========================================
echo.
echo Your Farm Financial Data RAG Application is ready!
echo.
echo [LAUNCH] Starting web interface...
echo Web interface: http://localhost:8000/web_interface.html
echo API docs: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server when you're done
echo.

REM Start the web interface
python farm_rag_api.py
if %errorLevel% neq 0 (
    echo [WARN] Standard python failed for web interface, trying python3...
    python3 farm_rag_api.py
    if %errorLevel% neq 0 (
        echo [ERROR] Failed to start web interface with both python and python3.
        echo Please ensure Python is installed and accessible.
        pause
        exit /b 1
    )
)

echo.
echo [INFO] Web server has stopped
echo.
echo To run the application again, just double-click this file.
echo.
pause
