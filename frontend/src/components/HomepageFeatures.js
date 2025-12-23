import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'Physical AI Focus',
    description: (
      <>
        Learn about the intersection of artificial intelligence and the physical world,
        with practical examples and simulations.
      </>
    ),
  },
  {
    title: 'Interactive Learning',
    description: (
      <>
        Engage with interactive elements, AI assistants, and real-world robot examples
        to enhance your learning experience.
      </>
    ),
  },
  {
    title: 'Modern Robotics',
    description: (
      <>
        Explore cutting-edge robotics technologies including ROS 2, NVIDIA Isaac,
        and Vision-Language-Action models.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}