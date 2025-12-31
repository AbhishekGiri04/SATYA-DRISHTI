import warnings
warnings.filterwarnings('ignore', message='.*image_processor_type.*')

from transformers import pipeline

class ViolenceDetector:
    def __init__(self):
        try:
            # Lightweight CLIP model for zero-shot classification
            self.classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")
        except:
            self.classifier = None
    
    def detect(self, image):
        if not self.classifier or image is None:
            return {"is_violent": False, "is_hateful_visual": False, "is_spam": False, "confidence": 0.0}
        
        try:
            # Comprehensive visual content labels
            violence_labels = ["weapons", "guns", "knives", "violence", "blood", "gore", "physical fight", "war"]
            hate_labels = ["hateful symbols", "hate speech visual", "discriminatory imagery", "offensive gestures"]
            spam_labels = ["spam advertisement", "clickbait", "promotional banner", "fake news thumbnail"]
            safe_labels = ["safe content", "normal image"]
            
            all_labels = violence_labels + hate_labels + spam_labels + safe_labels
            result = self.classifier(image, candidate_labels=all_labels)
            
            scores_dict = {label: score for label, score in zip(result['labels'], result['scores'])}
            
            # Calculate category scores
            violence_score = max([scores_dict.get(l, 0) for l in violence_labels])
            hate_score = max([scores_dict.get(l, 0) for l in hate_labels])
            spam_score = max([scores_dict.get(l, 0) for l in spam_labels])
            
            detected_categories = []
            if violence_score > 0.4:
                detected_categories.extend([l for l in violence_labels if scores_dict.get(l, 0) > 0.4])
            if hate_score > 0.4:
                detected_categories.extend([l for l in hate_labels if scores_dict.get(l, 0) > 0.4])
            if spam_score > 0.3:
                detected_categories.extend([l for l in spam_labels if scores_dict.get(l, 0) > 0.3])
            
            return {
                "is_violent": violence_score > 0.4,
                "is_hateful_visual": hate_score > 0.4,
                "is_spam": spam_score > 0.3,
                "confidence": max(violence_score, hate_score, spam_score),
                "violence_score": violence_score,
                "hate_score": hate_score,
                "spam_score": spam_score,
                "detected_categories": detected_categories,
                "all_scores": scores_dict
            }
        except:
            return {"is_violent": False, "is_hateful_visual": False, "is_spam": False, "confidence": 0.0}
