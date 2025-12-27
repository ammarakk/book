import React from 'react';
import clsx from 'clsx';
import styles from './PlaceholderFeatures.module.css';

type PlaceholderFeaturesProps = {
  features?: string[];
};

const PlaceholderFeatures = ({ features = [] }: PlaceholderFeaturesProps): JSX.Element => {
  return (
    <div className={styles.placeholderContainer}>
      {features.includes('chatbot') && (
        <div className={clsx('card', styles.featureCard)}>
          <div className={styles.featureHeader}>
            <h3>🤖 AI Chatbot</h3>
            <p className={styles.featureTag}>Coming in Phase 2</p>
          </div>
          <p>Interactive chatbot to answer questions about the book content using advanced AI.</p>
          <div className={styles.comingSoonBadge}>Coming Soon</div>
        </div>
      )}
      
      {features.includes('personalization') && (
        <div className={clsx('card', styles.featureCard)}>
          <div className={styles.featureHeader}>
            <h3>👤 Content Personalization</h3>
            <p className={styles.featureTag}>Coming in Phase 4</p>
          </div>
          <p>Adaptive content that adjusts to your background and learning preferences.</p>
          <div className={styles.comingSoonBadge}>Coming Soon</div>
        </div>
      )}
      
      {features.includes('translation') && (
        <div className={clsx('card', styles.featureCard)}>
          <div className={styles.featureHeader}>
            <h3>🌐 Translation System</h3>
            <p className={styles.featureTag}>Coming in Phase 5</p>
          </div>
          <p>Multi-language support to make the content accessible to a global audience.</p>
          <div className={styles.comingSoonBadge}>Coming Soon</div>
        </div>
      )}
    </div>
  );
};

export default PlaceholderFeatures;