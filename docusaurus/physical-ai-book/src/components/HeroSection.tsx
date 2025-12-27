import React from 'react';
import clsx from 'clsx';
import styles from './HeroSection.module.css';

type HeroSectionProps = {
  title: string;
  subtitle: string;
  imageUrl?: string;
  tagline?: string;
};

const HeroSection = ({ title, subtitle, imageUrl, tagline }: HeroSectionProps): JSX.Element => {
  return (
    <div className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <div className="row">
          <div className={clsx('col col--5')}>
            <h1 className={clsx('hero__title', styles.neonGlow)}>{title}</h1>
            <p className="hero__subtitle">{subtitle}</p>
            {tagline && <p className="hero__tagline">{tagline}</p>}
          </div>
          <div className={clsx('col col--5 col--offset-1')}>
            {imageUrl ? (
              <div className={styles.heroImgContainer}>
                <img 
                  className={styles.heroImg} 
                  src={imageUrl} 
                  alt={title} 
                />
              </div>
            ) : (
              <div className={styles.heroPlaceholder}>
                <div className={styles.robotIcon}>🤖</div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default HeroSection;