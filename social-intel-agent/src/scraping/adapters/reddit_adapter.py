import requests
import re
from .base_adapter import BaseAdapter

class RedditAdapter(BaseAdapter):
    """Reddit adapter using JSON API with improved text cleaning"""
    
    async def extract(self, url: str):
        """Extract Reddit post using .json endpoint"""
        json_url = url.rstrip('/') + '.json'
        
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; ContentAnalyzer/1.0)'}
        response = requests.get(json_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        post_data = data[0]['data']['children'][0]['data']
        
        # Extract and clean text from post
        raw_text = post_data.get('selftext', '') or post_data.get('title', '')
        cleaned_text = self._clean_reddit_text(raw_text)
        
        # Extract images from Reddit JSON
        media = self._extract_reddit_images(post_data)
        
        # Build HTML with images for image analyzer
        html = f"<html><body><h1>{post_data.get('title', '')}</h1><p>{cleaned_text}</p>"
        for img_url in media:
            html += f'<img src="{img_url}" />'
        html += "</body></html>"
        
        return self._create_unified_output(
            url=url,
            platform="reddit",
            title=post_data.get('title', ''),
            author=post_data.get('author', ''),
            published_at=str(post_data.get('created_utc', '')),
            text=cleaned_text,
            meta_description=post_data.get('title', ''),
            media=media,
            html=html,
            base_url=url
        )
    
    def _extract_reddit_images(self, post_data: dict) -> list:
        """Extract all images from Reddit post JSON"""
        images = []
        
        # 1. Direct reddit image (i.redd.it)
        if 'url' in post_data and post_data['url'].endswith(('.jpg', '.png', '.jpeg', '.gif', '.webp')):
            images.append(post_data['url'])
        
        # 2. Preview images
        if 'preview' in post_data and 'images' in post_data['preview']:
            for item in post_data['preview']['images']:
                src = item.get('source', {}).get('url')
                if src:
                    images.append(src.replace('&amp;', '&'))
        
        # 3. Gallery posts (media_metadata)
        if 'media_metadata' in post_data:
            for item in post_data['media_metadata'].values():
                if item.get('e') == 'Image':
                    img = item.get('s', {}).get('u', '')
                    if img:
                        images.append(img.replace('&amp;', '&'))
        
        # Remove duplicates and limit to 10
        return list(dict.fromkeys(images))[:10]
    
    def _clean_reddit_text(self, text: str) -> str:
        """Fix 5: Clean Reddit text by removing noise"""
        if not text:
            return ""
        
        # Remove usernames (u/username)
        text = re.sub(r'u/\w+', '', text)
        
        # Remove subreddit mentions (r/subreddit)
        text = re.sub(r'r/\w+', '', text)
        
        # Remove quote blocks (lines starting with >)
        text = re.sub(r'^>.*$', '', text, flags=re.MULTILINE)
        
        # Remove [deleted] and [removed]
        text = re.sub(r'\[(deleted|removed)\]', '', text, flags=re.IGNORECASE)
        
        # Remove HTML entities
        text = re.sub(r'&\w+;', '', text)
        
        # Remove markdown links but keep text
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        
        # Remove URLs
        text = re.sub(r'http\S+|www\.\S+', '', text)
        
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove metadata patterns
        text = re.sub(r'Edit:.*$', '', text, flags=re.IGNORECASE)
        text = re.sub(r'Update:.*$', '', text, flags=re.IGNORECASE)
        
        return text.strip()
