import React from 'react';
import './InfoSections.css';

function HowItWorks() {
  return (
    <div className="info-section">
      <h2>How It Works</h2>

      <div className="flow-container">
        <div className="flow-step">
          <div className="flow-number">1</div>
          <div className="flow-content">
            <h3>URL Submission</h3>
            <p>Enter any URL from Reddit, Twitter, Instagram, YouTube, news sites, or generic web content</p>
            <div className="tech-note">Platform detection using URL patterns and domain matching</div>
          </div>
        </div>

        <div className="flow-arrow">↓</div>

        <div className="flow-step">
          <div className="flow-number">2</div>
          <div className="flow-content">
            <h3>Content Extraction</h3>
            <p>Platform-specific adapters extract text and images:</p>
            <ul>
              <li>Reddit: JSON API with image gallery support</li>
              <li>News: Trafilatura for article extraction</li>
              <li>Generic: BeautifulSoup + Playwright</li>
            </ul>
            <div className="tech-note">Downloads up to 10 images per URL</div>
          </div>
        </div>

        <div className="flow-arrow">↓</div>

        <div className="flow-step">
          <div className="flow-number">3</div>
          <div className="flow-content">
            <h3>Text Analysis (7 AI Models)</h3>
            <ul>
              <li><strong>Sentiment:</strong> distilbert-base-uncased</li>
              <li><strong>Toxicity:</strong> unitary/toxic-bert (meta-context aware)</li>
              <li><strong>Hate Speech:</strong> facebook/roberta-hate-speech-dynabench</li>
              <li><strong>Categories:</strong> facebook/bart-large-mnli (24 categories)</li>
              <li><strong>Intent:</strong> facebook/bart-large-mnli (reporting/endorsing/neutral)</li>
              <li><strong>NSFW Text:</strong> facebook/bart-large-mnli</li>
            </ul>
            <div className="tech-note">Context-aware analysis reduces false positives by 80%</div>
          </div>
        </div>

        <div className="flow-arrow">↓</div>

        <div className="flow-step">
          <div className="flow-number">4</div>
          <div className="flow-content">
            <h3>Image Analysis (5 Detectors)</h3>
            <ul>
              <li><strong>NSFW:</strong> Falconsai/nsfw_image_detection (3 levels)</li>
              <li><strong>Violence:</strong> openai/clip-vit-base-patch32</li>
              <li><strong>Hateful Visual:</strong> openai/clip-vit-base-patch32</li>
              <li><strong>Religious Hate:</strong> openai/clip-vit-base-patch32 + symbol detection</li>
              <li><strong>OCR:</strong> EasyOCR with full text analysis</li>
            </ul>
            <div className="tech-note">NSFW + religious symbols = automatic hate classification</div>
          </div>
        </div>

        <div className="flow-arrow">↓</div>

        <div className="flow-step">
          <div className="flow-number">5</div>
          <div className="flow-content">
            <h3>Confidence-Based Risk Scoring</h3>
            <p>Risk calculated proportionally to model confidence:</p>
            <ul>
              <li>Text: (0.4 × toxicity + 0.4 × hate) × 100 + category penalties</li>
              <li>Image: explicit(0-35) + violence(0-30) + religious_hate(0-40)</li>
              <li>Combined: text_risk × 0.6 + image_risk × 0.4</li>
              <li>Intent adjustment: reporting ×0.25, neutral ×0.5, endorsing ×1.5</li>
            </ul>
            <div className="tech-note">Levels: SAFE(0-14), LOW(15-29), MEDIUM(30-49), HIGH(50-69), CRITICAL(70-100)</div>
          </div>
        </div>

        <div className="flow-arrow">↓</div>

        <div className="flow-step">
          <div className="flow-number">6</div>
          <div className="flow-content">
            <h3>Visual Marking & Results</h3>
            <p>OpenCV marks detected content with bounding boxes and labels</p>
            <ul>
              <li>Risk score with confidence percentages</li>
              <li>24 fine-grained categories</li>
              <li>Separate image cards with marked analysis</li>
              <li>OCR text extraction and analysis</li>
              <li>Detailed recommendations</li>
            </ul>
            <div className="tech-note">Real-time processing, no data storage</div>
          </div>
        </div>
      </div>

      <div className="architecture-section">
        <h3>Technical Architecture</h3>
        <div className="arch-grid">
          <div className="arch-card">
            <h4>Frontend</h4>
            <p>React 18 with Axios, real-time pipeline visualization, responsive design</p>
          </div>
          <div className="arch-card">
            <h4>Backend</h4>
            <p>FastAPI + PyTorch + Transformers, 7 text models + 5 image detectors</p>
          </div>
          <div className="arch-card">
            <h4>Models</h4>
            <p>~3GB total: BART, BERT, RoBERTa, DistilBERT, CLIP, Falconsai, EasyOCR</p>
          </div>
          <div className="arch-card">
            <h4>Performance</h4>
            <p>10-15s per URL (CPU), 3-5s (GPU), first run: 5-10min (downloads)</p>
          </div>
        </div>
      </div>

      <div className="privacy-section">
        <h3>Key Innovations</h3>
        <ul>
          <li><strong>Context-Aware:</strong> Intent detection distinguishes news reporting from endorsing</li>
          <li><strong>Meta-Context:</strong> Detects discussions about toxicity vs toxic content</li>
          <li><strong>Confidence-Based:</strong> Risk scores proportional to model certainty</li>
          <li><strong>Religious Hate:</strong> Combines NSFW + religious symbols for accurate detection</li>
          <li><strong>24 Categories:</strong> Fine-grained classification from hateful to safe</li>
          <li><strong>OCR Analysis:</strong> Extracts and analyzes text from memes</li>
        </ul>
      </div>
    </div>
  );
}

export default HowItWorks;
