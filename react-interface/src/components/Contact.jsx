import React from 'react';
import './InfoSections.css';

function Contact() {
  return (
    <div className="info-section">
      <h2>Contact</h2>

      <div className="contact-grid">
        <div className="contact-card">
          <div className="contact-icon">👨‍💻</div>
          <h3>Developer</h3>
          <p><strong>Abhishek Giri</strong></p>
          <p className="contact-desc">Code Catalyst | AI Engineer</p>
        </div>

        <div className="contact-card">
          <div className="contact-icon">📧</div>
          <h3>Email</h3>
          <p>abhishekgiri04@gmail.com</p>
          <p className="contact-desc">For inquiries, support, and feedback</p>
        </div>

        <div className="contact-card">
          <div className="contact-icon">💡</div>
          <h3>Collaboration</h3>
          <p>Open for partnerships</p>
          <p className="contact-desc">Government agencies & enterprises</p>
        </div>
      </div>

      <div className="social-links">
        <h3>Connect with Abhishek Giri</h3>
        <div className="social-icons">
          <a href="https://github.com/abhishekgiri04" target="_blank" rel="noopener noreferrer" className="social-icon">GitHub</a>
          <a href="https://www.linkedin.com/in/abhishek-giri04/" target="_blank" rel="noopener noreferrer" className="social-icon">LinkedIn</a>
          <a href="https://t.me/AbhishekGiri7" target="_blank" rel="noopener noreferrer" className="social-icon">Telegram</a>
        </div>
      </div>

      <div className="faq">
        <h3>FAQ</h3>
        <div className="faq-item">
          <h4>How accurate is the analysis?</h4>
          <p>Our AI models achieve 85-95% accuracy across different content types, using state-of-the-art transformer models.</p>
        </div>
        <div className="faq-item">
          <h4>Is my data stored?</h4>
          <p>We only analyze content in real-time and don't store any personal data or analyzed content. Privacy-first approach.</p>
        </div>
        <div className="faq-item">
          <h4>Can this be used by government agencies?</h4>
          <p>Yes! SATYA-DRISHTI is designed for government use with legal-ready reports and IPC/IT Act compliance.</p>
        </div>
      </div>
    </div>
  );
}

export default Contact;
