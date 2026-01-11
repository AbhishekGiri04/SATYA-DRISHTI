class RiskScorer:
    def calculate(self, content: dict):
        risk_factors = []
        reasons = []
        
        # Enhanced weighted scoring with sentiment
        toxicity_score = content.get("toxicity", {}).get("confidence", 0) if content.get("toxicity", {}).get("is_toxic") else 0
        hate_score = content.get("hate_speech", {}).get("confidence", 0) if content.get("hate_speech", {}).get("is_hate_speech") else 0
        sentiment = content.get("sentiment", {}).get("label", "NEUTRAL")
        sentiment_score = content.get("sentiment", {}).get("score", 0)
        
        # Intent detection - critical for reducing false positives
        intent = content.get("intent", {}).get("intent", "unknown")
        intent_confidence = content.get("intent", {}).get("confidence", 0)
        
        # Base risk calculation with sentiment weight
        sentiment_multiplier = 1.2 if sentiment == "NEGATIVE" and sentiment_score > 0.8 else 1.0
        base_risk = (0.35 * toxicity_score + 0.45 * hate_score + 0.2 * (1 if sentiment == "NEGATIVE" else 0)) * 100 * sentiment_multiplier
        
        # Category analysis with fine-grained detection
        categories = content.get("content_categories", {})
        detected = categories.get("detected_categories", [])
        category_scores = categories.get("category_scores", {})
        primary_category = categories.get("primary_category", "safe")
        
        # Fix 3: Reduce risk for criticism and social commentary
        if primary_category in ["criticism", "social_commentary"]:
            base_risk *= 0.4  # 60% reduction
            reasons.append("Content is criticism or social commentary, not harmful")
        
        # Add category-based risk with confidence weighting
        if "threats" in detected:
            base_risk += 35 * category_scores.get("threats", 0)
            risk_factors.append("threats")
        if "violent" in detected:
            base_risk += 30 * category_scores.get("violent", 0)
            risk_factors.append("violence")
        if "hateful" in detected:
            base_risk += 28 * category_scores.get("hateful", 0)
            risk_factors.append("hate_speech")
        if "racist" in detected:
            base_risk += 30 * category_scores.get("racist", 0)
            risk_factors.append("racism")
        if "religious_hate" in detected:
            base_risk += 30 * category_scores.get("religious_hate", 0)
            risk_factors.append("religious_hate")
        if "national_hate" in detected:
            base_risk += 28 * category_scores.get("national_hate", 0)
            risk_factors.append("national_hate")
        if "community_hate" in detected:
            base_risk += 28 * category_scores.get("community_hate", 0)
            risk_factors.append("community_hate")
        if "sexist" in detected:
            base_risk += 25 * category_scores.get("sexist", 0)
            risk_factors.append("sexism")
        if "drugs" in detected:
            base_risk += 22 * category_scores.get("drugs", 0)
            risk_factors.append("drug_content")
        if "explicit_sexual" in detected:
            base_risk += 30 * category_scores.get("explicit_sexual", 0)
            risk_factors.append("explicit_content")
        if "sexual_content" in detected:
            base_risk += 20 * category_scores.get("sexual_content", 0)
            risk_factors.append("sexual_content")
        if "bullying" in detected:
            base_risk += 22 * category_scores.get("bullying", 0)
            risk_factors.append("bullying")
        if "harassment" in detected:
            base_risk += 25 * category_scores.get("harassment", 0)
            risk_factors.append("harassment")
        if "abusive" in detected:
            base_risk += 20 * category_scores.get("abusive", 0)
            risk_factors.append("abusive_language")
        if "slurs" in detected:
            base_risk += 28 * category_scores.get("slurs", 0)
            risk_factors.append("slurs")
        if "spam" in detected:
            base_risk += 10 * category_scores.get("spam", 0)
            risk_factors.append("spam")
        if "marketing" in detected:
            base_risk += 5 * category_scores.get("marketing", 0)
            risk_factors.append("marketing")
        
        # NSFW detection
        nsfw = content.get("nsfw", {})
        if nsfw.get("is_nsfw") and nsfw.get("confidence", 0) > 0.6:
            base_risk += 25
            risk_factors.append("explicit_content")
            reasons.append("Explicit adult or sexual content detected")
        
        # Misinformation detection
        misinformation = content.get("misinformation", {})
        if misinformation.get("is_misinformation") and misinformation.get("confidence", 0) > 0.5:
            base_risk += 30
            risk_factors.append("misinformation")
            reasons.append("Potential misinformation detected")
        
        # Social media patterns
        social_analysis = content.get("social_analysis", {})
        social_patterns = social_analysis.get("social_patterns", [])
        engagement_intent = social_analysis.get("engagement_intent", "normal")
        
        for pattern in social_patterns:
            if pattern["pattern"] in ["clickbait", "engagement bait"]:
                base_risk += 10 * pattern["confidence"]
                risk_factors.append("engagement_manipulation")
            elif pattern["pattern"] in ["misinformation", "conspiracy theory", "fake news"]:
                base_risk += 25 * pattern["confidence"]
                risk_factors.append("misinformation_patterns")
            elif pattern["pattern"] in ["scam", "spam"]:
                base_risk += 20 * pattern["confidence"]
                risk_factors.append("scam_content")
        
        # Intent-based adjustment - KEY IMPROVEMENT
        # Skip intent reduction for NSFW content
        if not (nsfw.get("is_nsfw") and nsfw.get("confidence", 0) > 0.6):
            if intent == "reporting" and intent_confidence > 0.6:
                base_risk *= 0.25  # Reduce by 75% for news reporting
                reasons.append("Content appears to be news reporting, not endorsement")
            elif intent == "neutral" and intent_confidence > 0.5:
                base_risk *= 0.5  # Reduce by 50% for neutral discussion
                reasons.append("Content is neutral discussion")
            elif intent == "endorsing":
                base_risk *= 1.5  # Increase for endorsement
                risk_factors.append("endorsing_harmful_content")
        
        # News/safe content detection
        if primary_category in ["news_reporting", "safe"]:
            if category_scores.get("news_reporting", 0) > 0.6 or category_scores.get("safe", 0) > 0.6:
                base_risk *= 0.3
                reasons.append("Classified as neutral news or safe content")
        
        # Personal experience gets lower risk
        if primary_category == "personal_experience":
            base_risk *= 0.6
            reasons.append("Content describes personal experience")
        

        
        # Sentiment consideration (minor weight)
        if content.get("sentiment", {}).get("label") == "NEGATIVE":
            base_risk += 5
        
        # Cap score at 100
        total_score = min(int(base_risk), 100)
        
        # Determine risk level
        if total_score >= 70:
            risk_level = "CRITICAL"
        elif total_score >= 50:
            risk_level = "HIGH"
        elif total_score >= 30:
            risk_level = "MEDIUM"
        elif total_score >= 15:
            risk_level = "LOW"
        else:
            risk_level = "SAFE"
        
        return {
            "score": total_score,
            "level": risk_level,
            "factors": risk_factors,
            "reasons": reasons
        }