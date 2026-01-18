import React, { useState, useEffect } from 'react';
import './Navbar.css';
import emblem from '../emblem.svg';

function Navbar({ onSectionChange, currentSection }) {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleNavClick = (section) => {
    onSectionChange(section);
    setIsMobileMenuOpen(false);
  };

  return (
    <nav className={`navbar ${isScrolled ? 'scrolled' : ''}`}>
      <div className="nav-container">
        {/* Government Header */}
        <div className="govt-header">
          <span className="govt-text">भारत सरकार • Government of India</span>
          <div className="tricolor-line"></div>
        </div>
        
        <div className="nav-main">
          <div className="nav-brand" onClick={() => handleNavClick('home')}>
            <img src={emblem} alt="Government of India" className="govt-logo" />
            <div className="brand-text">
              <span className="brand-name">SATYA-DRISHTI</span>
              <span className="brand-tagline">National Digital Security Framework</span>
            </div>
          </div>

          {/* Desktop Navigation */}
          <div className="nav-links">
            <button
              className={`nav-btn ${currentSection === 'home' ? 'active' : ''}`}
              onClick={() => handleNavClick('home')}
            >
              <svg className="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                <polyline points="9,22 9,12 15,12 15,22"/>
              </svg>
              <span className="nav-text">Home</span>
            </button>
            <button
              className={`nav-btn ${currentSection === 'how-it-works' ? 'active' : ''}`}
              onClick={() => handleNavClick('how-it-works')}
            >
              <svg className="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
              </svg>
              <span className="nav-text">How It Works</span>
            </button>
            <button
              className={`nav-btn ${currentSection === 'about' ? 'active' : ''}`}
              onClick={() => handleNavClick('about')}
            >
              <svg className="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                <circle cx="9" cy="7" r="4"/>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
              </svg>
              <span className="nav-text">About</span>
            </button>
            <button
              className={`nav-btn ${currentSection === 'governance' ? 'active' : ''}`}
              onClick={() => handleNavClick('governance')}
            >
              <svg className="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                <path d="M9 12l2 2 4-4"/>
              </svg>
              <span className="nav-text">Governance</span>
            </button>
            <button
              className={`nav-btn ${currentSection === 'contact' ? 'active' : ''}`}
              onClick={() => handleNavClick('contact')}
            >
              <svg className="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/>
              </svg>
              <span className="nav-text">Contact</span>
            </button>
          </div>

          {/* Mobile Menu Button */}
          <button 
            className="mobile-menu-btn"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            <span className={`hamburger ${isMobileMenuOpen ? 'open' : ''}`}></span>
            <span className={`hamburger ${isMobileMenuOpen ? 'open' : ''}`}></span>
            <span className={`hamburger ${isMobileMenuOpen ? 'open' : ''}`}></span>
          </button>
        </div>

        {/* Mobile Navigation */}
        <div className={`mobile-nav ${isMobileMenuOpen ? 'open' : ''}`}>
          <button
            className={`mobile-nav-btn ${currentSection === 'home' ? 'active' : ''}`}
            onClick={() => handleNavClick('home')}
          >
            <svg className="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
              <polyline points="9,22 9,12 15,12 15,22"/>
            </svg>
            Home
          </button>
          <button
            className={`mobile-nav-btn ${currentSection === 'how-it-works' ? 'active' : ''}`}
            onClick={() => handleNavClick('how-it-works')}
          >
            <svg className="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <circle cx="12" cy="12" r="3"/>
              <path d="M12 1v6m0 6v6m11-7h-6m-6 0H1"/>
            </svg>
            How It Works
          </button>
          <button
            className={`mobile-nav-btn ${currentSection === 'about' ? 'active' : ''}`}
            onClick={() => handleNavClick('about')}
          >
            <svg className="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
              <circle cx="9" cy="7" r="4"/>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
            </svg>
            About
          </button>
          <button
            className={`mobile-nav-btn ${currentSection === 'governance' ? 'active' : ''}`}
            onClick={() => handleNavClick('governance')}
          >
            <svg className="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
              <line x1="16" y1="2" x2="16" y2="6"/>
              <line x1="8" y1="2" x2="8" y2="6"/>
              <line x1="3" y1="10" x2="21" y2="10"/>
            </svg>
            Governance
          </button>
          <button
            className={`mobile-nav-btn ${currentSection === 'contact' ? 'active' : ''}`}
            onClick={() => handleNavClick('contact')}
          >
            <svg className="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
              <polyline points="22,6 12,13 2,6"/>
            </svg>
            Contact
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
