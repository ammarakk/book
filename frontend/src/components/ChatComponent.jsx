// frontend/src/components/ChatComponent.jsx
import React, { useState, useRef, useEffect } from 'react';
import apiService from '../services/api';

const ChatComponent = ({ chapterId }) => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async () => {
    if (!inputValue.trim()) return;

    // Add user message to the chat
    const userMessage = {
      id: Date.now(),
      content: inputValue,
      sender: 'user',
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Send message to backend and get response
      const response = await apiService.sendChatMessage(1, {  // Using a placeholder session ID
        content: inputValue,
        context: chapterId ? { chapter_id: chapterId } : {}
      });

      const aiMessage = {
        id: Date.now() + 1,
        content: response.content || "Sorry, I couldn't generate a response.",
        sender: 'assistant',
        timestamp: new Date()
      };

      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      
      const errorMessage = {
        id: Date.now() + 1,
        content: "Sorry, there was an error processing your request.",
        sender: 'assistant',
        timestamp: new Date()
      };
      
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className="chat-component" style={{
      border: '1px solid #ddd',
      borderRadius: '8px',
      padding: '1rem',
      backgroundColor: '#f9f9f9',
      display: 'flex',
      flexDirection: 'column',
      height: '500px'
    }}>
      <div className="chat-header" style={{
        fontWeight: 'bold',
        marginBottom: '1rem',
        borderBottom: '1px solid #ddd',
        paddingBottom: '0.5rem'
      }}>
        AI Assistant
      </div>
      
      <div className="chat-messages" style={{
        flex: 1,
        overflowY: 'auto',
        marginBottom: '1rem',
        padding: '0.5rem',
        backgroundColor: 'white',
        borderRadius: '4px'
      }}>
        {messages.map((message) => (
          <div 
            key={message.id}
            className={`message ${message.sender}`}
            style={{
              textAlign: message.sender === 'user' ? 'right' : 'left',
              marginBottom: '0.5rem'
            }}
          >
            <div style={{
              display: 'inline-block',
              padding: '0.5rem 1rem',
              borderRadius: '18px',
              backgroundColor: message.sender === 'user' ? '#007cba' : '#e5e5ea',
              color: message.sender === 'user' ? 'white' : 'black'
            }}>
              {message.content}
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="message assistant" style={{ textAlign: 'left', marginBottom: '0.5rem' }}>
            <div style={{
              display: 'inline-block',
              padding: '0.5rem 1rem',
              borderRadius: '18px',
              backgroundColor: '#e5e5ea',
              color: 'black'
            }}>
              Thinking...
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      
      <div className="chat-input-area" style={{
        display: 'flex',
        gap: '0.5rem'
      }}>
        <textarea
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Ask a question about this content..."
          style={{
            flex: 1,
            padding: '0.5rem',
            borderRadius: '4px',
            border: '1px solid #ddd'
          }}
          rows={2}
        />
        <button
          onClick={handleSendMessage}
          disabled={isLoading || !inputValue.trim()}
          style={{
            padding: '0.5rem 1rem',
            backgroundColor: isLoading ? '#ccc' : '#007cba',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: isLoading ? 'not-allowed' : 'pointer'
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatComponent;