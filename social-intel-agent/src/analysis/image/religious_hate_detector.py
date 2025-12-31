from transformers import pipeline

class ReligiousHateDetector:
    def __init__(self):
        try:
            self.classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
        except:
            self.classifier = None
    
    def detect(self, image, nsfw_result=None):
        if not self.classifier or image is None:
            return {"is_religious_hate": False, "confidence": 0.0, "targets": [], "symbols": []}
        
        try:
            # Religious symbols
            symbol_labels = ["mosque", "quran", "kaaba", "islamic symbol", "crescent moon", 
                           "cross", "jesus", "church", "bible", "christian symbol",
                           "om symbol", "hindu god", "shiva", "hindu temple",
                           "menorah", "torah", "synagogue", "star of david",
                           "buddha", "buddhist temple", "sikh khanda", "safe content"]
            
            # Hate context
            hate_labels = ["anti-muslim hate", "anti-hindu hate", "anti-christian hate", 
                          "anti-jewish hate", "religious hate meme", "insulting god", 
                          "religious violence", "safe content"]
            
            # Extremist symbols
            extremist_labels = ["isis flag", "nazi symbol", "kkk logo", "swastika", 
                              "extremist symbol", "safe content"]
            
            symbols_result = self.classifier(image, candidate_labels=symbol_labels)
            hate_result = self.classifier(image, candidate_labels=hate_labels)
            extremist_result = self.classifier(image, candidate_labels=extremist_labels)
            
            detected_symbols = [l for l, s in zip(symbols_result['labels'], symbols_result['scores']) 
                              if l != "safe content" and s > 0.25]
            
            detected_hate = [l for l, s in zip(hate_result['labels'], hate_result['scores']) 
                           if l != "safe content" and s > 0.4]
            
            detected_extremist = [l for l, s in zip(extremist_result['labels'], extremist_result['scores']) 
                                if l != "safe content" and s > 0.4]
            
            max_hate_score = max([s for l, s in zip(hate_result['labels'], hate_result['scores']) 
                                 if l != "safe content"], default=0.0)
            
            # Check if NSFW + religious symbols = hateful (confidence-based)
            is_nsfw_religious_hate = False
            if nsfw_result and detected_symbols:
                nsfw_confidence = nsfw_result.get('confidence', 0)
                if nsfw_confidence > 0.5:
                    is_nsfw_religious_hate = True
                    detected_hate.append("sexual content with religious imagery")
                    # Combine confidences for more accurate scoring
                    symbol_confidence = max([s for l, s in zip(symbols_result['labels'], symbols_result['scores']) 
                                           if l in detected_symbols], default=0.5)
                    max_hate_score = max(max_hate_score, (nsfw_confidence + symbol_confidence) / 2)
            
            return {
                "is_religious_hate": len(detected_hate) > 0 or len(detected_extremist) > 0 or is_nsfw_religious_hate,
                "confidence": max_hate_score,
                "religious_symbols": detected_symbols,
                "hate_context": detected_hate,
                "extremist_symbols": detected_extremist,
                "targets": self._extract_targets(detected_hate)
            }
        except:
            return {"is_religious_hate": False, "confidence": 0.0, "targets": [], "symbols": []}
    
    def _extract_targets(self, hate_labels):
        targets = []
        if any('muslim' in l.lower() for l in hate_labels):
            targets.append("Muslims")
        if any('hindu' in l.lower() for l in hate_labels):
            targets.append("Hindus")
        if any('christian' in l.lower() for l in hate_labels):
            targets.append("Christians")
        if any('jewish' in l.lower() or 'jew' in l.lower() for l in hate_labels):
            targets.append("Jews")
        return targets
