import React, { useState, useEffect } from 'react';

const PersonalizedContent = ({ chapterId, sessionId }) => {
  const [personalizedContent, setPersonalizedContent] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [expandedSections, setExpandedSections] = useState({});

  useEffect(() => {
    if (sessionId) {
      fetchPersonalizedContent();
    }
  }, [sessionId]);

  const fetchPersonalizedContent = async () => {
    setIsLoading(true);
    setError(null);

    try {
      // In a real implementation, this would fetch from the backend API
      // using the session ID to get the personalized content
      console.log(`Fetching personalized content for session: ${sessionId}`);

      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 500));

      // Mock personalized content for demonstration
      const mockContent = [
        {
          content_id: "1",
          original_content_id: "original-1",
          personalized_text: "As a beginner, think of ROS as a toolkit that helps different parts of your robot communicate with each other...",
          personalization_type: "explanation",
          user_background_level: "beginner"
        },
        {
          content_id: "2",
          original_content_id: "original-2",
          personalized_text: "For beginners, this code is setting up a basic publisher that sends messages to other parts of your robot...",
          personalization_type: "explanation",
          user_background_level: "beginner"
        }
      ];

      setPersonalizedContent(mockContent);
    } catch (err) {
      setError('Failed to load personalized content');
      console.error('Error fetching personalized content:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const toggleSection = (contentId) => {
    setExpandedSections(prev => ({
      ...prev,
      [contentId]: !prev[contentId]
    }));
  };

  if (isLoading) {
    return <div className="personalized-content-loading">Loading personalized content...</div>;
  }

  if (error) {
    return <div className="personalized-content-error">Error: {error}</div>;
  }

  return (
    <div className="personalized-content-container">
      {personalizedContent.map((item) => (
        <div
          key={item.content_id}
          className={`expandable-section personalized-${item.personalization_type} ${expandedSections[item.content_id] ? 'active' : ''}`}
          onClick={() => toggleSection(item.content_id)}
        >
          <div className="expandable-header">
            <span>Personalized Content: {item.personalization_type} for {item.user_background_level} level</span>
            <span>{expandedSections[item.content_id] ? '▲' : '▼'}</span>
          </div>
          <div className="expandable-content">
            <div
              className="personalized-content-item"
              style={{
                backgroundColor: '#f0f8ff',
                border: '1px solid #4CAF50',
                borderRadius: '4px',
                padding: '15px',
                margin: '10px 0',
                position: 'relative'
              }}
              onClick={(e) => e.stopPropagation()} // Prevent event bubbling to parent
            >
              <div className="personalization-indicator" style={{
                position: 'absolute',
                top: '-10px',
                left: '10px',
                backgroundColor: '#4CAF50',
                color: 'white',
                padding: '2px 8px',
                borderRadius: '3px',
                fontSize: '12px',
                fontWeight: 'bold'
              }}>
                PERSONALIZED
              </div>
              <div className="personalized-text">
                {item.personalized_text}
              </div>
              <div className="personalization-type" style={{
                fontSize: '12px',
                color: '#666',
                marginTop: '8px',
                fontStyle: 'italic'
              }}>
                Type: {item.personalization_type} | Level: {item.user_background_level}
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default PersonalizedContent;