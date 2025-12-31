import cv2
import numpy as np
from PIL import Image
import io
import base64

class ImageMarker:
    """Mark detected harmful regions in images"""
    
    def mark_image(self, image, detections):
        """
        Mark image with bounding boxes for detected harmful content
        Returns base64 encoded marked image
        """
        # Convert PIL to OpenCV
        img_array = np.array(image)
        img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        height, width = img_cv.shape[:2]
        marked = False
        
        # Add text overlay for detections
        y_offset = 30
        
        if detections.get('nsfw', {}).get('is_nsfw'):
            confidence = detections['nsfw'].get('confidence', 0)
            if detections['nsfw'].get('is_explicit'):
                label = f"EXPLICIT CONTENT ({confidence*100:.1f}%)"
                color = (0, 0, 255)  # Red
            elif detections['nsfw'].get('is_sexual'):
                label = f"SEXUAL CONTENT ({confidence*100:.1f}%)"
                color = (0, 100, 255)  # Orange
            else:
                label = f"NSFW ({confidence*100:.1f}%)"
                color = (0, 165, 255)  # Orange
            
            cv2.rectangle(img_cv, (10, y_offset-25), (width-10, y_offset+5), color, -1)
            cv2.putText(img_cv, label, (20, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            y_offset += 40
            marked = True
        
        if detections.get('violence', {}).get('is_violent'):
            confidence = detections['violence'].get('violence_score', 0)
            label = f"VIOLENCE DETECTED ({confidence*100:.1f}%)"
            color = (0, 0, 200)  # Dark Red
            cv2.rectangle(img_cv, (10, y_offset-25), (width-10, y_offset+5), color, -1)
            cv2.putText(img_cv, label, (20, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            y_offset += 40
            marked = True
        
        if detections.get('violence', {}).get('is_hateful_visual'):
            confidence = detections['violence'].get('hate_score', 0)
            label = f"HATEFUL CONTENT ({confidence*100:.1f}%)"
            color = (0, 0, 150)  # Brown
            cv2.rectangle(img_cv, (10, y_offset-25), (width-10, y_offset+5), color, -1)
            cv2.putText(img_cv, label, (20, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            y_offset += 40
            marked = True
        
        if detections.get('religious_hate', {}).get('is_religious_hate'):
            targets = detections['religious_hate'].get('targets', [])
            label = f"RELIGIOUS HATE: {', '.join(targets)}"
            color = (0, 50, 150)  # Dark Brown
            cv2.rectangle(img_cv, (10, y_offset-25), (width-10, y_offset+5), color, -1)
            cv2.putText(img_cv, label, (20, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            y_offset += 40
            marked = True
        
        if detections.get('violence', {}).get('is_spam'):
            confidence = detections['violence'].get('spam_score', 0)
            label = f"SPAM/SCAM ({confidence*100:.1f}%)"
            color = (0, 165, 255)  # Orange
            cv2.rectangle(img_cv, (10, y_offset-25), (width-10, y_offset+5), color, -1)
            cv2.putText(img_cv, label, (20, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            y_offset += 40
            marked = True
        
        if detections.get('ocr', {}).get('text'):
            label = "TEXT DETECTED IN IMAGE"
            color = (255, 100, 0)  # Blue
            cv2.rectangle(img_cv, (10, y_offset-25), (width-10, y_offset+5), color, -1)
            cv2.putText(img_cv, label, (20, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            marked = True
        
        # Add border if anything detected
        if marked:
            cv2.rectangle(img_cv, (5, 5), (width-5, height-5), (0, 0, 255), 5)
        
        # Convert back to PIL and encode
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)
        
        # Convert to base64
        buffered = io.BytesIO()
        pil_img.save(buffered, format="JPEG", quality=95)
        img_base64 = base64.b64encode(buffered.getvalue()).decode()
        
        return f"data:image/jpeg;base64,{img_base64}"
    
    def categorize_image(self, detections):
        """Categorize image based on detections"""
        categories = []
        primary_category = "safe"
        
        # Check all detection types
        if detections.get('nsfw', {}).get('is_explicit'):
            categories.append("explicit_nudity")
            primary_category = "explicit_nudity"
        elif detections.get('nsfw', {}).get('is_sexual'):
            categories.append("sexual_content")
            if primary_category == "safe":
                primary_category = "sexual_content"
        elif detections.get('nsfw', {}).get('is_nsfw'):
            categories.append("nsfw")
            if primary_category == "safe":
                primary_category = "nsfw"
        
        if detections.get('violence', {}).get('is_violent'):
            categories.append("violence")
            if primary_category in ["safe", "nsfw"]:
                primary_category = "violence"
        
        if detections.get('violence', {}).get('is_hateful_visual'):
            categories.append("hateful")
            if primary_category in ["safe", "nsfw", "sexual_content"]:
                primary_category = "hateful"
        
        if detections.get('religious_hate', {}).get('is_religious_hate'):
            categories.append("religious_hate")
            if primary_category in ["safe", "nsfw", "sexual_content"]:
                primary_category = "religious_hate"
        
        if detections.get('violence', {}).get('is_spam'):
            categories.append("spam_scam")
            if primary_category == "safe":
                primary_category = "spam_scam"
        
        # Check for terrorism indicators
        extremist_symbols = detections.get('religious_hate', {}).get('extremist_symbols', [])
        if extremist_symbols:
            categories.append("terrorism")
            primary_category = "terrorism"
        
        if not categories:
            categories.append("safe")
        
        return {
            "primary_category": primary_category,
            "all_categories": categories,
            "category_descriptions": self._get_category_descriptions(categories)
        }
    
    def _get_category_descriptions(self, categories):
        """Get human-readable descriptions for categories"""
        descriptions = {
            "explicit_nudity": "Contains explicit nudity or pornographic content",
            "sexual_content": "Contains sexual or suggestive content",
            "nsfw": "Not safe for work content detected",
            "violence": "Contains violent imagery, weapons, or gore",
            "hateful": "Contains hateful symbols or discriminatory imagery",
            "religious_hate": "Contains religious hate or extremist symbols",
            "terrorism": "Contains terrorism-related symbols or imagery",
            "spam_scam": "Appears to be spam, scam, or promotional content",
            "safe": "No harmful content detected"
        }
        return [descriptions.get(cat, cat) for cat in categories]
