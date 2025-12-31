from src.services.universal_scraper_service import UniversalScraperService
from src.analysis.text.sentiment import SentimentAnalyzer
from src.analysis.text.toxicity import ToxicityDetector
from src.analysis.text.hate_speech import HateSpeechDetector
from src.analysis.text.content_classifier import ContentClassifier
from src.analysis.text.intent_detector import IntentDetector
from src.analysis.text.nsfw_detector import NSFWDetector
from src.analysis.image.image_analyzer import ImageAnalyzer
from src.analysis.scoring.risk_score import RiskScorer
from src.config.logger import setup_logger
import uuid
from datetime import datetime

logger = setup_logger(__name__)

class UniversalAnalysisDispatcher:
    """Universal analysis dispatcher with complete AI analysis"""
    
    def __init__(self):
        self.scraper = UniversalScraperService()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.toxicity_detector = ToxicityDetector()
        self.hate_speech_detector = HateSpeechDetector()
        self.content_classifier = ContentClassifier()
        self.intent_detector = IntentDetector()
        self.nsfw_detector = NSFWDetector()
        self.image_analyzer = ImageAnalyzer()
        self.risk_scorer = RiskScorer()
    
    async def analyze(self, url: str, deep_analysis: bool = False):
        """Complete analysis pipeline"""
        try:
            # Step 1: Extract content
            logger.info(f"Starting analysis for {url}")
            extracted_data = await self.scraper.scrape(url)
            
            text_content = extracted_data.get("text", "").strip()
            
            if not text_content or len(text_content) < 10:
                return {
                    "analysis_id": str(uuid.uuid4()),
                    "timestamp": datetime.utcnow().isoformat(),
                    "url": url,
                    "platform": extracted_data.get("platform", "unknown"),
                    "status": "error",
                    "message": "No meaningful text content found"
                }
            
            # Truncate for analysis
            analysis_text = text_content[:512]
            
            # Step 2: Sentiment analysis
            logger.info("Analyzing sentiment")
            sentiment = self.sentiment_analyzer.analyze(analysis_text)
            
            # Step 3: Toxicity detection
            logger.info("Detecting toxicity")
            toxicity = self.toxicity_detector.detect(analysis_text)
            
            # Step 4: Hate speech detection
            logger.info("Detecting hate speech")
            hate_speech = self.hate_speech_detector.detect(analysis_text)
            
            # Step 5: Content classification
            logger.info("Classifying content categories")
            content_categories = self.content_classifier.classify(analysis_text)
            
            # Step 6: Intent detection
            logger.info("Detecting intent")
            intent = self.intent_detector.detect(analysis_text)
            
            # Step 7: NSFW detection
            logger.info("Detecting NSFW content")
            nsfw = self.nsfw_detector.detect(analysis_text)
            
            # Step 8: Image analysis with OCR text analysis
            logger.info("Analyzing images")
            image_analysis = []
            try:
                html = extracted_data.get('html', '')
                base_url = extracted_data.get('base_url', url)
                logger.info(f"HTML length: {len(html) if html else 0}, Base URL: {base_url}")
                
                if html:
                    # Create text analyzer function for OCR
                    def analyze_ocr_text(text):
                        return {
                            "sentiment": self.sentiment_analyzer.analyze(text[:512]),
                            "toxicity": self.toxicity_detector.detect(text[:512]),
                            "hate_speech": self.hate_speech_detector.detect(text[:512]),
                            "content_categories": self.content_classifier.classify(text[:512]),
                            "risk_assessment": self.risk_scorer.calculate({
                                "sentiment": self.sentiment_analyzer.analyze(text[:512]),
                                "toxicity": self.toxicity_detector.detect(text[:512]),
                                "hate_speech": self.hate_speech_detector.detect(text[:512]),
                                "content_categories": self.content_classifier.classify(text[:512]),
                                "intent": {"intent": "unknown", "confidence": 0},
                                "nsfw": self.nsfw_detector.detect(text[:512])
                            })
                        }
                    
                    image_analysis = self.image_analyzer.analyze_images(html, base_url, analyze_ocr_text)
                    logger.info(f"Image analysis completed: {len(image_analysis)} images analyzed")
                else:
                    logger.warning("No HTML content available for image extraction")
            except Exception as e:
                logger.error(f"Image analysis failed: {str(e)}", exc_info=True)
            

            
            # Step 10: Calculate risk score
            analysis_data = {
                "sentiment": sentiment,
                "toxicity": toxicity,
                "hate_speech": hate_speech,
                "content_categories": content_categories,
                "intent": intent,
                "nsfw": nsfw,
                "image_analysis": image_analysis
            }
            
            risk_assessment = self.risk_scorer.calculate(analysis_data)
            
            # Calculate combined risk
            image_risk = self._calculate_combined_image_risk(image_analysis)
            text_risk = risk_assessment['score']
            combined_risk = int(text_risk * 0.6 + image_risk * 0.4)
            combined_level = self._get_risk_level(combined_risk)
            
            # Step 11: Generate report
            logger.info(f"Generating report with {len(image_analysis)} images, combined risk: {combined_risk}")
            
            report = {
                "analysis_id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "url": url,
                "platform": extracted_data.get("detected_platform", "unknown"),
                "status": "completed",
                "metadata": {
                    "title": extracted_data.get("title", ""),
                    "author": extracted_data.get("author", ""),
                    "published_at": extracted_data.get("published_at", "")
                },
                "risk_assessment": risk_assessment,
                "image_analysis": image_analysis,
                "combined_risk": {
                    "score": combined_risk,
                    "level": combined_level,
                    "text_risk": text_risk,
                    "image_risk": image_risk
                },
                "content_analysis": {
                    "sentiment": sentiment,
                    "toxicity": toxicity,
                    "hate_speech": hate_speech,
                    "content_categories": content_categories,
                    "intent": intent,
                    "nsfw": nsfw
                },
                "summary": self._generate_summary(risk_assessment, sentiment, toxicity, hate_speech, content_categories, intent, nsfw, image_analysis),
                "text_preview": text_content[:200] + ("..." if len(text_content) > 200 else "")
            }
            
            logger.info(f"Analysis completed with risk level: {risk_assessment['level']}")
            return report
            
        except Exception as e:
            logger.error(f"Analysis failed: {str(e)}")
            return {
                "analysis_id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "url": url,
                "status": "error",
                "message": str(e)
            }
    
    def _generate_summary(self, risk, sentiment, toxicity, hate_speech, content_categories, intent, nsfw, image_analysis):
        """Generate human-readable summary"""
        summary_parts = []
        
        # Image analysis summary
        if image_analysis:
            nsfw_images = sum(1 for img in image_analysis if img.get('nsfw', {}).get('is_nsfw'))
            explicit_images = sum(1 for img in image_analysis if img.get('nsfw', {}).get('is_explicit'))
            violent_images = sum(1 for img in image_analysis if img.get('violence', {}).get('is_violent'))
            hateful_visuals = sum(1 for img in image_analysis if img.get('violence', {}).get('is_hateful_visual'))
            spam_images = sum(1 for img in image_analysis if img.get('violence', {}).get('is_spam'))
            religious_hate_images = sum(1 for img in image_analysis if img.get('religious_hate', {}).get('is_religious_hate'))
            ocr_detected = sum(1 for img in image_analysis if img.get('ocr', {}).get('text'))
            
            if explicit_images:
                summary_parts.append(f"{explicit_images} explicit image(s) detected.")
            elif nsfw_images:
                summary_parts.append(f"{nsfw_images} NSFW image(s) detected.")
            if violent_images:
                summary_parts.append(f"{violent_images} violent image(s) detected.")
            if hateful_visuals:
                summary_parts.append(f"{hateful_visuals} hateful visual(s) detected.")
            if religious_hate_images:
                summary_parts.append(f"{religious_hate_images} religious hate image(s) detected.")
            if spam_images:
                summary_parts.append(f"{spam_images} spam image(s) detected.")
            if ocr_detected:
                summary_parts.append(f"Text extracted from {ocr_detected} image(s) and analyzed.")
        
        # NSFW check
        if nsfw.get('is_nsfw') and nsfw.get('confidence', 0) > 0.6:
            summary_parts.append("Explicit adult or sexual content detected in text.")
        
        intent_type = intent.get('intent', 'unknown')
        if intent_type == 'reporting' and not nsfw.get('is_nsfw'):
            summary_parts.append("The content appears to be news reporting or factual discussion.")
        elif intent_type == 'endorsing':
            summary_parts.append("The content may be endorsing or promoting harmful content.")
        
        if risk['level'] in ['CRITICAL', 'HIGH']:
            summary_parts.append(f"High risk detected (Score: {risk['score']}/100).")
        elif risk['level'] == 'MEDIUM':
            summary_parts.append(f"Moderate risk detected (Score: {risk['score']}/100).")
        else:
            summary_parts.append(f"Low risk content (Score: {risk['score']}/100).")
        
        if toxicity.get('is_toxic') and toxicity.get('confidence', 0) > 0.7:
            summary_parts.append("Contains toxic language.")
        
        if hate_speech.get('is_hate_speech') and hate_speech.get('confidence', 0) > 0.7:
            summary_parts.append("Hate speech detected.")
        
        detected = content_categories.get('detected_categories', [])
        if detected:
            cat_str = ", ".join(detected)
            summary_parts.append(f"Categories: {cat_str}.")
        
        if risk.get('reasons'):
            summary_parts.extend(risk['reasons'])
        
        return " ".join(summary_parts) if summary_parts else "Content analyzed successfully."
    
    def _calculate_combined_image_risk(self, image_analysis):
        if not image_analysis:
            return 0
        scores = [img.get('image_risk_score', 0) for img in image_analysis]
        return int(sum(scores) / len(scores)) if scores else 0
    
    def _get_risk_level(self, score):
        if score >= 70:
            return "CRITICAL"
        elif score >= 50:
            return "HIGH"
        elif score >= 30:
            return "MEDIUM"
        elif score >= 15:
            return "LOW"
        return "SAFE"
