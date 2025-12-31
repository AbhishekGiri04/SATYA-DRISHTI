import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

class ImageExtractor:
    def extract_images(self, html: str, base_url: str) -> list:
        soup = BeautifulSoup(html, 'html.parser')
        images = []
        
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src')
            if src and self._is_valid_image(src):
                if src.startswith('//'):
                    src = 'https:' + src
                elif src.startswith('/'):
                    src = base_url + src
                images.append(src)
        
        return images[:5]
    
    def _is_valid_image(self, url: str) -> bool:
        if not url or len(url) < 10:
            return False
        valid_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
        return any(url.lower().endswith(ext) for ext in valid_exts) or 'image' in url.lower()
    
    def download_image(self, url: str):
        try:
            headers = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://www.reddit.com/'}
            response = requests.get(url, timeout=10, headers=headers, stream=True)
            img = Image.open(BytesIO(response.content)).convert('RGB')
            # Normalize size for consistent model input
            img = img.resize((512, 512), Image.Resampling.LANCZOS)
            return img
        except Exception as e:
            return None
