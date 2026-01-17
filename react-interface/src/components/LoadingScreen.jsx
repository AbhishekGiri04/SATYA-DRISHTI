import React, { useEffect, useState } from 'react';
import './LoadingScreen.css';

const LoadingScreen = ({ onComplete }) => {
  useEffect(() => {
    const timer = setTimeout(() => {
      onComplete();
    }, 3000);

    return () => clearTimeout(timer);
  }, [onComplete]);

  return (
    <div className="loading-screen">
      <div className="loading-content">
        <img 
          src="https://cdn.dribbble.com/userupload/23629041/file/original-07819f1cc87dd1ca0206af41565dc5c6.gif" 
          alt="Loading" 
          className="loading-gif"
        />
        <h1 className="loading-title">SATYA-DRISHTI</h1>
        <p className="loading-subtitle">AI-Powered Content Moderation Platform</p>
        <div className="loading-bar">
          <div className="loading-progress"></div>
        </div>
      </div>
    </div>
  );
};

export default LoadingScreen;
