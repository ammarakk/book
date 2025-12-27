import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProfileDisplay = () => {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          setError('No authentication token found');
          setLoading(false);
          return;
        }

        const response = await axios.get('/api/auth/profile', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });

        setProfile(response.data);
      } catch (err) {
        setError(err.response?.data?.detail || 'Failed to fetch profile');
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, []);

  if (loading) {
    return <div>Loading profile...</div>;
  }

  if (error) {
    return <div className="error-message">{error}</div>;
  }

  if (!profile) {
    return <div>No profile data available</div>;
  }

  return (
    <div className="profile-display">
      <h3>User Profile</h3>
      <div className="profile-info">
        <p><strong>Email:</strong> {profile.email}</p>
        <p><strong>Software Background:</strong> {profile.profile.software_background}</p>
        <p><strong>Hardware Background:</strong> {profile.profile.hardware_background}</p>
      </div>
    </div>
  );
};

export default ProfileDisplay;