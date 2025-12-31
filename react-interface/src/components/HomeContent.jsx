import React from 'react';
import './HomeContent.css';

function HomeContent() {
  return (
    <div className="home-content">
      <div className="features-grid">
        <div className="feature-card">
          <div className="feature-icon">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
            </svg>
          </div>
          <h3>Content Safety</h3>
          <p>Advanced AI detection of harmful content, hate speech, and toxic material</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <circle cx="12" cy="12" r="10"/>
              <path d="M8 14s1.5 2 4 2 4-2 4-2"/>
              <line x1="9" y1="9" x2="9.01" y2="9"/>
              <line x1="15" y1="9" x2="15.01" y2="9"/>
            </svg>
          </div>
          <h3>Sentiment Analysis</h3>
          <p>Understand emotional tone and sentiment with 95% accuracy</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
            </svg>
          </div>
          <h3>Real-time Analysis</h3>
          <p>Instant results with comprehensive risk scores in 10-15 seconds</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="2" y1="12" x2="22" y2="12"/>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
          </div>
          <h3>Multi-Platform Support</h3>
          <p>Compatible with Reddit, Twitter, YouTube, Instagram, and news sites</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <line x1="12" y1="20" x2="12" y2="10"/>
              <line x1="18" y1="20" x2="18" y2="4"/>
              <line x1="6" y1="20" x2="6" y2="16"/>
            </svg>
          </div>
          <h3>Risk Assessment</h3>
          <p>Comprehensive 0-100 scale scoring with detailed risk factors</p>
        </div>

        <div className="feature-card">
          <div className="feature-icon">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <circle cx="11" cy="11" r="8"/>
              <path d="m21 21-4.35-4.35"/>
            </svg>
          </div>
          <h3>Deep Insights</h3>
          <p>Detailed analysis covering toxicity, hate speech, and NSFW content</p>
        </div>
      </div>

      <div className="cta-section">
        <h2>How to Use</h2>
        <div className="steps">
          <div className="step">
            <div className="step-box">1</div>
            <p>Enter URL</p>
          </div>
          <div className="step-arrow">→</div>
          <div className="step">
            <div className="step-box">2</div>
            <p>Analyze</p>
          </div>
          <div className="step-arrow">→</div>
          <div className="step">
            <div className="step-box">3</div>
            <p>View Report</p>
          </div>
        </div>
      </div>

      <div className="info-banner">
        <h3>Government of India Initiative</h3>
        <p>12 AI Models • 87% Accuracy • Real-time Analysis • Digital India</p>
      </div>
    </div>
  );
}

export default HomeContent;
