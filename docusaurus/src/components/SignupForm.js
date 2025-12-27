import React, { useState } from 'react';

const SignupForm = ({ onSubmit, loading = false }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [softwareBackground, setSoftwareBackground] = useState('beginner');
  const [hardwareBackground, setHardwareBackground] = useState('none');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Basic validation
    if (!email || !password) {
      setError('Email and password are required');
      return;
    }
    
    if (password.length < 8) {
      setError('Password must be at least 8 characters');
      return;
    }
    
    setError('');
    
    // Call the parent's submit handler
    onSubmit({
      email,
      password,
      softwareBackground,
      hardwareBackground
    });
  };

  return (
    <div className="signup-form-container">
      <form onSubmit={handleSubmit} className="signup-form">
        {error && <div className="error-message">{error}</div>}
        
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            disabled={loading}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            minLength="8"
            disabled={loading}
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="softwareBackground">Software Background:</label>
          <select
            id="softwareBackground"
            value={softwareBackground}
            onChange={(e) => setSoftwareBackground(e.target.value)}
            disabled={loading}
          >
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
          </select>
        </div>
        
        <div className="form-group">
          <label htmlFor="hardwareBackground">Hardware Background:</label>
          <select
            id="hardwareBackground"
            value={hardwareBackground}
            onChange={(e) => setHardwareBackground(e.target.value)}
            disabled={loading}
          >
            <option value="none">None</option>
            <option value="basic_electronics">Basic Electronics</option>
            <option value="robotics_experience">Robotics Experience</option>
          </select>
        </div>
        
        <button type="submit" disabled={loading}>
          {loading ? 'Creating Account...' : 'Sign Up'}
        </button>
      </form>
    </div>
  );
};

export default SignupForm;