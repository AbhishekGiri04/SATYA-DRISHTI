from .base_adapter import BaseAdapter
import subprocess
import json

class YouTubeAdapter(BaseAdapter):
    """YouTube adapter using yt-dlp"""
    
    async def extract(self, url: str):
        """Extract YouTube video metadata and transcript"""
        try:
            # Extract metadata using yt-dlp
            cmd = [
                'yt-dlp',
                '--dump-json',
                '--skip-download',
                '--no-warnings',
                url
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0:
                raise Exception(f"yt-dlp failed: {result.stderr}")
            
            data = json.loads(result.stdout)
            
            # Combine title and description as text
            text = f"{data.get('title', '')}\n\n{data.get('description', '')}"
            
            return self._create_unified_output(
                url=url,
                platform="youtube",
                title=data.get('title', ''),
                author=data.get('uploader', ''),
                published_at=data.get('upload_date', ''),
                text=text,
                meta_description=data.get('description', '')[:200],
                media=[{"type": "video", "url": url}]
            )
            
        except subprocess.TimeoutExpired:
            raise Exception("YouTube extraction timed out")
        except json.JSONDecodeError:
            raise Exception("Failed to parse YouTube data")
