// frontend/src/components/HeroSection.jsx
import React from 'react';
import Link from '@docusaurus/Link';

const HeroSection = () => {
  return (
    <section 
      style={{
        padding: '4rem 2rem',
        textAlign: 'center',
        backgroundColor: '#f8f9fa',
        backgroundImage: 'linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%)',
      }}
    >
      <div className="container">
        <h1 style={{ 
          fontSize: '3rem', 
          marginBottom: '1rem',
          color: '#2c3e50',
          textShadow: '1px 1px 2px rgba(0,0,0,0.1)'
        }}>
          Physical AI & Humanoid Robotics
        </h1>
        
        <p style={{ 
          fontSize: '1.5rem', 
          marginBottom: '2rem',
          color: '#34495e',
          maxWidth: '800px',
          margin: '0 auto'
        }}>
          Explore the intersection of artificial intelligence and the physical world. 
          Learn to understand, simulate, and design humanoid robots using modern 
          robotics, simulation, and AI systems.
        </p>
        
        <div style={{ marginTop: '2rem' }}>
          <Link
            to="/docs/intro"
            style={{
              display: 'inline-block',
              padding: '1rem 2rem',
              backgroundColor: '#3498db',
              color: 'white',
              textDecoration: 'none',
              borderRadius: '8px',
              fontSize: '1.2rem',
              fontWeight: 'bold',
              boxShadow: '0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08)',
              transition: 'transform 0.2s, box-shadow 0.2s',
              marginRight: '1rem'
            }}
            onMouseEnter={(e) => {
              e.target.style.transform = 'translateY(-2px)';
              e.target.style.boxShadow = '0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08)';
            }}
            onMouseLeave={(e) => {
              e.target.style.transform = 'translateY(0)';
              e.target.style.boxShadow = '0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08)';
            }}
          >
            Start Learning
          </Link>
          
          <Link
            to="/docs/module1/chapter1"
            style={{
              display: 'inline-block',
              padding: '1rem 2rem',
              backgroundColor: '#2ecc71',
              color: 'white',
              textDecoration: 'none',
              borderRadius: '8px',
              fontSize: '1.2rem',
              fontWeight: 'bold',
              boxShadow: '0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08)',
              transition: 'transform 0.2s, box-shadow 0.2s'
            }}
            onMouseEnter={(e) => {
              e.target.style.transform = 'translateY(-2px)';
              e.target.style.boxShadow = '0 7px 14px rgba(50, 50, 93, 0.1), 0 3px 6px rgba(0, 0, 0, 0.08)';
            }}
            onMouseLeave={(e) => {
              e.target.style.transform = 'translateY(0)';
              e.target.style.boxShadow = '0 4px 6px rgba(50, 50, 93, 0.11), 0 1px 3px rgba(0, 0, 0, 0.08)';
            }}
          >
            Jump to Content
          </Link>
        </div>
        
        <div style={{ 
          marginTop: '3rem', 
          display: 'flex', 
          justifyContent: 'center', 
          flexWrap: 'wrap',
          gap: '2rem'
        }}>
          <div style={{ 
            backgroundColor: 'white', 
            padding: '1.5rem', 
            borderRadius: '8px',
            boxShadow: '0 2px 10px rgba(0,0,0,0.05)',
            minWidth: '200px'
          }}>
            <h3 style={{ color: '#2c3e50', marginBottom: '0.5rem' }}>Interactive Learning</h3>
            <p>Engage with AI assistants and real-world robot examples</p>
          </div>
          
          <div style={{ 
            backgroundColor: 'white', 
            padding: '1.5rem', 
            borderRadius: '8px',
            boxShadow: '0 2px 10px rgba(0,0,0,0.05)',
            minWidth: '200px'
          }}>
            <h3 style={{ color: '#2c3e50', marginBottom: '0.5rem' }}>Personalized Content</h3>
            <p>Adjust content based on your technical background</p>
          </div>
          
          <div style={{ 
            backgroundColor: 'white', 
            padding: '1.5rem', 
            borderRadius: '8px',
            boxShadow: '0 2px 10px rgba(0,0,0,0.05)',
            minWidth: '200px'
          }}>
            <h3 style={{ color: '#2c3e50', marginBottom: '0.5rem' }}>Modern Robotics</h3>
            <p>Learn with ROS 2, NVIDIA Isaac, and VLA models</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;