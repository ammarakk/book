import React, { useState } from 'react';
import FloatingButton from './FloatingButton';
import ChatWindow from './ChatWindow';
import './chat-widget.css';

const ChatWidget = () => {
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [selectedText, setSelectedText] = useState('');

  const toggleChat = () => {
    setIsChatOpen(!isChatOpen);
  };

  const closeChat = () => {
    setIsChatOpen(false);
  };

  // Function to handle sending messages to the backend
  const sendMessageToBackend = async (message, contextMode, selectedText = null) => {
    try {
      // Determine the endpoint based on context mode
      const endpoint = contextMode === 'selection' 
        ? '/api/v1/chat/selection' 
        : '/api/v1/chat';
      
      const requestBody = contextMode === 'selection'
        ? {
            question: message,
            selected_text: selectedText,
          }
        : {
            question: message,
          };
      
      // Add session ID if available
      const sessionId = localStorage.getItem('chat-session-id');
      if (sessionId) {
        requestBody.session_id = sessionId;
      } else {
        // Generate a new session ID if one doesn't exist
        const newSessionId = `session-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
        localStorage.setItem('chat-session-id', newSessionId);
        requestBody.session_id = newSessionId;
      }

      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data.answer_text || data.answer || "Sorry, I couldn't process your request.";
    } catch (error) {
      console.error('Error sending message:', error);
      return "Sorry, I'm having trouble connecting. Please try again.";
    }
  };

  return (
    <>
      <FloatingButton
        onClick={toggleChat}
        isOpen={isChatOpen}
      />
      <ChatWindow
        isOpen={isChatOpen}
        onClose={closeChat}
        onSendMessage={sendMessageToBackend}
        selectedText={selectedText}
      />
    </>
  );
};

// Function to enable text selection functionality
const enableTextSelection = () => {
  // This would be called when the component mounts
  // to enable the "Ask about selected text" functionality
  document.addEventListener('mouseup', function() {
    const selectedText = window.getSelection().toString().trim();
    if (selectedText) {
      // Store the selected text so it can be used when the chat is opened
      // This would require state management that connects to the ChatWidget
      console.log('Selected text:', selectedText);
    }
  });
};

export default ChatWidget;