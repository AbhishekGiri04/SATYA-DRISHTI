import React from 'react';
import './InfoSections.css';

function Docs() {
  return (
    <div className="info-section">
      <h2>API Documentation</h2>

      <div className="doc-section">
        <h3>1. URL Analysis Endpoint</h3>
        <div className="code-block">
          POST http://localhost:8001/analyze/
        </div>
        <p><strong>Request:</strong></p>
        <div className="code-block">
{`{
  "url": "https://reddit.com/r/example/post",
  "deep_analysis": false
}`}
        </div>
        <p><strong>Response:</strong></p>
        <div className="code-block">
{`{
  "analysis_id": "uuid",
  "url": "https://reddit.com/r/example/post",
  "platform": "reddit",
  "status": "completed",
  "risk_assessment": {
    "score": 65,
    "level": "HIGH",
    "factors": ["hate_speech", "nsfw_content"],
    "reasons": ["Content appears to be endorsing harmful content"]
  },
  "content_analysis": {
    "sentiment": {"label": "NEGATIVE", "score": 0.82},
    "toxicity": {"is_toxic": true, "confidence": 0.75},
    "hate_speech": {"is_hate_speech": true, "confidence": 0.81},
    "intent": {"intent": "endorsing", "confidence": 0.78},
    "nsfw": {"is_nsfw": false, "confidence": 0.12},
    "content_categories": {
      "primary_category": "hate",
      "detected_categories": ["hate", "violence"]
    }
  },
  "image_analysis": [
    {
      "image_url": "https://example.com/image.jpg",
      "nsfw": {"is_nsfw": true, "confidence": 0.87},
      "violence": {"is_violent": true, "confidence": 0.72},
      "religious_hate": {
        "is_religious_hate": true,
        "religious_symbols": ["mosque"],
        "hate_context": ["sexual content with religious imagery"]
      },
      "ocr": {"text": "extracted text"},
      "image_risk_score": 85
    }
  ],
  "combined_risk": {
    "score": 72,
    "level": "CRITICAL",
    "text_risk": 65,
    "image_risk": 85
  }
}`}
        </div>
      </div>

      <div className="doc-section">
        <h3>2. Image Analysis Endpoint</h3>
        <div className="code-block">
          POST http://localhost:8001/analyze-image/
        </div>
        <p><strong>Request:</strong></p>
        <div className="code-block">
{`{
  "image_url": "https://example.com/image.jpg"
}`}
        </div>
        <p><strong>Response:</strong></p>
        <div className="code-block">
{`{
  "status": "success",
  "image_url": "https://example.com/image.jpg",
  "risk_score": 75,
  "nsfw": {
    "is_nsfw": true,
    "is_explicit": true,
    "is_sexual": false,
    "confidence": 0.89
  },
  "violence": {
    "is_violent": true,
    "is_hateful_visual": false,
    "is_spam": false,
    "violence_score": 0.72,
    "hate_score": 0.0,
    "spam_score": 0.0
  },
  "religious_hate": {
    "is_religious_hate": true,
    "confidence": 0.85,
    "religious_symbols": ["mosque", "cross"],
    "hate_context": ["sexual content with religious imagery"],
    "extremist_symbols": []
  },
  "ocr": {
    "text": "extracted text from image",
    "confidence": 0.92
  },
  "marked_image": "data:image/jpeg;base64,...",
  "categorization": {
    "primary_category": "religious_hate",
    "all_categories": ["explicit_nudity", "religious_hate"]
  },
  "report": {
    "summary": "Image classified as RELIGIOUS_HATE",
    "detected_issues": [
      "NSFW content detected",
      "Religious hate content detected",
      "Religious symbols: mosque, cross",
      "Hate context: sexual content with religious imagery"
    ],
    "recommendations": [
      "Content should be removed immediately"
    ]
  }
}`}
        </div>
      </div>

      <div className="doc-section">
        <h3>3. Health Check Endpoint</h3>
        <div className="code-block">
          GET http://localhost:8001/health
        </div>
        <p><strong>Response:</strong></p>
        <div className="code-block">
{`{
  "status": "healthy"
}`}
        </div>
      </div>

      <div className="doc-section">
        <h3>AI Models Used</h3>
        <table className="risk-table">
          <thead>
            <tr>
              <th>Model</th>
              <th>Purpose</th>
              <th>Size</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>facebook/bart-large-mnli</td><td>Intent, Categories, NSFW Text</td><td>1.5GB</td></tr>
            <tr><td>unitary/toxic-bert</td><td>Toxicity Detection</td><td>500MB</td></tr>
            <tr><td>facebook/roberta-hate-speech</td><td>Hate Speech</td><td>500MB</td></tr>
            <tr><td>distilbert-base-uncased</td><td>Sentiment</td><td>250MB</td></tr>
            <tr><td>Falconsai/nsfw_image_detection</td><td>NSFW Images</td><td>500MB</td></tr>
            <tr><td>openai/clip-vit-base-patch32</td><td>Violence, Hate, Religious</td><td>600MB</td></tr>
            <tr><td>EasyOCR</td><td>Text Extraction</td><td>100MB</td></tr>
          </tbody>
        </table>
        <p><strong>Total:</strong> ~3GB (auto-downloaded on first run)</p>
      </div>

      <div className="doc-section">
        <h3>24 Content Categories</h3>
        <p><strong>Harmful:</strong></p>
        <ul>
          <li>hateful, racist, sexist, religious_hate, community_hate, national_hate</li>
          <li>violent, explicit_sexual, sexual_content</li>
          <li>abusive, bullying, harassment, threats, slurs, toxic_behavior</li>
          <li>drugs, spam, marketing</li>
        </ul>
        <p><strong>Neutral:</strong></p>
        <ul>
          <li>criticism, social_commentary, news_reporting, personal_experience, safe</li>
        </ul>
      </div>

      <div className="doc-section">
        <h3>Risk Scoring Formula</h3>
        <p><strong>Text Risk:</strong></p>
        <div className="code-block">
{`base_risk = (0.4 × toxicity + 0.4 × hate_speech) × 100
+ category_penalties (terrorism +30, hate +25, violence +20)
× intent_multiplier (reporting 0.25, neutral 0.5, endorsing 1.5)
× category_multiplier (news/safe 0.3, criticism 0.6)`}
        </div>
        <p><strong>Image Risk:</strong></p>
        <div className="code-block">
{`per_image = explicit(0-35) + sexual(0-25) + violence(0-30)
          + hateful_visual(0-25) + religious_hate(0-40)
          + spam(0-10) + ocr_text(0-20)`}
        </div>
        <p><strong>Combined:</strong></p>
        <div className="code-block">
{`final_score = (text_risk × 0.6) + (image_risk × 0.4)`}
        </div>
      </div>

      <div className="doc-section">
        <h3>Risk Levels</h3>
        <table className="risk-table">
          <thead>
            <tr>
              <th>Level</th>
              <th>Score Range</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>SAFE</td><td>0-14</td><td>No harmful content detected</td></tr>
            <tr><td>LOW</td><td>15-29</td><td>Minor concerns, generally acceptable</td></tr>
            <tr><td>MEDIUM</td><td>30-49</td><td>Moderate risk, review recommended</td></tr>
            <tr><td>HIGH</td><td>50-69</td><td>Significant risk, action needed</td></tr>
            <tr><td>CRITICAL</td><td>70-100</td><td>Severe risk, immediate action required</td></tr>
          </tbody>
        </table>
      </div>

      <div className="doc-section">
        <h3>Hardware Requirements</h3>
        <p><strong>Minimum:</strong></p>
        <ul>
          <li>CPU: 4 cores</li>
          <li>RAM: 8GB</li>
          <li>Storage: 10GB</li>
          <li>GPU: Optional</li>
        </ul>
        <p><strong>Recommended:</strong></p>
        <ul>
          <li>CPU: 8+ cores</li>
          <li>RAM: 16GB</li>
          <li>Storage: 20GB</li>
          <li>GPU: NVIDIA 4GB+ VRAM (10x faster)</li>
        </ul>
      </div>

      <div className="doc-section">
        <h3>Performance</h3>
        <ul>
          <li>Text analysis: 3-5 seconds</li>
          <li>Image analysis: 2-3 seconds per image (CPU)</li>
          <li>Image analysis: &lt;1 second per image (GPU)</li>
          <li>Total: 10-15 seconds for 5 images</li>
          <li>First run: 5-10 minutes (model downloads)</li>
        </ul>
      </div>
    </div>
  );
}

export default Docs;
