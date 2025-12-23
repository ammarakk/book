// frontend/src/hooks/useAuth.js
import { useState, useEffect } from 'react';

const useAuth = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [authToken, setAuthToken] = useState(null);

  // Check for token on initial load
  useEffect(() => {
    const token = localStorage.getItem('authToken');
    if (token) {
      setAuthToken(token);
      // In a real implementation, you would decode the token or make a request
      // to validate it and get user details
      // For now, we'll just set a placeholder user object
      setUser({ id: 1, email: 'user@example.com', name: 'User' });
    }
    setLoading(false);
  }, []);

  const login = (token, userData) => {
    localStorage.setItem('authToken', token);
    setAuthToken(token);
    setUser(userData);
  };

  const logout = () => {
    localStorage.removeItem('authToken');
    setAuthToken(null);
    setUser(null);
  };

  const isAuthenticated = !!authToken;

  return {
    user,
    loading,
    authToken,
    isAuthenticated,
    login,
    logout
  };
};

export default useAuth;