// frontend/src/components/PersonalizationSettings.jsx
import React, { useState, useEffect } from 'react';
import apiService from '../services/api';

const PersonalizationSettings = () => {
  const [settings, setSettings] = useState({
    content_depth: 'intermediate',
    preferred_language: 'en',
    learning_preferences: null
  });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const fetchSettings = async () => {
      try {
        const data = await apiService.getPersonalizationSettings();
        setSettings(data);
      } catch (error) {
        console.error('Error fetching settings:', error);
        // Set default values if there's an error
        setSettings({
          content_depth: 'intermediate',
          preferred_language: 'en',
          learning_preferences: null
        });
      } finally {
        setLoading(false);
      }
    };

    fetchSettings();
  }, []);

  const handleChange = (e) => {
    setSettings({
      ...settings,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSaving(true);
    setMessage('');

    try {
      const response = await apiService.updatePersonalizationSettings(settings);
      setMessage('Settings updated successfully!');
      console.log('Updated settings:', response);
    } catch (error) {
      console.error('Error updating settings:', error);
      setMessage('Failed to update settings. Please try again.');
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return <div>Loading personalization settings...</div>;
  }

  return (
    <div style={{
      maxWidth: '600px',
      margin: '2rem auto',
      padding: '2rem',
      border: '1px solid #ddd',
      borderRadius: '8px',
      backgroundColor: 'white'
    }}>
      <h2>Personalization Settings</h2>
      
      {message && (
        <div style={{
          padding: '0.75rem',
          marginBottom: '1rem',
          borderRadius: '4px',
          backgroundColor: message.includes('successfully') ? '#d4edda' : '#f8d7da',
          color: message.includes('successfully') ? '#155724' : '#721c24',
          border: message.includes('successfully') 
            ? '1px solid #c3e6cb' 
            : '1px solid #f5c6cb'
        }}>
          {message}
        </div>
      )}
      
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '1.5rem' }}>
          <label htmlFor="content_depth" style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 'bold' }}>
            Content Depth
          </label>
          <select
            id="content_depth"
            name="content_depth"
            value={settings.content_depth}
            onChange={handleChange}
            style={{
              width: '100%',
              padding: '0.5rem',
              border: '1px solid #ccc',
              borderRadius: '4px',
              fontSize: '1rem'
            }}
          >
            <option value="beginner">Beginner - Simple explanations with basic examples</option>
            <option value="intermediate">Intermediate - Moderate complexity with practical examples</option>
            <option value="advanced">Advanced - Complex concepts with detailed technical explanations</option>
          </select>
          <p style={{ fontSize: '0.9rem', color: '#666', marginTop: '0.25rem' }}>
            Adjust how technical the content explanations should be
          </p>
        </div>
        
        <div style={{ marginBottom: '1.5rem' }}>
          <label htmlFor="preferred_language" style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 'bold' }}>
            Preferred Language
          </label>
          <select
            id="preferred_language"
            name="preferred_language"
            value={settings.preferred_language}
            onChange={handleChange}
            style={{
              width: '100%',
              padding: '0.5rem',
              border: '1px solid #ccc',
              borderRadius: '4px',
              fontSize: '1rem'
            }}
          >
            <option value="en">English</option>
            <option value="ur">Urdu</option>
          </select>
          <p style={{ fontSize: '0.9rem', color: '#666', marginTop: '0.25rem' }}>
            Language for content display and translations
          </p>
        </div>
        
        <button
          type="submit"
          disabled={saving}
          style={{
            padding: '0.75rem 1.5rem',
            backgroundColor: saving ? '#ccc' : '#007cba',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: saving ? 'not-allowed' : 'pointer',
            fontSize: '1rem'
          }}
        >
          {saving ? 'Saving...' : 'Save Settings'}
        </button>
      </form>
    </div>
  );
};

export default PersonalizationSettings;