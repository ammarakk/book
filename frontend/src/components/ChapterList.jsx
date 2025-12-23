// frontend/src/components/ChapterList.jsx
import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from '@docusaurus/router';
import apiService from '../services/api';

const ChapterList = () => {
  const [chapters, setChapters] = useState([]);
  const [module, setModule] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const { moduleId } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchChapters = async () => {
      try {
        // First get the module details
        // Note: We don't have a direct API for getting module by ID, 
        // so we'll just use the moduleId from the URL
        
        // Then get chapters for this module
        const data = await apiService.getChaptersForModule(moduleId);
        setChapters(data);
      } catch (err) {
        setError('Failed to load chapters');
        console.error('Error fetching chapters:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchChapters();
  }, [moduleId]);

  if (loading) {
    return <div>Loading chapters...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="chapter-list">
      <h2>Chapters in Module {moduleId}</h2>
      <div className="chapters-container">
        {chapters.map((chapter) => (
          <div 
            key={chapter.id} 
            className="chapter-card"
            onClick={() => navigate(`/chapters/${chapter.id}`)}
            style={{
              border: '1px solid #ccc',
              padding: '1rem',
              margin: '0.5rem',
              borderRadius: '4px',
              cursor: 'pointer',
              backgroundColor: '#f9f9f9'
            }}
          >
            <h3>{chapter.title}</h3>
            <div className="chapter-info">
              <span>Chapter {chapter.chapter_number}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ChapterList;