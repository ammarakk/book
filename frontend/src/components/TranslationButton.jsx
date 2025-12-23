// frontend/src/components/TranslationButton.jsx
import React from 'react';

const TranslationButton = ({ onTranslate }) => {
  return (
    <button 
      onClick={onTranslate}
      style={{
        padding: '0.5rem 1rem',
        backgroundColor: '#28a745',
        color: 'white',
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer'
      }}
    >
      Translate to Urdu
    </button>
  );
};

export default TranslationButton;