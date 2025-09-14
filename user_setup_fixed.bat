@echo off
echo ========================================
echo    Farm Financial RAG Setup (Windows)
echo ========================================
echo.

REM Check if Python is available
echo [CHECK] Checking Python installation...
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] Python not found. Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)
echo [OK] Python found

REM Check if Git is available
echo [CHECK] Checking Git installation...
git --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] Git not found. Please install Git from https://git-scm.com
    pause
    exit /b 1
)
echo [OK] Git found

REM Navigate to src directory
cd /d "src"

REM Check if database exists and has data
echo [CHECK] Checking database...
if not exist "finbin_farm_data.db" (
    echo [INFO] Database does not exist, creating...
    goto :create_db
) else (
    echo [INFO] Database exists, checking if it has data...
    python check_database_windows.py
    if %errorLevel% neq 0 (
        echo [WARN] Database is empty or corrupted, recreating...
        del finbin_farm_data.db
        goto :create_db
    ) else (
        echo [OK] Database has data
        goto :start_app
    )
)

:create_db
echo [SETUP] Creating database with sample data...
python create_simple_db.py
if %errorLevel% neq 0 (
    echo [WARN] Standard python failed, trying python.exe...
    python.exe create_simple_db.py
    if %errorLevel% neq 0 (
        echo [ERROR] Failed to create database with both python and python.exe.
        echo Please ensure Python is installed and accessible.
        pause
        exit /b 1
    )
)

echo [VERIFY] Verifying database creation...
python check_database_windows.py
if %errorLevel% neq 0 (
    echo [ERROR] Database creation failed - database is still empty.
    echo Please check the error messages above.
    pause
    exit /b 1
)

echo [OK] Database created successfully with data

:start_app
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
    echo [WARN] Standard python failed for web interface, trying python.exe...
    python.exe farm_rag_api.py
    if %errorLevel% neq 0 (
        echo [ERROR] Failed to start web interface with both python and python.exe.
        echo Please ensure Python is installed and accessible.
        pause
        exit /b 1
    )
)

echo.
echo [INFO] Web server has stopped
echo.
echo To run the application again, just double-click this file.
pause
