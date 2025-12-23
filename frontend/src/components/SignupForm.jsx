// frontend/src/components/SignupForm.jsx
import React, { useState } from 'react';
import apiService from '../services/api';
import { useNavigate } from '@docusaurus/router';

const SignupForm = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    name: '',
    software_background: '',
    hardware_background: '',
    ai_experience: ''
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await apiService.signup(formData);
      
      // Store the token in localStorage
      localStorage.setItem('authToken', response.token);
      
      // Redirect to a success page or the home page
      navigate('/');
    } catch (err) {
      setError(err.message || 'An error occurred during signup');
      console.error('Signup error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      maxWidth: '500px',
      margin: '2rem auto',
      padding: '2rem',
      border: '1px solid #ddd',
      borderRadius: '8px',
      backgroundColor: '#f9f9f9'
    }}>
      <h2>Sign Up</h2>
      
      {error && (
        <div style={{
          color: 'red',
          marginBottom: '1rem',
          padding: '0.5rem',
          backgroundColor: '#ffe6e6',
          borderRadius: '4px'
        }}>
          {error}
        </div>
      )}
      
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '1rem' }}>
          <label htmlFor="name" style={{ display: 'block', marginBottom: '0.5rem' }}>
            Full Name *
          </label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            style={{
              width: '100%',
              padding: '0.5rem',
              border: '1px solid #ccc',
              borderRadius: '4px'
            }}
          />
        </div>
        
        <div style={{ marginBottom: '1rem' }}>
          <label htmlFor="email" style={{ display: 'block', marginBottom: '0.5rem' }}>
            Email *
          </label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            style={{
              width: '100%',
              padding: '0.5rem',
              border: '1px solid #ccc',
              borderRadius: '4px'
            }}
          />
        </div>
        
        <div style={{ marginBottom: '1rem' }}>
          <label htmlFor="password" style={{ display: 'block', marginBottom: '0.5rem' }}>
            Password *
          </label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            style={{
              width: '100%',
              padding: '0.5rem',
              border: '1px solid #ccc',
              borderRadius: '4px'
            }}
          />
        </div>
        
        <div style={{ marginBottom: '1rem' }}>
          <label htmlFor="software_background" style={{ display: 'block', marginBottom: '0.5rem' }}>
            Software Background
          </label>
          <select
            id="software_background"
            name="software_background"
            value={formData.software_background}
            onChange={handleChange}
            style={{
              width: '100%',
              padding: '0.5rem',
              border: '1px solid #ccc',
              borderRadius: '4px'
            }}
          >
            <option value="">Select your software background</option>
            <option value="none">None</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
          </select>
        </div>
        
        <div style={{ marginBottom: '1rem' }}>
          <label htmlFor="hardware_background" style={{ display: 'block', marginBottom: '0.5rem' }}>
            Hardware Background
          </label>
          <select
            id="hardware_background"
            name="hardware_background"
            value={formData.hardware_background}
            onChange={handleChange}
            style={{
              width: '100%',
              padding: '0.5rem',
              border: '1px solid #ccc',
              borderRadius: '4px'
            }}
          >
            <option value="">Select your hardware background</option>
            <option value="none">None</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
          </select>
        </div>
        
        <div style={{ marginBottom: '1rem' }}>
          <label htmlFor="ai_experience" style={{ display: 'block', marginBottom: '0.5rem' }}>
            AI Experience
          </label>
          <select
            id="ai_experience"
            name="ai_experience"
            value={formData.ai_experience}
            onChange={handleChange}
            style={{
              width: '100%',
              padding: '0.5rem',
              border: '1px solid #ccc',
              borderRadius: '4px'
            }}
          >
            <option value="">Select your AI experience</option>
            <option value="none">None</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
          </select>
        </div>
        
        <button
          type="submit"
          disabled={loading}
          style={{
            width: '100%',
            padding: '0.75rem',
            backgroundColor: loading ? '#ccc' : '#28a745',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: loading ? 'not-allowed' : 'pointer',
            fontSize: '1rem'
          }}
        >
          {loading ? 'Signing up...' : 'Sign Up'}
        </button>
      </form>
      
      <div style={{ marginTop: '1rem', textAlign: 'center' }}>
        Already have an account? <a href="/signin">Sign in</a>
      </div>
    </div>
  );
};

export default SignupForm;