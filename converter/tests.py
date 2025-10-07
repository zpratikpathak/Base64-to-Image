import base64
import io
from django.test import TestCase, Client
from django.urls import reverse
from PIL import Image


class ConverterViewTests(TestCase):
    """Test cases for the base64/image converter views."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_index_view_loads(self):
        """Test that the index page loads successfully."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'converter/index.html')
        self.assertContains(response, 'Base64 Image Converter')

    def test_convert_view_get_method_not_allowed(self):
        """Test that GET requests to convert endpoint are not allowed."""
        response = self.client.get(reverse('convert'))
        self.assertEqual(response.status_code, 405)
        data = response.json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Only POST requests are allowed')

    def test_convert_no_input_provided(self):
        """Test conversion fails when no input is provided."""
        response = self.client.post(reverse('convert'))
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('No input provided', data['error'])

    def test_base64_to_image_conversion(self):
        """Test converting valid base64 string to image."""
        # Create a simple test image
        img = Image.new('RGB', (100, 100), color='red')
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_bytes = img_buffer.getvalue()
        
        # Encode to base64
        base64_string = base64.b64encode(img_bytes).decode('utf-8')
        
        # Test conversion
        response = self.client.post(reverse('convert'), {
            'base64_input': base64_string
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['type'], 'base64_to_image')
        self.assertIn('data:image/', data['result'])
        self.assertIn('base64,', data['result'])

    def test_base64_to_image_with_data_uri(self):
        """Test converting base64 data URI to image."""
        # Create a simple test image
        img = Image.new('RGB', (50, 50), color='blue')
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_bytes = img_buffer.getvalue()
        
        # Create data URI
        base64_string = base64.b64encode(img_bytes).decode('utf-8')
        data_uri = f"data:image/png;base64,{base64_string}"
        
        # Test conversion
        response = self.client.post(reverse('convert'), {
            'base64_input': data_uri
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['type'], 'base64_to_image')
        self.assertIn('data:image/', data['result'])

    def test_invalid_base64_string(self):
        """Test that invalid base64 strings are rejected."""
        response = self.client.post(reverse('convert'), {
            'base64_input': 'this-is-not-valid-base64!!!'
        })
        
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('Invalid base64', data['error'])

    def test_base64_string_not_an_image(self):
        """Test that valid base64 but not an image is rejected."""
        # Encode text as base64
        text_base64 = base64.b64encode(b"This is just text").decode('utf-8')
        
        response = self.client.post(reverse('convert'), {
            'base64_input': text_base64
        })
        
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('Invalid base64', data['error'])

    def test_image_to_base64_conversion_png(self):
        """Test converting PNG image file to base64."""
        # Create a test PNG image
        img = Image.new('RGB', (100, 100), color='green')
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        img_buffer.name = 'test_image.png'
        
        # Test conversion
        response = self.client.post(reverse('convert'), {
            'file': img_buffer
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['type'], 'image_to_base64')
        self.assertIn('data:image/', data['result'])
        self.assertIn('base64,', data['result'])

    def test_image_to_base64_conversion_jpeg(self):
        """Test converting JPEG image file to base64."""
        # Create a test JPEG image
        img = Image.new('RGB', (100, 100), color='yellow')
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='JPEG')
        img_buffer.seek(0)
        img_buffer.name = 'test_image.jpg'
        
        # Test conversion
        response = self.client.post(reverse('convert'), {
            'file': img_buffer
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['type'], 'image_to_base64')
        self.assertIn('data:image/', data['result'])
        self.assertIn('jpeg', data['result'].lower())

    def test_image_formats_supported(self):
        """Test that multiple image formats are supported."""
        formats = ['PNG', 'JPEG', 'GIF', 'BMP']
        
        for fmt in formats:
            with self.subTest(format=fmt):
                # Create test image in specific format
                img = Image.new('RGB', (50, 50), color='purple')
                img_buffer = io.BytesIO()
                img.save(img_buffer, format=fmt)
                img_buffer.seek(0)
                img_buffer.name = f'test_image.{fmt.lower()}'
                
                # Test conversion
                response = self.client.post(reverse('convert'), {
                    'file': img_buffer
                })
                
                self.assertEqual(response.status_code, 200)
                data = response.json()
                self.assertTrue(data['success'])
                self.assertEqual(data['type'], 'image_to_base64')

    def test_round_trip_conversion(self):
        """Test converting image to base64 and back to image."""
        # Create original image
        original_img = Image.new('RGB', (100, 100), color='cyan')
        img_buffer = io.BytesIO()
        original_img.save(img_buffer, format='PNG')
        original_bytes = img_buffer.getvalue()
        img_buffer.seek(0)
        img_buffer.name = 'test_image.png'
        
        # Convert image to base64
        response1 = self.client.post(reverse('convert'), {
            'file': img_buffer
        })
        self.assertEqual(response1.status_code, 200)
        data1 = response1.json()
        self.assertTrue(data1['success'])
        base64_result = data1['result']
        
        # Extract base64 string from data URI
        base64_string = base64_result.split(',', 1)[1]
        
        # Convert base64 back to image
        response2 = self.client.post(reverse('convert'), {
            'base64_input': base64_string
        })
        self.assertEqual(response2.status_code, 200)
        data2 = response2.json()
        self.assertTrue(data2['success'])
        
        # Verify the base64 strings match
        result_base64 = data2['result'].split(',', 1)[1]
        self.assertEqual(base64_string, result_base64)

    def test_empty_file_upload(self):
        """Test that empty file uploads are handled gracefully."""
        empty_file = io.BytesIO(b'')
        empty_file.name = 'empty.png'
        
        response = self.client.post(reverse('convert'), {
            'file': empty_file
        })
        
        # Should return an error
        self.assertIn(response.status_code, [400, 500])
        data = response.json()
        self.assertFalse(data['success'])

    def test_whitespace_in_base64_input(self):
        """Test that whitespace in base64 input is handled."""
        # Create a test image
        img = Image.new('RGB', (50, 50), color='orange')
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_bytes = img_buffer.getvalue()
        
        # Encode to base64 with extra whitespace
        base64_string = base64.b64encode(img_bytes).decode('utf-8')
        base64_with_whitespace = f"\n  {base64_string}  \n"
        
        # Test conversion
        response = self.client.post(reverse('convert'), {
            'base64_input': base64_with_whitespace
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])

    def test_large_image_handling(self):
        """Test handling of larger images."""
        # Create a larger test image
        img = Image.new('RGB', (1000, 1000), color='magenta')
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        img_buffer.name = 'large_test_image.png'
        
        # Test conversion
        response = self.client.post(reverse('convert'), {
            'file': img_buffer
        })
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['type'], 'image_to_base64')


class URLTests(TestCase):
    """Test URL routing."""

    def test_index_url_resolves(self):
        """Test that the index URL resolves correctly."""
        url = reverse('index')
        self.assertEqual(url, '/')

    def test_convert_url_resolves(self):
        """Test that the convert URL resolves correctly."""
        url = reverse('convert')
        self.assertEqual(url, '/convert/')
