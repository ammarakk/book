import React, { useState, useEffect } from 'react';

const TranslatedContent = ({ chapterId, sessionId }) => {
  const [translatedContent, setTranslatedContent] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (sessionId) {
      fetchTranslatedContent();
    }
  }, [sessionId]);

  const fetchTranslatedContent = async () => {
    setIsLoading(true);
    setError(null);

    try {
      // In a real implementation, this would fetch from the backend API
      // using the session ID to get the translated content
      console.log(`Fetching translated content for session: ${sessionId}`);
      
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 500));
      
      // Mock translated content for demonstration
      const mockContent = [
        {
          content_id: "1",
          original_content_id: "original-1",
          translated_text: "روبوٹکس میں، روبوٹ آپریٹنگ سسٹم (ROS) مختلف حصوں کو ایک دوسرے کے ساتھ بات چیت کرنے کے قابل بناتا ہے...",
          content_type: "explanation",
          preservation_flags: {
            "technical_terms": ["ROS"],
            "code_elements": []
          }
        },
        {
          content_id: "2", 
          original_content_id: "original-2",
          translated_text: "شروع کرنے کے لیے، یہ کوڈ ایک بنیادی شائع کنندہ تشکیل دے رہا ہے جو آپ کے روبوٹ کے دیگر حصوں کو پیغامات بھیجتا ہے...",
          content_type: "explanation",
          preservation_flags: {
            "technical_terms": [],
            "code_elements": []
          }
        }
      ];
      
      setTranslatedContent(mockContent);
    } catch (err) {
      setError('Failed to load translated content');
      console.error('Error fetching translated content:', err);
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return <div className="translated-content-loading">Loading translated content...</div>;
  }

  if (error) {
    return <div className="translated-content-error">Error: {error}</div>;
  }

  return (
    <div className="translated-content-container">
      {translatedContent.map((item) => (
        <div 
          key={item.content_id} 
          className={`translated-content-item translated-${item.content_type}`}
          style={{
            backgroundColor: '#f9f9f9',
            borderLeft: '4px solid #4CAF50',
            padding: '15px',
            margin: '10px 0',
            position: 'relative'
          }}
        >
          <div className="translation-indicator" style={{
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
            TRANSLATED
          </div>
          <div className="translated-text">
            {item.translated_text}
          </div>
          <div className="content-type" style={{
            fontSize: '12px',
            color: '#666',
            marginTop: '8px',
            fontStyle: 'italic'
          }}>
            Type: {item.content_type}
          </div>
        </div>
      ))}
    </div>
  );
};

export default TranslatedContent;