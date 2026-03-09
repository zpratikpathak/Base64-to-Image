#!/bin/bash
set -e

echo "========================================"
echo "Base64 Image Converter - Starting Server"
echo "========================================"
echo ""

# Check if UV is installed
if ! command -v uv &> /dev/null; then
    echo "ERROR: UV is not installed or not in PATH"
    echo "Please install UV first: https://github.com/astral-sh/uv"
    echo ""
    echo "Quick install: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Check if virtual environment exists, if not create it
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment with UV..."
    uv venv
fi

# Sync dependencies with UV (installs from pyproject.toml)
echo "Syncing dependencies..."
uv sync

# Run migrations (optional - only needed for admin/auth features)
echo "Running database migrations..."
uv run python manage.py migrate --noinput

# Start server
echo "Starting Django server with Waitress (production-ready WSGI server)..."
echo "Server will be available at http://127.0.0.1:8000"
echo "Server can handle multiple concurrent requests (100-200+ requests/day)"
echo ""
echo "Opening browser..."
sleep 2

# Open browser (works with common Linux browsers)
if command -v xdg-open &> /dev/null; then
    xdg-open http://127.0.0.1:8000
elif command -v firefox &> /dev/null; then
    firefox http://127.0.0.1:8000 &
elif command -v chromium &> /dev/null; then
    chromium http://127.0.0.1:8000 &
elif command -v google-chrome &> /dev/null; then
    google-chrome http://127.0.0.1:8000 &
else
    echo "Note: Could not open browser automatically. Visit http://127.0.0.1:8000 manually"
fi

# Start the server
uv run python manage.py runserver 0.0.0.0:8000
