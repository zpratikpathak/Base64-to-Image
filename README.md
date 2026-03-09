# 🔄 Base64 Image Converter

A modern web application built with Django that converts between Base64 strings and image files. Supports drag-and-drop, paste from clipboard, and PDF to image conversion.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ✨ Features

- ✅ **Image ↔ Base64 Conversion** - Upload images or paste Base64 strings
- ✅ **Drag & Drop Upload** - Simple file drop with visual feedback
- ✅ **Clipboard Paste** - Paste screenshots and copied images with `Ctrl+V`
- ✅ **PDF Support** - Convert first page of PDF to image
- ✅ **Multiple Formats** - PNG, JPEG, GIF, BMP, WebP, TIFF, ICO
- ✅ **Copy Output** - One-click copy of results to clipboard
- ✅ **Modern UI** - Responsive design with smooth animations

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10+**

### Installation & Running

#### 1. Install UV Package Manager

**Windows (PowerShell):**
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal after installation.

#### 2. Clone & Run

```bash
git clone https://github.com/zpratikpathak/Base64-to-Image.git
cd Base64-to-Image
```

**Windows:**
```bash
start-server.bat
```

**macOS/Linux:**
```bash
chmod +x start-server.sh
./start-server.sh
```

The server will start at: **http://127.0.0.1:8000**

---

## 📖 Usage

### Convert Image to Base64
1. Upload or drag-drop an image
2. Click **"Convert"**
3. Copy the Base64 string with the copy button

### Convert Base64 to Image
1. Paste Base64 string in the text area
2. Click **"Convert"**
3. View or download the decoded image

### Using Clipboard
- Press `Ctrl+V` to paste screenshots or copied images
- Click **"📋 Paste from Clipboard"** button

### PDF Conversion
1. Upload a PDF file
2. Click **"Convert"** - First page converts to image
3. Copy the Base64 result



---

## 🛠️ Tech Stack

- **Backend**: Django 5.2.7 with Python 3.10+
- **Image Processing**: Pillow, PyMuPDF
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Server**: Waitress WSGI server

---

## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| UV not found | Install UV: `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Port 8000 in use | Kill process: `lsof -i :8000` (macOS/Linux) or `netstat -ano \| findstr :8000` (Windows) |
| ModuleNotFoundError | Run `start-server.bat` or `./start-server.sh` to reinstall dependencies |
| Drag & Drop not working | Hard refresh: `Ctrl+Shift+R` and clear cache |
| Virtual env issues | Delete `.venv` folder and re-run the startup script |

---

## 📄 License

MIT License - feel free to use this project however you wish!

---

## 🤝 Contributing

Found a bug? Have a feature idea? Contributions are welcome!

- 🐛 [Report issues](https://github.com/zpratikpathak/Base64-to-Image/issues)
- 💡 [Suggest features](https://github.com/zpratikpathak/Base64-to-Image/issues)
- 🔧 [Submit pull requests](https://github.com/zpratikpathak/Base64-to-Image)

---

## 👨‍💻 Author

**Pratik Pathak** - [@zpratikpathak](https://github.com/zpratikpathak)

---

<div align="center">

Made with ❤️ using Django and Python

[⬆ Back to Top](#-base64-image-converter)

</div>