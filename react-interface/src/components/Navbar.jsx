import React, { useState } from 'react';
import './Navbar.css';
import emblem from '../emblem.svg';

function Navbar({ onSectionChange, currentSection }) {
  const [activeSection, setActiveSection] = useState(currentSection || 'home');

  const handleNavClick = (section) => {
    setActiveSection(section);
    onSectionChange(section);
  };

  return (
    <nav className="navbar">
      <div className="nav-container">
        <div className="nav-brand" onClick={() => handleNavClick('home')}>
          <img src={emblem} alt="Government of India" className="govt-logo" />
          <div className="brand-text">
            <span className="brand-name">SATYA-DRISHTI</span>
            <span className="brand-tagline">Digital Suraksha Framework</span>
          </div>
        </div>
        <div className="nav-links">
          <button
            className={activeSection === 'home' ? 'active' : ''}
            onClick={() => handleNavClick('home')}
          >
            Home
          </button>
          <button
            className={activeSection === 'how' ? 'active' : ''}
            onClick={() => handleNavClick('how')}
          >
            How It Works
          </button>
          <button
            className={activeSection === 'governance' ? 'active' : ''}
            onClick={() => handleNavClick('governance')}
          >
            🏛️ Governance
          </button>
          <button
            className={activeSection === 'docs' ? 'active' : ''}
            onClick={() => handleNavClick('docs')}
          >
            Documentation
          </button>
          <button
            className={activeSection === 'impact' ? 'active' : ''}
            onClick={() => handleNavClick('impact')}
          >
            Impact
          </button>
          <button
            className={activeSection === 'contact' ? 'active' : ''}
            onClick={() => handleNavClick('contact')}
          >
            Contact
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
