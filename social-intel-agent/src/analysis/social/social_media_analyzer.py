from transformers import pipeline
from src.config.logger import setup_logger

logger = setup_logger(__name__)

class SocialMediaAnalyzer:
    def __init__(self):
        try:
            self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        except:
            self.classifier = None
    
    def analyze_social_content(self, text: str, platform: str):
        """Analyze social media specific patterns"""
        if not self.classifier:
            return {"social_patterns": [], "engagement_intent": "unknown"}
        
        try:
            # Social media specific labels
            social_labels = [
                "viral content", "clickbait", "engagement bait", "misinformation",
                "conspiracy theory", "fake news", "scam", "spam", "bot content",
                "influencer promotion", "normal social post"
            ]
            
            result = self.classifier(text, candidate_labels=social_labels)
            
            detected_patterns = []
            for label, score in zip(result['labels'], result['scores']):
                if label != "normal social post" and score > 0.3:
                    detected_patterns.append({
                        "pattern": label,
                        "confidence": score
                    })
            
            # Determine engagement intent
            engagement_intent = self._determine_engagement_intent(text, platform)
            
            return {
                "social_patterns": detected_patterns,
                "engagement_intent": engagement_intent,
                "platform_specific": self._platform_specific_analysis(text, platform)
            }
        except Exception as e:
            logger.error(f"Social media analysis failed: {e}")
            return {"social_patterns": [], "engagement_intent": "unknown"}
    
    def _determine_engagement_intent(self, text: str, platform: str):
        """Determine the intent behind the social media post"""
        text_lower = text.lower()
        
        # Engagement bait patterns
        if any(phrase in text_lower for phrase in ["like if", "share if", "comment if", "tag someone"]):
            return "engagement_bait"
        
        # Viral attempt patterns
        if any(phrase in text_lower for phrase in ["going viral", "share this", "spread the word"]):
            return "viral_attempt"
        
        # Promotional content
        if any(phrase in text_lower for phrase in ["buy now", "limited time", "discount", "promo code"]):
            return "promotional"
        
        # Misinformation patterns
        if any(phrase in text_lower for phrase in ["they don't want you to know", "hidden truth", "wake up"]):
            return "misinformation"
        
        return "normal"
    
    def _platform_specific_analysis(self, text: str, platform: str):
        """Platform-specific analysis patterns"""
        analysis = {"platform": platform}
        
        if platform == "twitter":
            analysis["hashtag_count"] = text.count("#")
            analysis["mention_count"] = text.count("@")
            analysis["thread_indicator"] = "1/" in text or "thread" in text.lower()
        
        elif platform == "instagram":
            analysis["hashtag_count"] = text.count("#")
            analysis["story_mention"] = "@" in text
            analysis["influencer_patterns"] = any(word in text.lower() for word in ["sponsored", "ad", "partnership"])
        
        elif platform == "tiktok":
            analysis["hashtag_count"] = text.count("#")
            analysis["trend_participation"] = any(trend in text.lower() for trend in ["challenge", "trend", "viral"])
        
        elif platform == "reddit":
            analysis["subreddit_mention"] = "r/" in text
            analysis["user_mention"] = "u/" in text
            analysis["edit_indicator"] = "edit:" in text.lower()
        
        return analysis