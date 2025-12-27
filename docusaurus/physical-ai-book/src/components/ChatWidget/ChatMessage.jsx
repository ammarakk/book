import React from 'react';
import './chat-widget.css';

const ChatMessage = ({ message, sender, timestamp, isLoading = false }) => {
  const formatTimestamp = (date) => {
    if (!date) return '';
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className={`message-container ${sender}`}>
      <div className={`message-bubble ${sender}`}>
        {isLoading ? (
          <div className="loading-indicator">
            <div className="dot"></div>
            <div className="dot"></div>
            <div className="dot"></div>
          </div>
        ) : (
          <p>{message}</p>
        )}
        {timestamp && !isLoading && (
          <div className="message-timestamp">
            {formatTimestamp(timestamp)}
          </div>
        )}
      </div>
      {sender === 'bot' && !isLoading && (
        <div className="bot-icon">
          <svg 
            xmlns="http://www.w3.org/2000/svg" 
            viewBox="0 0 24 24" 
            width="20" 
            height="20"
            fill="currentColor"
          >
            <path d="M12 2C13.1 2 14 2.9 14 4C14 5.1 13.1 6 12 6C10.9 6 10 5.1 10 4C10 2.9 10.9 2 12 2ZM21 9V7L15 1H5C3.89 1 3 1.89 3 3V7C1.9 7 1 7.9 1 9V10.33C2.16 11.3 3.62 12.03 5.22 12.42C5.5 13.86 5.92 15.24 6.49 16.54C6.25 16.81 6.02 17.1 5.81 17.41C4.6 16.69 3.58 15.7 2.8 14.5C2.09 15.73 1.62 17.14 1.43 18.65C1.4 18.85 1.52 19.05 1.72 19.08C1.87 19.11 2.02 19.05 2.11 18.93C3.33 17.17 5.06 15.82 7.05 15.08C7.39 15.52 7.77 15.93 8.19 16.3C8.13 16.5 8.09 16.71 8.09 16.92C8.09 18.03 8.98 18.92 10.09 18.92C11.2 18.92 12.09 18.03 12.09 16.92C12.09 16.71 12.05 16.5 11.99 16.3C12.41 15.93 12.79 15.52 13.13 15.08C15.12 15.82 16.85 17.17 18.07 18.93C18.16 19.05 18.31 19.11 18.46 19.08C18.66 19.05 18.78 18.85 18.75 18.65C18.56 17.14 18.09 15.73 17.38 14.5C16.6 15.7 15.58 16.69 14.37 17.41C14.16 17.1 13.93 16.81 13.69 16.54C14.26 15.24 14.68 13.86 14.96 12.42C16.56 12.03 18.02 11.3 19.18 10.33V9H21Z" />
          </svg>
        </div>
      )}
    </div>
  );
};

export default ChatMessage;