import React, { useState, useEffect } from 'react';
import './chat-widget.css';

const FloatingButton = ({ onClick, isOpen }) => {
  const [isHovered, setIsHovered] = useState(false);
  const [isPulsing, setIsPulsing] = useState(true);

  // Turn off pulsing after initial load
  useEffect(() => {
    const timer = setTimeout(() => {
      setIsPulsing(false);
    }, 5000); // Stop pulsing after 5 seconds

    return () => clearTimeout(timer);
  }, []);

  return (
    <button
      className={`floating-chat-button ${isOpen ? 'open' : ''} ${isHovered ? 'hovered' : ''} ${isPulsing ? 'pulsing' : ''}`}
      onClick={onClick}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      aria-label="Open chatbot"
      title="Ask AI about the book"
    >
      <div className="robot-icon">
        {/* Robot icon using SVG */}
        <svg 
          xmlns="http://www.w3.org/2000/svg" 
          viewBox="0 0 100 100" 
          width="40" 
          height="40"
          className={`robot-svg ${isOpen ? 'active' : ''}`}
        >
          {/* Robot head */}
          <circle cx="50" cy="35" r="20" fill="none" stroke="#00eeff" strokeWidth="3"/>
          
          {/* Robot eyes */}
          <circle cx="40" cy="30" r="3" fill="#00eeff" />
          <circle cx="60" cy="30" r="3" fill="#00eeff" />
          
          {/* Robot mouth */}
          <path d="M 40 45 Q 50 50 60 45" stroke="#00eeff" strokeWidth="2" fill="none" />
          
          {/* Robot body */}
          <rect x="35" y="55" width="30" height="30" rx="5" fill="none" stroke="#00eeff" strokeWidth="3"/>
          
          {/* Antenna */}
          <line x1="50" y1="15" x2="50" y2="5" stroke="#00eeff" strokeWidth="2" />
          <circle cx="50" cy="3" r="2" fill="#00eeff" />
        </svg>
      </div>
    </button>
  );
};

export default FloatingButton;