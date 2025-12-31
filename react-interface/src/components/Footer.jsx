import React from 'react';
import './Footer.css';

const SHIELD_ICON = 'https://cdn3d.iconscout.com/3d/premium/thumb/cyber-security-shield-3d-icon-png-download-8270466.png';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <img src={SHIELD_ICON} alt="SATYA-DRISHTI" className="footer-logo" />
          <h3>SATYA-DRISHTI</h3>
          <p className="footer-desc">AI-powered Digital Suraksha Framework with 12 AI models for comprehensive content safety analysis.</p>
          <p className="tagline">"Truth Detection through Advanced AI"</p>
        </div>

        <div className="footer-section">
          <h4>Developer</h4>
          <p><strong>Abhishek Giri</strong></p>
          <p className="dev-desc">Code Catalyst</p>
          <div className="footer-links">
            <a href="https://github.com/abhishekgiri04" target="_blank" rel="noopener noreferrer">
              GitHub
            </a>
            <a href="https://www.linkedin.com/in/abhishek-giri04/" target="_blank" rel="noopener noreferrer">
              LinkedIn
            </a>
            <a href="https://t.me/AbhishekGiri7" target="_blank" rel="noopener noreferrer">
              Telegram
            </a>
          </div>
        </div>

        <div className="footer-section">
          <h4>Key Features</h4>
          <ul>
            <li>Source Verification (Vishwaas Score)</li>
            <li>Multilingual Support (Bhashini)</li>
            <li>Legal-Ready Reports</li>
            <li>Real-time Alerting</li>
            <li>DPI Integration</li>
          </ul>
        </div>
      </div>
      
      <div className="footer-bottom">
        <p>© 2024 SATYA-DRISHTI. All Rights Reserved.</p>
        <p className="footer-credits">Built for Digital India | Developed by Code Catalyst</p>
      </div>
    </footer>
  );
}

export default Footer;
