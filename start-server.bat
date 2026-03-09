@echo off
echo ========================================
echo Base64 Image Converter - Starting Server
echo ========================================
echo.

REM Check if UV is installed
where uv >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: UV is not installed or not in PATH
    echo Please install UV first: https://github.com/astral-sh/uv
    echo.
    echo Quick install: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    pause
    exit /b 1
)

REM Check if virtual environment exists, if not create it
if not exist ".venv" (
    echo Creating virtual environment with UV...
    uv venv
    if %ERRORLEVEL% NEQ 0 (
        echo Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Sync dependencies with UV (installs from pyproject.toml)
echo Syncing dependencies...
uv sync
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to sync dependencies
    pause
    exit /b 1
)

REM Run migrations (optional - only needed for admin/auth features)
echo Running database migrations...
uv run python manage.py migrate --noinput

REM Start server in background and save PID
echo Starting Django server with Waitress (production-ready WSGI server)...
echo Server will be available at http://127.0.0.1:8000
echo Server can handle multiple concurrent requests (100-200+ requests/day)
echo.
echo Opening browser...
timeout /t 2 /nobreak >nul
start chrome http://127.0.0.1:8000

echo.
echo ========================================
echo Server is running!
echo Press Ctrl+C to stop the server
echo ========================================
echo.

REM Start the server using Waitress (production WSGI server for Windows)
REM Waitress supports multiple threads and can handle concurrent requests
uv run waitress-serve --host=127.0.0.1 --port=8000 --threads=4 base64_project.wsgi:application

REM Cleanup on exit
echo.
echo Server stopped.
pause
