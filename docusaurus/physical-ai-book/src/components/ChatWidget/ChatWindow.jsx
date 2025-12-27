import React, { useState, useRef, useEffect } from 'react';
import ChatMessage from './ChatMessage';
import ChatInput from './ChatInput';  // Fixed: was ChatInput, should be ChatInput
import './chat-widget.css';

const ChatWindow = ({ isOpen, onClose, onSendMessage }) => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Sample initial message
  useEffect(() => {
    if (isOpen && messages.length === 0) {
      setMessages([
        {
          id: 1,
          text: "Hello! I'm your AI assistant for the Physical AI & Humanoid Robotics book. Ask me anything about the content!",
          sender: 'bot',
          timestamp: new Date()
        }
      ]);
    }
  }, [isOpen]);

  // Scroll to bottom of messages
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const handleSend = async (text, contextMode = 'global', selectedText = null) => {
    if (!text.trim()) return;

    // Add user message
    const userMessage = {
      id: Date.now(),
      text: text,
      sender: 'user',
      timestamp: new Date(),
      contextMode: contextMode,
      selectedText: selectedText
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    try {
      // In a real implementation, this would call the backend API
      // For now, we'll simulate a response
      const response = await simulateApiCall(text, contextMode, selectedText);

      const botMessage = {
        id: Date.now() + 1,
        text: response,
        sender: 'bot',
        timestamp: new Date()
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = {
        id: Date.now() + 1,
        text: "Sorry, I couldn't process your request. Please try again.",
        sender: 'bot',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  // Simulate API call to backend
  const simulateApiCall = (question, contextMode, selectedText) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        // This is a placeholder response - in reality, this would come from the backend
        const responses = [
          "Based on the Physical AI & Humanoid Robotics book, this concept relates to the robotic nervous system described in Module 1.",
          "According to the book's Module 2 on Digital Twins, this topic covers simulation environments and physics engines.",
          "The AI-Robot Brain section in Module 3 explains this concept in detail, particularly regarding perception and planning algorithms.",
          "For Vision-Language-Action systems, please refer to Module 4 which covers multimodal AI and computer vision techniques.",
          "The Capstone Module 5 integrates all previous concepts into a complete humanoid robot system."
        ];

        // Select a random response for simulation
        const randomResponse = responses[Math.floor(Math.random() * responses.length)];
        resolve(randomResponse);
      }, 1000); // Simulate network delay
    });
  };

  if (!isOpen) return null;

  return (
    <div className="chat-window">
      <div className="chat-header">
        <h3>AI Assistant</h3>
        <button className="close-button" onClick={onClose} aria-label="Close chat">
          ×
        </button>
      </div>
      
      <div className="chat-messages">
        {messages.map((message) => (
          <ChatMessage 
            key={message.id} 
            message={message.text} 
            sender={message.sender} 
            timestamp={message.timestamp} 
          />
        ))}
        {isLoading && (
          <ChatMessage
            message="Thinking..."
            sender="bot"
            isLoading={true}
          />
        )}
        <div ref={messagesEndRef} />
      </div>
      
      <div className="chat-input-container">
        <ChatInput onSend={handleSend} />
      </div>
    </div>
  );
};

export default ChatWindow;