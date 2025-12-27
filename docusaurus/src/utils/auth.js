// Utility functions for authentication

// Function to get the JWT token from localStorage
export const getToken = () => {
  return localStorage.getItem('token');
};

// Function to set the JWT token in localStorage
export const setToken = (token) => {
  localStorage.setItem('token', token);
};

// Function to remove the JWT token from localStorage
export const removeToken = () => {
  localStorage.removeItem('token');
};

// Function to check if the user is authenticated
export const isAuthenticated = () => {
  const token = getToken();
  return token !== null && token !== undefined;
};

// Function to validate token format (basic check)
export const isValidToken = (token) => {
  if (!token) return false;
  
  // Basic JWT format check: 3 parts separated by dots
  const parts = token.split('.');
  return parts.length === 3;
};

// Function to get user info from token (decode without verification)
export const getUserFromToken = (token) => {
  if (!token || !isValidToken(token)) {
    return null;
  }

  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split('')
        .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    );

    return JSON.parse(jsonPayload);
  } catch (error) {
    console.error('Error decoding token:', error);
    return null;
  }
};