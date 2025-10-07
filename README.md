# 🔄 Base64 Image Converter

A beautiful, modern web application built with Django that converts between Base64 strings and image files with support for multiple input methods and formats.

**GitHub Repository:** [https://github.com/zpratikpathak/Base64-to-Image](https://github.com/zpratikpathak/Base64-to-Image)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ✨ Features

### 🔄 Bidirectional Conversion
- **Image to Base64**: Upload any image and get a Base64-encoded string
- **Base64 to Image**: Paste a Base64 string and preview the decoded image
- **Data URI Support**: Works with both raw Base64 and data URI format

### 📄 PDF Support (NEW!)
- Upload PDF files and automatically convert the **first page** to a Base64 image
- High-quality rendering at **144 DPI** for crisp output
- Supports multi-page PDFs (extracts page 1)

### 🎯 Multiple Input Methods

#### 1. **Drag & Drop**
- Simply drag image files or PDFs from your file explorer
- Drop onto the upload area with visual feedback
- Supports all image formats and PDFs

#### 2. **Click to Upload**
- Traditional file selection dialog
- Browse and select files from your computer
- Multi-format support

#### 3. **Paste from Clipboard** 
- **Button Method**: Click "📋 Paste from Clipboard"
  - Works for screenshots (Snipping Tool, Print Screen)
  - Works for copied images from websites (Right-click → Copy Image)
  
- **Keyboard Method**: Press `Ctrl+V` anywhere
  - Paste copied image files from File Explorer
  - Paste screenshots directly
  - Auto-detects and loads the image

#### 4. **Text Input**
- Type or paste Base64 strings directly into the text area
- Automatic validation and format detection
- Supports data URIs and raw Base64

### 📋 Copy to Clipboard
- One-click button to copy conversion results
- **Clean output**: Only Base64 data URI, no extra text
- Visual confirmation when copied

### 🖼️ Multi-Format Support
**Image Formats:**
- PNG
- JPEG / JPG
- GIF
- BMP
- WebP
- TIFF
- ICO

**Document Formats:**
- PDF (converts first page to image)

### 🎨 Modern User Interface
- **Beautiful gradient design** with purple theme
- **Smooth animations** on hover and interactions
- **Responsive layout** works on desktop and mobile
- **Visual feedback** for drag-over, loading, and errors
- **Clear error messages** with helpful suggestions
- **Console logging** for debugging (F12)

### ⚡ Performance
- **Instant processing** - conversions happen in real-time
- **High-quality output** - maintains image fidelity
- **Efficient PDF rendering** - 144 DPI quality
- **Client-side validation** - fast error detection

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10+** 
- **UV Package Manager** ([Install Guide](https://github.com/astral-sh/uv))

### Installation

#### 1. Install UV (if not already installed)

**Windows (PowerShell):**
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then **restart your terminal**.

#### 2. Clone the Repository
```bash
git clone https://github.com/zpratikpathak/Base64-to-Image.git
cd Base64-to-Image
```

#### 3. Run the Application
**Windows:**
```bash
start-server.bat
```

**macOS/Linux:**
```bash
chmod +x start-server.sh
./start-server.sh
```

The script will:
- ✅ Create a virtual environment
- ✅ Install all dependencies (Django, Pillow, PyMuPDF)
- ✅ Run database migrations
- ✅ Start the Django development server
- ✅ Open your browser automatically

**Access the app at:** `http://127.0.0.1:8000`

---

## 📖 Usage Guide

### Converting Image to Base64

#### Method 1: Drag & Drop
1. Drag an image file from your file explorer
2. Drop it onto the purple upload area (it will highlight)
3. Click **"Convert"**
4. View the Base64 string below
5. Click **"📋 Copy to Clipboard"** to copy the result

#### Method 2: Click to Upload
1. Click **"📁 Click to upload or drag & drop"**
2. Select an image from your computer
3. Click **"Convert"**
4. View and copy the Base64 string

#### Method 3: Paste with Ctrl+V
1. Copy an image file from File Explorer (`Ctrl+C`)
2. Go back to the browser and press `Ctrl+V`
3. The file will be automatically loaded
4. Click **"Convert"**

#### Method 4: Screenshot Paste
1. Take a screenshot (`Win+Shift+S` or Snipping Tool)
2. Click **"📋 Paste from Clipboard"** button
3. The screenshot will be loaded
4. Click **"Convert"**

### Converting Base64 to Image

#### Method 1: Type or Paste
1. Paste your Base64 string in the text area
2. Click **"Convert"**
3. View the decoded image below
4. Click **"📋 Copy to Clipboard"** to copy the data URI

#### Method 2: Paste Button
1. Copy a Base64 string (`Ctrl+C`)
2. Click **"📋 Paste from Clipboard"** button
3. The Base64 will be automatically pasted
4. Click **"Convert"**

### Converting PDF to Base64 Image

1. Upload or drag-and-drop a PDF file
2. You'll see: "Selected: yourfile.pdf (PDF - will convert first page)"
3. Click **"Convert"**
4. The **first page** is extracted as a high-quality image
5. View the Base64 string below
6. Click **"📋 Copy to Clipboard"**

---

## 🛠️ Manual Setup (Alternative)

If you prefer manual setup without the batch file:

```bash
# Create virtual environment
uv venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
uv pip install django pillow PyMuPDF

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Then open `http://127.0.0.1:8000` in your browser.

---

## 🏗️ Project Structure

```
Base64-to-Image/
├── base64_project/          # Django project settings
│   ├── settings.py          # Configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI config
│
├── converter/               # Main application
│   ├── templates/
│   │   └── converter/
│   │       └── index.html   # Frontend UI (HTML/CSS/JS)
│   ├── views.py            # Backend logic (conversion)
│   ├── urls.py             # App URL routing
│   └── tests.py            # Test cases
│
├── manage.py               # Django management
├── pyproject.toml          # UV dependencies
├── requirements.txt        # Pip fallback
├── start-server.bat        # Windows startup script
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

---

## 🔧 Technical Details

### Backend
- **Framework**: Django 5.2.7
- **Image Processing**: Pillow (PIL)
- **PDF Processing**: PyMuPDF (fitz)
- **Database**: SQLite (for Django admin only)
- **Server**: Django development server

### Frontend
- **HTML5** with semantic markup
- **CSS3** with modern features (gradients, animations, flexbox)
- **Vanilla JavaScript** (no frameworks)
- **Clipboard API** for paste functionality
- **FileReader API** for image preview
- **Drag and Drop API** for file uploads

### Features Implementation
- **Drag & Drop**: HTML5 Drag and Drop API with inline event handlers
- **Clipboard Paste**: Clipboard API + paste event listeners
- **PDF Rendering**: PyMuPDF with 2x zoom (144 DPI)
- **Base64 Validation**: Regex pattern matching and format detection
- **Error Handling**: Comprehensive try-catch with user-friendly messages

---

## 📦 Dependencies

### Core Dependencies
```toml
django>=5.0          # Web framework
pillow>=10.0.0       # Image processing
PyMuPDF>=1.23.0      # PDF processing
```

### Installation Methods
- **UV (Recommended)**: `uv sync`
- **Pip**: `pip install -r requirements.txt`

---

## 🎨 UI Features

- **Color Scheme**: Purple gradient (`#667eea` to `#764ba2`)
- **Animations**: Smooth transitions on hover and interactions
- **Responsive**: Works on all screen sizes
- **Visual Feedback**:
  - Upload area highlights on drag-over
  - Loading spinner during conversion
  - Success messages in console
  - Error messages with helpful hints
- **Accessibility**: Clear labels and keyboard navigation support

---

## 🧪 Testing

The application includes comprehensive test coverage:

```bash
# Run all tests
python manage.py test converter

# Run with verbose output
python manage.py test converter -v 2
```

**Test Coverage:**
- Base64 to Image conversion
- Image to Base64 conversion
- PDF to Base64 conversion
- Multiple image formats (PNG, JPEG, GIF, BMP)
- Invalid input handling
- Round-trip conversion (image → base64 → image)
- URL routing
- Error cases

---

## ⚠️ Troubleshooting

### "UV is not installed" error
- Install UV using the command in Prerequisites
- Restart your terminal after installation
- Verify with: `uv --version`

### "ModuleNotFoundError: No module named 'fitz'"
- PyMuPDF not installed
- Run: `uv pip install PyMuPDF`
- Or run `start-server.bat` which installs it automatically

### Server won't start
- Check if port 8000 is already in use
- Run: `netstat -ano | findstr :8000` (Windows)
- Or: `lsof -i :8000` (macOS/Linux)
- Close any existing Django servers

### Drag & Drop not working
- Hard refresh the browser (`Ctrl+Shift+R`)
- Clear browser cache
- Make sure JavaScript is enabled

### Paste button doesn't work for copied files
- Use `Ctrl+V` instead (button works for screenshots/web images only)
- See the tip below the paste button for guidance

### Conversion fails
- Ensure the Base64 string is valid
- Check that the image file format is supported
- Verify the file size is under 10MB
- Check browser console (F12) for detailed errors

### Virtual environment issues
- Delete the `.venv` folder
- Run `start-server.bat` again to recreate it

---

## 🔐 Security Notes

### Development vs Production
- **SECRET_KEY**: Change in production (settings.py)
- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Configure for your domain
- **HTTPS**: Use SSL certificate in production

### File Upload Security
- Maximum file size: **10MB** (configurable in settings.py)
- File type validation: Server-side MIME type checking
- No file storage: Files processed in memory only
- CSRF protection: Enabled for all POST requests

---

## 📊 Browser Compatibility

| Browser | Version | Support | Notes |
|---------|---------|---------|-------|
| Chrome | 76+ | ✅ Full | Best experience |
| Edge | 79+ | ✅ Full | Chromium-based |
| Firefox | 87+ | ✅ Full | Excellent |
| Safari | 13.1+ | ✅ Full | macOS/iOS |
| Opera | 63+ | ✅ Full | Chromium-based |

**Required Browser APIs:**
- Clipboard API (for paste functionality)
- FileReader API (for image preview)
- Drag and Drop API (for file uploads)

---

## 🎯 Use Cases

- **Web Development**: Generate Base64 images for CSS/HTML
- **API Testing**: Convert images for API requests
- **Data URIs**: Embed images directly in code
- **Documentation**: Create inline image references
- **Email Templates**: Embed images in HTML emails
- **Mobile Apps**: Convert images for app data
- **PDF Preview**: Extract PDF pages as images
- **Quick Sharing**: Convert and share image data

---

## 🚦 Performance

- **Conversion Speed**: Instant (< 100ms for typical images)
- **PDF Rendering**: 1-2 seconds for first page
- **File Size Limit**: 10MB (configurable)
- **Memory Usage**: Efficient (files processed in-memory)
- **Concurrent Users**: Handles multiple simultaneous conversions

---

## 🔮 Future Enhancements

Potential features for future releases:

- [ ] Multiple page selection for PDFs
- [ ] Batch conversion (multiple files at once)
- [ ] Image compression options
- [ ] Custom resolution settings for PDFs
- [ ] History of recent conversions
- [ ] Dark mode toggle
- [ ] Download as file option
- [ ] Image editing (crop, resize, filters)
- [ ] API endpoint for programmatic access
- [ ] Docker container support

---

## 📄 License

This project is open source and available under the **MIT License**.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

**GitHub Repository:** [https://github.com/zpratikpathak/Base64-to-Image](https://github.com/zpratikpathak/Base64-to-Image)

### How to Contribute:
1. ⭐ **Star the repository** to show your support
2. 🐛 **Report bugs** by opening an issue
3. 💡 **Suggest features** in the issues section
4. 🔧 **Submit pull requests** with improvements

### Development Setup:
```bash
# Fork and clone the repo
git clone https://github.com/YOUR_USERNAME/Base64-to-Image.git

# Create a new branch
git checkout -b feature/your-feature-name

# Make your changes and commit
git commit -m "Add: your feature description"

# Push and create a pull request
git push origin feature/your-feature-name
```

---

## 👨‍💻 Author

**Pratik Pathak**

- GitHub: [@zpratikpathak](https://github.com/zpratikpathak)
- Repository: [Base64-to-Image](https://github.com/zpratikpathak/Base64-to-Image)

---

## 🙏 Acknowledgments

- **Django** - Web framework
- **Pillow** - Image processing library
- **PyMuPDF** - PDF processing library
- **UV** - Modern Python package manager

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the **Troubleshooting** section above
2. Search existing [Issues](https://github.com/zpratikpathak/Base64-to-Image/issues)
3. Open a new issue with detailed information

---

<div align="center">

**Made with ❤️ using Django and Python**

[⬆ Back to Top](#-base64-image-converter)

</div>