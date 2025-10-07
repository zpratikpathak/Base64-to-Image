# Base64 Image Converter

A beautiful, modern web application built with Django that converts between Base64 strings and image files.

## Features

- 🔄 **Bidirectional Conversion**: Convert Base64 to images or images to Base64
- 📄 **PDF Support**: Upload PDF files and convert first page to Base64 image (NEW!)
- 📋 **Paste from Clipboard**: Intelligent paste button that detects images or base64 strings
- 🎯 **Drag & Drop**: Simply drag and drop image files or PDFs for instant conversion
- 🎨 **Modern UI**: Clean, gradient design with smooth animations
- 📋 **Copy to Clipboard**: One-click copying of conversion results
- 🖼️ **Multi-format Support**: Works with JPEG, PNG, GIF, WebP, BMP, PDF, and more
- 📱 **Responsive Design**: Works on desktop and mobile devices
- ⚡ **Fast Processing**: Instant client-server conversion

## Prerequisites

- Python 3.10 or higher
- UV package manager ([Installation guide](https://github.com/astral-sh/uv))

### Installing UV

**Windows (PowerShell):**
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Quick Start

1. **Install UV Package Manager** (if not already installed)
   ```powershell
   irm https://astral.sh/uv/install.ps1 | iex
   ```
   Then restart your terminal.

2. **Run the server**
   - Simply double-click `start-server.bat`
   - The script will automatically:
     - Create a virtual environment (.venv)
     - Install Django and Pillow
     - Run database migrations
     - Start the Django server
     - Open your browser in Chrome

3. **Start converting!**
   - The application will open in Chrome at `http://127.0.0.1:8000`
   - If Chrome doesn't open automatically, manually navigate to the URL

4. **Stop the server**
   - Press `Ctrl+C` in the batch file window

## Usage

### Converting Base64 to Image

**Option 1: Type or Paste**
1. Paste your Base64 string in the text area
2. Click "Convert"
3. View the decoded image below
4. Click "Copy to Clipboard" to copy the Base64 data URI

**Option 2: Paste from Clipboard** 📋 (NEW!)
1. Copy a Base64 string to your clipboard
2. Click "📋 Paste from Clipboard" button
3. The Base64 string will be automatically detected and pasted
4. Click "Convert"
5. View the decoded image below

### Converting Image to Base64

**Option 1: Click to Upload**
1. Click "📁 Click to upload or drag & drop"
2. Select an image from your computer
3. Click "Convert"
4. View the Base64 string below
5. Click "Copy to Clipboard" to copy the Base64 data URI

**Option 2: Drag & Drop** 🎯
1. Drag an image file from your computer
2. Drop it onto the upload area (it will highlight when you hover)
3. Click "Convert"
4. View the Base64 string below
5. Click "Copy to Clipboard"

**Option 3: Paste from Clipboard** 📋 (NEW!)

*For screenshots and copied images:*
1. Copy an image (right-click → Copy Image, or screenshot with Snipping Tool)
2. Click "📋 Paste from Clipboard" button
3. The image will be automatically detected and loaded
4. Click "Convert"
5. View the Base64 string below

*For copied files (from File Explorer):*
1. Copy an image or PDF file (Ctrl+C in File Explorer)
2. Click anywhere on the page and press **Ctrl+V**
3. The file will be automatically loaded
4. Click "Convert"
5. View the Base64 string below

**Option 4: PDF Files** 📄 (NEW!)
1. Upload or drag-and-drop a PDF file
2. The **first page** will be automatically extracted as an image
3. Click "Convert"
4. View the Base64 string of the first page
5. Click "Copy to Clipboard"

## Manual Setup (Alternative)

If you prefer manual setup:

```bash
# Create virtual environment
uv venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
uv pip install django pillow

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

## Project Structure

```
Base64/
├── base64_project/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── converter/               # Main application
│   ├── templates/
│   │   └── converter/
│   │       └── index.html   # Frontend UI
│   ├── views.py            # Conversion logic
│   └── urls.py
├── manage.py               # Django management script
├── pyproject.toml          # Python dependencies
├── start-server.bat        # Automated server startup
└── README.md
```

## Technologies Used

- **Backend**: Django 5.0
- **Image Processing**: Pillow (PIL)
- **Package Management**: UV
- **Frontend**: Vanilla JavaScript, CSS3, HTML5

## Security Notes

- This is a development server. For production use, configure proper security settings.
- The SECRET_KEY in settings.py should be changed for production.
- File upload size is limited to 10MB.

## Troubleshooting

**"UV is not installed" error:**
- Install UV using the command in Quick Start section
- Restart your terminal after installation
- Make sure UV is in your PATH

**Package build error:**
- The batch file has been updated to install dependencies directly
- If you see hatchling errors, make sure you're using the latest `start-server.bat`
- The file now uses `uv pip install django pillow` instead of package installation

**Server won't start:**
- Make sure UV is installed and in your PATH
- Check that port 8000 is not already in use
- Try: `netstat -ano | findstr :8000` to see if port is occupied
- Close any existing Django servers

**Conversion fails:**
- Ensure the Base64 string is valid
- Check that the image file format is supported
- Verify the file size is under 10MB

**Browser doesn't open automatically:**
- Manually navigate to `http://127.0.0.1:8000`
- The batch file tries to open Chrome; you can modify it for other browsers

**Virtual environment issues:**
- Delete the `.venv` folder and run `start-server.bat` again
- This will create a fresh virtual environment

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome!
