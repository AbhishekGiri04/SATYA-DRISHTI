from transformers import pipeline
import re
from src.config.logger import setup_logger

logger = setup_logger(__name__)

class MisinformationDetector:
    def __init__(self):
        try:
            self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        except:
            self.classifier = None
    
    def detect(self, text: str):
        """Detect misinformation patterns"""
        if not self.classifier:
            return {"is_misinformation": False, "confidence": 0.0}
        
        try:
            # Misinformation labels
            labels = [
                "conspiracy theory", "fake news", "medical misinformation", 
                "political misinformation", "scientific misinformation",
                "hoax", "propaganda", "factual information"
            ]
            
            result = self.classifier(text, candidate_labels=labels)
            
            # Check for misinformation patterns
            misinfo_patterns = self._check_patterns(text)
            
            # Get highest non-factual score
            misinfo_scores = [score for label, score in zip(result['labels'], result['scores']) 
                            if label != "factual information"]
            max_misinfo_score = max(misinfo_scores) if misinfo_scores else 0.0
            
            # Combine pattern and ML detection
            pattern_boost = 0.2 if misinfo_patterns else 0.0
            final_confidence = min(max_misinfo_score + pattern_boost, 1.0)
            
            return {
                "is_misinformation": final_confidence > 0.5,
                "confidence": final_confidence,
                "detected_patterns": misinfo_patterns,
                "categories": [label for label, score in zip(result['labels'], result['scores']) 
                             if label != "factual information" and score > 0.3]
            }
        except Exception as e:
            logger.error(f"Misinformation detection failed: {e}")
            return {"is_misinformation": False, "confidence": 0.0}
    
    def _check_patterns(self, text: str):
        """Check for common misinformation patterns"""
        text_lower = text.lower()
        patterns = []
        
        # Conspiracy patterns
        conspiracy_phrases = [
            "they don't want you to know", "hidden truth", "wake up sheeple",
            "mainstream media lies", "cover up", "deep state", "new world order"
        ]
        if any(phrase in text_lower for phrase in conspiracy_phrases):
            patterns.append("conspiracy_language")
        
        # Urgency/fear patterns
        urgency_phrases = [
            "urgent", "breaking", "shocking truth", "must share", "before it's too late"
        ]
        if any(phrase in text_lower for phrase in urgency_phrases):
            patterns.append("urgency_manipulation")
        
        # False authority patterns
        authority_phrases = [
            "doctors hate this", "scientists don't want", "government hiding"
        ]
        if any(phrase in text_lower for phrase in authority_phrases):
            patterns.append("false_authority")
        
        # Emotional manipulation
        if len(re.findall(r'[!]{2,}', text)) > 2:
            patterns.append("excessive_punctuation")
        
        return patterns