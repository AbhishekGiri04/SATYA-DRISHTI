from transformers import pipeline
import re

class ContentClassifier:
    """Multi-category content classifier with fine-grained detection"""
    
    def __init__(self):
        try:
            self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        except:
            self.classifier = None
    
    def classify(self, text: str):
        """Classify text into multiple fine-grained categories"""
        
        # Fine-grained category taxonomy with NLI hypotheses
        category_hypotheses = {
            "hateful": "this text contains hateful content or hate speech",
            "abusive": "this text contains abusive or insulting language",
            "racist": "this text contains racism or racial slurs",
            "sexist": "this text expresses sexism or gender discrimination",
            "religious_hate": "this text attacks or insults a religion or religious group",
            "community_hate": "this text attacks or insults a specific community or group",
            "national_hate": "this text contains hate speech against a nation or nationality",
            "sexual_content": "this text contains sexual content",
            "explicit_sexual": "this text contains explicit or pornographic content",
            "violent": "this text contains violence or threats of violence",
            "bullying": "this text involves bullying or harassment",
            "threats": "this text contains threats against a person or group",
            "toxic_behavior": "this text describes or exhibits toxic behavior",
            "harassment": "this text is harassing someone",
            "slurs": "this text contains slurs",
            "spam": "this text is spam or unsolicited promotional content",
            "marketing": "this text is marketing or advertising content",
            "drugs": "this text promotes or discusses illegal drugs or substance abuse",
            "criticism": "this text expresses personal criticism",
            "social_commentary": "this text discusses social issues or society",
            "news_reporting": "this text is reporting news",
            "personal_experience": "this text describes a personal experience",
            "safe": "this text is safe"
        }
        
        if not self.classifier or not text or len(text) < 10:
            return self._get_default_result()
        
        try:
            # Clean and truncate text
            analysis_text = self._preprocess_text(text)[:512]
            
            # Run multi-label zero-shot classification
            result = self.classifier(
                analysis_text, 
                list(category_hypotheses.values()), 
                multi_label=True
            )
            
            # Map results back to category keys
            category_scores = {}
            detected_categories = []
            
            hypothesis_to_key = {v: k for k, v in category_hypotheses.items()}
            
            for label, score in zip(result['labels'], result['scores']):
                category_key = hypothesis_to_key.get(label, label)
                category_scores[category_key] = round(score, 3)
                
                # Detection thresholds
                if category_key in ["criticism", "social_commentary", "personal_experience", "news_reporting", "safe"]:
                    continue  # Skip neutral categories
                
                threshold = 0.5
                if score > threshold:
                    detected_categories.append(category_key)
            
            # Determine primary category
            primary_category = self._determine_primary_category(category_scores, detected_categories)
            
            return {
                "primary_category": primary_category,
                "detected_categories": detected_categories,
                "category_scores": category_scores,
                "is_flagged": len(detected_categories) > 0
            }
            
        except Exception as e:
            return self._get_default_result()
    
    def _preprocess_text(self, text: str) -> str:
        """Clean text before analysis"""
        # Remove usernames
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'u/\w+', '', text)
        # Remove URLs
        text = re.sub(r'http\S+|www\S+', '', text)
        # Remove quote markers
        text = re.sub(r'^>.*$', '', text, flags=re.MULTILINE)
        # Remove [deleted] and [removed]
        text = re.sub(r'\[(deleted|removed)\]', '', text)
        return text.strip()
    
    def _determine_primary_category(self, scores: dict, detected: list) -> str:
        """Determine primary category with priority logic"""
        if not detected:
            # Check if it's criticism or social commentary
            if scores.get("criticism", 0) > 0.6:
                return "criticism"
            if scores.get("social_commentary", 0) > 0.6:
                return "social_commentary"
            if scores.get("news_reporting", 0) > 0.6:
                return "news_reporting"
            return "safe"
        
        # Priority order for harmful content
        priority = [
            "threats", "violent", "hateful", "racist", "religious_hate",
            "national_hate", "community_hate", "sexist", "explicit_sexual",
            "sexual_content", "drugs", "bullying", "harassment", "abusive",
            "slurs", "toxic_behavior", "spam", "marketing"
        ]
        
        for cat in priority:
            if cat in detected and scores.get(cat, 0) > 0.5:
                return cat
        
        return detected[0] if detected else "safe"
    
    def _get_default_result(self):
        """Return default result when classifier unavailable"""
        return {
            "primary_category": "safe",
            "detected_categories": [],
            "category_scores": {},
            "is_flagged": False
        }
