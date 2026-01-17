import React, { useState } from 'react';
import './Contact.css';

function Contact() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: ''
  });
  const [notification, setNotification] = useState({ show: false, message: '', type: '' });

  const showNotification = (message, type) => {
    setNotification({ show: true, message, type });
    setTimeout(() => setNotification({ show: false, message: '', type: '' }), 5000);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await fetch('http://localhost:8001/contact/send', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      
      const data = await response.json();
      
      if (response.ok) {
        showNotification(data.message || 'Message sent successfully!', 'success');
        setFormData({ name: '', email: '', subject: '', message: '' });
      } else {
        showNotification(data.detail || 'Failed to send message. Please try again.', 'error');
      }
    } catch (error) {
      console.error('Error sending message:', error);
      showNotification('Network error. Please check your connection and try again.', 'error');
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div className="contact-container">
      {notification.show && (
        <div className={`notification ${notification.type}`}>
          <span>{notification.message}</span>
          <button onClick={() => setNotification({ show: false, message: '', type: '' })}>×</button>
        </div>
      )}

      <div className="contact-hero">
        <h1>Get in Touch</h1>
        <p className="hero-subtitle">Let's collaborate to make the digital world safer for everyone</p>
      </div>

      <div className="contact-content">
        <div className="contact-form-section">
          <h2>Send a Message</h2>
          <form onSubmit={handleSubmit} className="contact-form">
            <div className="form-group">
              <label>Your Name</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                placeholder="Enter your full name"
                required
              />
            </div>
            <div className="form-group">
              <label>Email Address</label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="your.email@example.com"
                required
              />
            </div>
            <div className="form-group full-width">
              <label>Subject</label>
              <input
                type="text"
                name="subject"
                value={formData.subject}
                onChange={handleChange}
                placeholder="What is this regarding?"
                required
              />
            </div>
            <div className="form-group full-width">
              <label>Message</label>
              <textarea
                name="message"
                value={formData.message}
                onChange={handleChange}
                placeholder="Tell us more about your inquiry..."
                rows="6"
                required
              ></textarea>
            </div>
            <button type="submit" className="submit-btn">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
              </svg>
              Send Message
            </button>
          </form>
        </div>

        <div className="contact-info-section">
          <div className="info-card">
            <div className="info-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <h3>Lead Developer</h3>
            <p className="dev-name">Abhishek Giri</p>
            <p className="dev-role">Full-Stack AI Engineer</p>
            <p className="dev-team">Team Code Catalyst</p>
            <p className="dev-desc">Specializing in AI/ML, Content Moderation & Digital Safety Solutions</p>
          </div>

          <div className="info-card">
            <div className="info-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                <polyline points="22,6 12,13 2,6"></polyline>
              </svg>
            </div>
            <h3>Email Us</h3>
            <a href="mailto:abhishekgiri1978@gmail.com" className="email-link">abhishekgiri1978@gmail.com</a>
            <p className="info-desc">For technical support, bug reports, feature requests, and general inquiries</p>
          </div>

          <div className="info-card">
            <div className="info-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
            <h3>Partnership Opportunities</h3>
            <ul className="partnership-list">
              <li>Government Agencies & Law Enforcement</li>
              <li>Social Media Platforms</li>
              <li>Educational Institutions</li>
              <li>Enterprise Organizations</li>
            </ul>
          </div>
        </div>
      </div>

      <div className="social-section">
        <h2>Connect with the Developer</h2>
        <div className="social-grid">
          <a href="https://github.com/abhishekgiri04" target="_blank" rel="noopener noreferrer" className="social-card github">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            <h3>GitHub</h3>
            <p>View source code & projects</p>
          </a>
          <a href="https://www.linkedin.com/in/abhishek-giri04/" target="_blank" rel="noopener noreferrer" className="social-card linkedin">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
            </svg>
            <h3>LinkedIn</h3>
            <p>Professional network</p>
          </a>
          <a href="https://t.me/AbhishekGiri7" target="_blank" rel="noopener noreferrer" className="social-card telegram">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
              <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
            </svg>
            <h3>Telegram</h3>
            <p>Instant messaging</p>
          </a>
        </div>
      </div>

      <div className="faq-section">
        <h2>Frequently Asked Questions</h2>
        <div className="faq-grid">
          <div className="faq-card">
            <svg className="faq-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <circle cx="12" cy="12" r="10"/>
              <path d="M9 12l2 2 4-4"/>
            </svg>
            <h4>How accurate is the AI analysis?</h4>
            <p>SATYA-DRISHTI achieves 87% overall accuracy using 12 state-of-the-art AI models. Individual models range from 83-95% accuracy: Sentiment Analysis (95%), NSFW Image Detection (94%), Toxicity Detection (92%), and Hate Speech Detection (89%).</p>
          </div>
          <div className="faq-card">
            <svg className="faq-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
            </svg>
            <h4>Is my data stored or shared?</h4>
            <p>We follow a privacy-first approach. Content is analyzed in real-time and only metadata (risk scores, timestamps) is stored in MongoDB for analytics. No personal data, images, or text content is permanently stored.</p>
          </div>
          <div className="faq-card">
            <svg className="faq-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
              <polyline points="9 22 9 12 15 12 15 22"/>
            </svg>
            <h4>Can government agencies use this?</h4>
            <p>Absolutely! SATYA-DRISHTI is specifically designed for government use with cybercell-ready reports, SHA256 evidence hashing for court admissibility, and automatic mapping to IPC Sections and IT Act provisions.</p>
          </div>
          <div className="faq-card">
            <svg className="faq-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="2" y1="12" x2="22" y2="12"/>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
            <h4>Which platforms are supported?</h4>
            <p>We support 8 major platforms: Reddit, Twitter/X, Instagram, YouTube, TikTok, News websites, Generic web pages, and Direct image URLs with platform-specific adapters.</p>
          </div>
          <div className="faq-card">
            <svg className="faq-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
            <h4>What languages are supported?</h4>
            <p>Currently supports 9 Indian languages: Hindi, Bengali, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam, and Punjabi. English is fully supported with advanced NLP models.</p>
          </div>
          <div className="faq-card">
            <svg className="faq-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
              <polyline points="17 6 23 6 23 12"/>
            </svg>
            <h4>How fast is the analysis?</h4>
            <p>Analysis takes 10-15 seconds on CPU and 3-5 seconds with GPU acceleration. All 12 AI models run in parallel for maximum efficiency.</p>
          </div>
          <div className="faq-card">
            <svg className="faq-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <line x1="12" y1="1" x2="12" y2="23"/>
              <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
            </svg>
            <h4>Is this free to use?</h4>
            <p>Yes! SATYA-DRISHTI is currently free for individual use and government agencies. For enterprise deployments with custom features, please contact us for licensing options.</p>
          </div>
          <div className="faq-card">
            <svg className="faq-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#1e40af" strokeWidth="2">
              <polyline points="16 18 22 12 16 6"/>
              <polyline points="8 6 2 12 8 18"/>
            </svg>
            <h4>Can I integrate this into my application?</h4>
            <p>Yes! We provide RESTful APIs with comprehensive documentation. Visit our API docs at /docs for integration guides, code examples, and authentication details.</p>
          </div>
        </div>
      </div>

      <div className="cta-section">
        <h2>Ready to Make Digital India Safer?</h2>
        <p>Join us in our mission to create a safer online environment for all Indians</p>
        <a href="#contact-form" onClick={() => document.querySelector('.contact-form-section').scrollIntoView({ behavior: 'smooth' })} className="cta-button">Start a Conversation</a>
      </div>
    </div>
  );
}

export default Contact;
