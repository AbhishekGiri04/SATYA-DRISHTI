from transformers import pipeline
import re

class IntentDetector:
    """Detects if content is reporting vs endorsing harmful content"""
    
    def __init__(self):
        try:
            # Lightweight: mDeBERTa-v3-base-mnli (279MB instead of 1.5GB BART)
            self.classifier = pipeline("zero-shot-classification", 
                                      model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
        except:
            self.classifier = None
    
    def detect(self, text: str):
        if not self.classifier or not text or len(text) < 10:
            return {"intent": "unknown", "confidence": 0.0}
        
        text_lower = text.lower()
        
        # Detect self-reflection / questioning patterns
        reflection_patterns = [
            r'\bquestioning myself\b',
            r'\bwondering\b.*\bhow\b',
            r'\bam i\b.*\b(becoming|unknowingly)\b',
            r'\bi still believe\b.*\bunity\b',
            r'\bsee each other as humans\b',
            r'\bhow do you stay grounded\b',
            r'\btrying to be fair\b',
            r'\bfelt this shift\b',
        ]
        
        for pattern in reflection_patterns:
            if re.search(pattern, text_lower):
                return {
                    "intent": "personal",
                    "confidence": 0.9,
                    "all_scores": {"personal": 0.9, "neutral": 0.05, "reporting": 0.03, "endorsing": 0.02}
                }
        
        # Detect unity/peace advocacy
        unity_patterns = [
            r'\bbelieve in unity\b',
            r'\bdon\'t blame.*entire community\b',
            r'\bsee.*as humans first\b',
            r'\bstop.*cycle\b',
        ]
        
        for pattern in unity_patterns:
            if re.search(pattern, text_lower):
                return {
                    "intent": "neutral",
                    "confidence": 0.85,
                    "all_scores": {"neutral": 0.85, "personal": 0.10, "reporting": 0.03, "endorsing": 0.02}
                }
        
        try:
            chunks = self._split_into_chunks(text, max_tokens=300)
            
            if len(chunks) == 0:
                return {"intent": "unknown", "confidence": 0.0}
            
            labels = [
                "this text is reporting news about harmful content",
                "this text is endorsing harmful content",
                "this text is neutral discussion",
                "this text describes a personal experience"
            ]
            
            intent_scores = {"reporting": [], "endorsing": [], "neutral": [], "personal": []}
            
            for chunk in chunks:
                result = self.classifier(chunk, labels)
                
                for label, score in zip(result['labels'], result['scores']):
                    if "reporting news" in label:
                        intent_scores["reporting"].append(score)
                    elif "endorsing" in label:
                        intent_scores["endorsing"].append(score)
                    elif "personal experience" in label:
                        intent_scores["personal"].append(score)
                    else:
                        intent_scores["neutral"].append(score)
            
            avg_scores = {k: sum(v)/len(v) if v else 0.0 for k, v in intent_scores.items()}
            primary_intent = max(avg_scores, key=avg_scores.get)
            confidence = avg_scores[primary_intent]
            
            return {
                "intent": primary_intent,
                "confidence": confidence,
                "all_scores": avg_scores
            }
        except Exception as e:
            return {"intent": "unknown", "confidence": 0.0}
    
    def _split_into_chunks(self, text: str, max_tokens: int = 300) -> list:
        """Split text into chunks of approximately max_tokens words"""
        # Clean text first
        text = re.sub(r'@\w+|u/\w+', '', text)
        text = re.sub(r'http\S+|www\S+', '', text)
        
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), max_tokens):
            chunk = ' '.join(words[i:i+max_tokens])
            if len(chunk.strip()) > 20:  # Minimum chunk size
                chunks.append(chunk)
        
        return chunks if chunks else [text[:512]]
