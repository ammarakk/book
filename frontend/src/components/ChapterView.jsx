// frontend/src/components/ChapterView.jsx
import React, { useState, useEffect } from 'react';
import { useParams } from '@docusaurus/router';
import apiService from '../services/api';
import ChatComponent from './ChatComponent';
import TranslationButton from './TranslationButton';

const ChapterView = () => {
  const [chapter, setChapter] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [translatedContent, setTranslatedContent] = useState(null);
  const [showChat, setShowChat] = useState(false);

  const { chapterId } = useParams();

  useEffect(() => {
    const fetchChapter = async () => {
      try {
        const data = await apiService.getChapter(chapterId);
        setChapter(data);
      } catch (err) {
        setError('Failed to load chapter');
        console.error('Error fetching chapter:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchChapter();
  }, [chapterId]);

  if (loading) {
    return <div>Loading chapter...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  const handleTranslate = async () => {
    if (!chapter) return;

    try {
      const translationResponse = await apiService.translateContent({
        content: chapter.content,
        source_language: 'en',
        target_language: 'ur'
      });
      setTranslatedContent(translationResponse.translated_content);
    } catch (err) {
      console.error('Translation failed:', err);
    }
  };

  const handleTextSelection = () => {
    const selectedText = window.getSelection().toString().trim();
    if (selectedText) {
      // You can do something with the selected text, like showing a context menu
      console.log('Selected text:', selectedText);
    }
  };

  return (
    <div className="chapter-view" onMouseUp={handleTextSelection}>
      <div className="chapter-header">
        <h1>{chapter.title}</h1>
        <div className="chapter-actions">
          <TranslationButton onTranslate={handleTranslate} />
          <button 
            onClick={() => setShowChat(!showChat)}
            style={{
              marginLeft: '1rem',
              padding: '0.5rem 1rem',
              backgroundColor: '#007cba',
              color: 'white',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer'
            }}
          >
            {showChat ? 'Hide Chat' : 'Show Chat'}
          </button>
        </div>
      </div>
      
      <div className="chapter-content">
        {translatedContent ? (
          <div className="translated-content">
            <h3>Urdu Translation:</h3>
            <div dangerouslySetInnerHTML={{ __html: translatedContent }} />
          </div>
        ) : (
          <div dangerouslySetInnerHTML={{ __html: chapter.content }} />
        )}
      </div>
      
      {showChat && (
        <div className="chat-container" style={{ marginTop: '2rem' }}>
          <ChatComponent chapterId={chapter.id} />
        </div>
      )}
    </div>
  );
};

export default ChapterView;