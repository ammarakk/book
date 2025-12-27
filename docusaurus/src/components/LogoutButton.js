import React from 'react';
import { useAuth } from '../components/AuthProvider';

const LogoutButton = () => {
  const { logout, isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return null; // Don't show logout button if not authenticated
  }

  return (
    <button onClick={logout} className="logout-button">
      Logout
    </button>
  );
};

export default LogoutButton;