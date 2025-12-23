// frontend/src/components/SigninForm.jsx
import React, { useState } from 'react';
import apiService from '../services/api';
import { useNavigate } from '@docusaurus/router';

const SigninForm = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
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
      const response = await apiService.signin(formData);
      
      // Store the token in localStorage
      localStorage.setItem('authToken', response.token);
      
      // Redirect to a success page or the home page
      navigate('/');
    } catch (err) {
      setError(err.message || 'An error occurred during sign in');
      console.error('Signin error:', err);
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
      <h2>Sign In</h2>
      
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
        
        <button
          type="submit"
          disabled={loading}
          style={{
            width: '100%',
            padding: '0.75rem',
            backgroundColor: loading ? '#ccc' : '#007cba',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: loading ? 'not-allowed' : 'pointer',
            fontSize: '1rem'
          }}
        >
          {loading ? 'Signing in...' : 'Sign In'}
        </button>
      </form>
      
      <div style={{ marginTop: '1rem', textAlign: 'center' }}>
        Don't have an account? <a href="/signup">Sign up</a>
      </div>
    </div>
  );
};

export default SigninForm;