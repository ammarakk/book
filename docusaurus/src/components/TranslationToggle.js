import React, { useState, useContext } from 'react';
import { AuthContext } from '../contexts/AuthContext';

const TranslationToggle = ({ chapterId }) => {
  const { isAuthenticated, user } = useContext(AuthContext);
  const [isLoading, setIsLoading] = useState(false);
  const [isTranslated, setIsTranslated] = useState(false);

  // Only show the button if the user is authenticated
  if (!isAuthenticated) {
    return null;
  }

  const handleTranslateClick = async () => {
    setIsLoading(true);

    try {
      // In a real implementation, this would call the backend API
      // to request translation for the current chapter
      console.log(`Requesting translation for chapter: ${chapterId} for user: ${user?.email}`);

      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000));

      // Update state to indicate translation is active
      setIsTranslated(true);
    } catch (error) {
      console.error('Error translating content:', error);
    } finally {
      setIsLoading(false);
    }
  };

  // Disable the button if translation is already active
  const isDisabled = isTranslated || isLoading;

  return (
    <button
      onClick={handleTranslateClick}
      disabled={isDisabled}
      className={`translate-toggle ${isDisabled ? 'disabled' : ''}`}
      style={{
        backgroundColor: isDisabled ? '#cccccc' : '#4CAF50',
        color: 'white',
        padding: '10px 20px',
        border: 'none',
        borderRadius: '4px',
        cursor: isDisabled ? 'not-allowed' : 'pointer',
        fontSize: '16px',
        margin: '10px 0'
      }}
    >
      {isLoading ? 'Translating...' :
       isTranslated ? 'Content Translated' : 'Translate to Urdu'}
    </button>
  );
};

export default TranslationToggle;