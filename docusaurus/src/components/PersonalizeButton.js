import React, { useState, useContext } from 'react';
import { AuthContext } from '../contexts/AuthContext';

const PersonalizeButton = ({ chapterId }) => {
  const { isAuthenticated, user } = useContext(AuthContext);
  const [isLoading, setIsLoading] = useState(false);
  const [isPersonalized, setIsPersonalized] = useState(false);

  // Only show the button if the user is authenticated
  if (!isAuthenticated) {
    return null;
  }

  const handlePersonalizeClick = async () => {
    setIsLoading(true);

    try {
      // In a real implementation, this would call the backend API
      // to request personalized content for the chapter
      console.log(`Requesting personalization for chapter: ${chapterId} for user: ${user?.email}`);

      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000));

      // Update state to indicate personalization is active
      setIsPersonalized(true);
    } catch (error) {
      console.error('Error personalizing content:', error);
    } finally {
      setIsLoading(false);
    }
  };

  // Disable the button if personalization is already active
  const isDisabled = isPersonalized || isLoading;

  return (
    <button
      onClick={handlePersonalizeClick}
      disabled={isDisabled}
      className={`personalize-button ${isDisabled ? 'disabled' : ''}`}
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
      {isLoading ? 'Personalizing...' :
       isPersonalized ? 'Content Personalized' : 'Personalize Content'}
    </button>
  );
};

export default PersonalizeButton;