// frontend/src/components/ModuleList.jsx
import React, { useState, useEffect } from 'react';
import { useNavigate } from '@docusaurus/router';
import apiService from '../services/api';

const ModuleList = () => {
  const [modules, setModules] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const navigate = useNavigate();

  useEffect(() => {
    const fetchModules = async () => {
      try {
        const data = await apiService.getModules();
        setModules(data);
      } catch (err) {
        setError('Failed to load modules');
        console.error('Error fetching modules:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchModules();
  }, []);

  if (loading) {
    return <div>Loading modules...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="module-list">
      <h2>Course Modules</h2>
      <div className="modules-container">
        {modules.map((module) => (
          <div 
            key={module.id} 
            className="module-card"
            onClick={() => navigate(`/modules/${module.id}/chapters`)}
            style={{
              border: '1px solid #ccc',
              padding: '1rem',
              margin: '0.5rem',
              borderRadius: '4px',
              cursor: 'pointer',
              backgroundColor: '#f9f9f9'
            }}
          >
            <h3>{module.title}</h3>
            <p>{module.description}</p>
            <div className="module-info">
              <span>Module {module.module_number}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ModuleList;