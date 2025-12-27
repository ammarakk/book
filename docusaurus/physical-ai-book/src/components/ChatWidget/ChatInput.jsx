import React, { useState } from 'react';
import './chat-widget.css';

const ChatInput = ({ onSend }) => {
  const [inputText, setInputText] = useState('');
  const [contextMode, setContextMode] = useState('global'); // 'global' or 'selection'
  const [selectedText, setSelectedText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputText.trim()) {
      onSend(inputText, contextMode, selectedText);
      setInputText('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <form className="chat-input-form" onSubmit={handleSubmit}>
      <div className="context-mode-selector">
        <label>
          <input
            type="radio"
            name="contextMode"
            value="global"
            checked={contextMode === 'global'}
            onChange={(e) => setContextMode(e.target.value)}
          />
          Entire Book
        </label>
        <label>
          <input
            type="radio"
            name="contextMode"
            value="selection"
            checked={contextMode === 'selection'}
            onChange={(e) => setContextMode(e.target.value)}
          />
          Selected Text Only
        </label>
      </div>
      
      {contextMode === 'selection' && (
        <div className="selected-text-preview">
          <strong>Selected Text:</strong>
          <p>"{selectedText || 'No text selected. Highlight text in the book and use the "Ask about this" option.'}"</p>
        </div>
      )}
      
      <div className="input-container">
        <textarea
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask a question about the Physical AI & Humanoid Robotics book..."
          rows="3"
          className="chat-textarea"
          aria-label="Type your question"
        />
        <button
          type="submit"
          disabled={!inputText.trim()}
          className="send-button"
          aria-label="Send message"
        >
          <svg 
            xmlns="http://www.w3.org/2000/svg" 
            viewBox="0 0 24 24" 
            width="24" 
            height="24"
            fill="currentColor"
          >
            <path d="M2.01 21L23 12L2.01 3L2 10L17 12L2 14L2.01 21Z" />
          </svg>
        </button>
      </div>
      
      <div className="input-hints">
        <small>Press Enter to send, Shift+Enter for new line</small>
      </div>
    </form>
  );
};

export default ChatInput;