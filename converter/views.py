import base64
import io
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import fitz  # PyMuPDF

# Supported image formats and their MIME types
SUPPORTED_FORMATS = {
    'JPEG': 'image/jpeg',
    'JPG': 'image/jpeg',
    'PNG': 'image/png',
    'GIF': 'image/gif',
    'BMP': 'image/bmp',
    'WEBP': 'image/webp',
    'TIFF': 'image/tiff',
    'TIF': 'image/tiff',
    'ICO': 'image/x-icon'
}

def get_mime_type(pil_format):
    """Convert PIL format to proper MIME type."""
    if not pil_format:
        return 'image/png'
    
    format_upper = pil_format.upper()
    return SUPPORTED_FORMATS.get(format_upper, f'image/{pil_format.lower()}')


def index(request):
    """Render the main converter page."""
    return render(request, 'converter/index.html')


@csrf_exempt
def convert(request):
    """Handle conversion between base64 and image."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
    try:
        # Check if it's a file upload
        if request.FILES.get('file'):
            file = request.FILES['file']
            
            # Add file size limit (10MB max)
            MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
            if file.size > MAX_FILE_SIZE:
                return JsonResponse({
                    'success': False,
                    'error': f'File too large. Maximum size is {MAX_FILE_SIZE // (1024*1024)}MB'
                }, status=400)
            
            file_name = file.name.lower()
            
            # Read the file content
            file_content = file.read()
            
            # Check if it's a PDF file
            if file_name.endswith('.pdf') or file.content_type == 'application/pdf':
                try:
                    # Validate it's a proper PDF using PyMuPDF with context manager
                    with fitz.open(stream=file_content, filetype="pdf") as pdf_document:
                        # Check if PDF is valid and has pages
                        if len(pdf_document) == 0:
                            return JsonResponse({
                                'success': False,
                                'error': 'PDF file is empty'
                            }, status=400)
                    
                    # Preserve PDF format - encode original file to base64
                    base64_string = base64.b64encode(file_content).decode('utf-8')
                    
                    # Create data URI for PDF
                    data_uri = f"data:application/pdf;base64,{base64_string}"
                    
                    return JsonResponse({
                        'success': True,
                        'type': 'pdf_to_base64',
                        'result': data_uri,
                        'format': 'PDF',
                        'message': f'PDF converted to base64 (original format preserved)'
                    })
                    
                except Exception as e:
                    return JsonResponse({
                        'success': False,
                        'error': f'Failed to process PDF: {str(e)}'
                    }, status=400)
            else:
                # Handle regular image files (JPEG, PNG, BMP, TIFF, etc.)
                try:
                    # First, validate it's a valid image using PIL with context manager
                    with Image.open(io.BytesIO(file_content)) as img:
                        # Get the format
                        original_format = img.format
                        if not original_format:
                            return JsonResponse({
                                'success': False,
                                'error': 'Unable to determine image format'
                            }, status=400)
                        
                        # Check if format is supported
                        if original_format.upper() not in SUPPORTED_FORMATS:
                            return JsonResponse({
                                'success': False,
                                'error': f'Unsupported image format: {original_format}. Supported formats: JPEG, PNG, BMP, TIFF, GIF, WebP'
                            }, status=400)
                        
                        # Get the proper MIME type
                        mime_type = get_mime_type(original_format)
                    
                    # For BMP and TIFF files, preserve the original format
                    # Convert to base64 directly from file content
                    base64_string = base64.b64encode(file_content).decode('utf-8')
                    
                    # Create data URI with correct MIME type
                    data_uri = f"data:{mime_type};base64,{base64_string}"
                    
                    return JsonResponse({
                        'success': True,
                        'type': 'image_to_base64',
                        'result': data_uri,
                        'format': original_format
                    })
                    
                except Exception as e:
                    return JsonResponse({
                        'success': False,
                        'error': f'Failed to process image: {str(e)}'
                    }, status=400)
        
        # Check if it's base64 string input
        elif request.POST.get('base64_input'):
            base64_input = request.POST.get('base64_input').strip()
            
            # Extract base64 data (handle data URI and plain base64)
            if base64_input.startswith('data:application/pdf'):
                base64_data = base64_input.split(',', 1)[1] if ',' in base64_input else base64_input
                is_pdf_uri = True
            elif base64_input.startswith('data:image'):
                base64_data = base64_input.split(',', 1)[1] if ',' in base64_input else base64_input
                is_pdf_uri = False
            else:
                # Plain base64 without data URI prefix
                base64_data = base64_input
                is_pdf_uri = False
            
            # Try to decode base64 first
            try:
                decoded_data = base64.b64decode(base64_data)
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'error': f'Invalid base64 encoding: {str(e)}'
                }, status=400)
            
            # Check if it's a PDF (try to detect by magic bytes or if explicitly marked)
            # PDF files start with %PDF- (magic bytes: 25 50 44 46 2D)
            is_pdf = decoded_data.startswith(b'%PDF-') or is_pdf_uri
            
            if is_pdf:
                # Handle PDF
                try:
                    # Validate with PyMuPDF using context manager
                    with fitz.open(stream=decoded_data, filetype="pdf") as pdf_document:
                        if len(pdf_document) == 0:
                            return JsonResponse({
                                'success': False,
                                'error': 'Decoded PDF is empty or invalid'
                            }, status=400)
                    
                    # Create proper data URI if not already present
                    if not base64_input.startswith('data:application/pdf'):
                        data_uri = f"data:application/pdf;base64,{base64_data}"
                    else:
                        data_uri = base64_input
                    
                    return JsonResponse({
                        'success': True,
                        'type': 'base64_to_pdf',
                        'result': data_uri,
                        'format': 'PDF'
                    })
                except Exception as e:
                    return JsonResponse({
                        'success': False,
                        'error': f'Invalid PDF base64 string: {str(e)}'
                    }, status=400)
            else:
                # Handle image
                try:
                    with Image.open(io.BytesIO(decoded_data)) as img:
                        # Get the proper format
                        img_format = img.format if img.format else 'PNG'
                        
                        # Get the proper MIME type
                        mime_type = get_mime_type(img_format)
                    
                    # Create data URI if not already present, otherwise use existing
                    if not base64_input.startswith('data:image'):
                        data_uri = f"data:{mime_type};base64,{base64_data}"
                    else:
                        data_uri = base64_input
                    
                    return JsonResponse({
                        'success': True,
                        'type': 'base64_to_image',
                        'result': data_uri,
                        'format': img_format
                    })
                except Exception as e:
                    return JsonResponse({
                        'success': False,
                        'error': f'Invalid base64 string or unsupported image format: {str(e)}'
                    }, status=400)
        
        else:
            return JsonResponse({
                'success': False,
                'error': 'No input provided'
            }, status=400)
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
