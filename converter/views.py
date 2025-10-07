import base64
import io
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import fitz  # PyMuPDF


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
            file_name = file.name.lower()
            
            # Read the file content
            file_content = file.read()
            
            # Check if it's a PDF file
            if file_name.endswith('.pdf') or file.content_type == 'application/pdf':
                try:
                    # Open PDF with PyMuPDF
                    pdf_document = fitz.open(stream=file_content, filetype="pdf")
                    
                    # Get the first page
                    if len(pdf_document) == 0:
                        return JsonResponse({
                            'success': False,
                            'error': 'PDF file is empty'
                        }, status=400)
                    
                    page = pdf_document[0]
                    
                    # Render page to image (with good quality)
                    # zoom=2 means 2x resolution (144 DPI instead of 72 DPI)
                    mat = fitz.Matrix(2, 2)
                    pix = page.get_pixmap(matrix=mat)
                    
                    # Convert pixmap to PIL Image
                    img_data = pix.tobytes("png")
                    img = Image.open(io.BytesIO(img_data))
                    
                    # Convert image to base64
                    img_buffer = io.BytesIO()
                    img.save(img_buffer, format='PNG')
                    img_bytes = img_buffer.getvalue()
                    base64_string = base64.b64encode(img_bytes).decode('utf-8')
                    
                    # Create data URI
                    data_uri = f"data:image/png;base64,{base64_string}"
                    
                    pdf_document.close()
                    
                    return JsonResponse({
                        'success': True,
                        'type': 'pdf_to_base64',
                        'result': data_uri,
                        'message': f'Converted first page of PDF to image'
                    })
                    
                except Exception as e:
                    return JsonResponse({
                        'success': False,
                        'error': f'Failed to process PDF: {str(e)}'
                    }, status=400)
            else:
                # Handle regular image files
                # Convert to base64
                base64_string = base64.b64encode(file_content).decode('utf-8')
                
                # Determine the image format
                img = Image.open(io.BytesIO(file_content))
                format_lower = img.format.lower() if img.format else 'png'
                
                # Create data URI
                data_uri = f"data:image/{format_lower};base64,{base64_string}"
                
                return JsonResponse({
                    'success': True,
                    'type': 'image_to_base64',
                    'result': data_uri
                })
        
        # Check if it's base64 string input
        elif request.POST.get('base64_input'):
            base64_input = request.POST.get('base64_input').strip()
            
            # Check if it's already a data URI
            if base64_input.startswith('data:image'):
                # It's already in the correct format
                data_uri = base64_input
                # Extract the base64 part for validation
                base64_data = base64_input.split(',', 1)[1] if ',' in base64_input else base64_input
            else:
                # It's just the base64 string
                base64_data = base64_input
                # Try to determine the image format
                try:
                    img_data = base64.b64decode(base64_data)
                    img = Image.open(io.BytesIO(img_data))
                    format_lower = img.format.lower() if img.format else 'png'
                    data_uri = f"data:image/{format_lower};base64,{base64_data}"
                except Exception as e:
                    return JsonResponse({
                        'success': False,
                        'error': 'Invalid base64 string or unsupported image format'
                    }, status=400)
            
            # Validate by decoding
            try:
                img_data = base64.b64decode(base64_data)
                img = Image.open(io.BytesIO(img_data))
                # Verify it's a valid image
                img.verify()
                
                return JsonResponse({
                    'success': True,
                    'type': 'base64_to_image',
                    'result': data_uri
                })
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid base64 string or unsupported image format'
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
