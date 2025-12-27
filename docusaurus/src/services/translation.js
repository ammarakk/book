/**
 * Service to interact with the translation API
 */

class TranslationService {
  constructor(apiBaseUrl = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000') {
    this.apiBaseUrl = apiBaseUrl;
  }

  /**
   * Request translation for a specific chapter
   */
  async requestTranslation(chapterId, targetLanguage = 'ur') {
    try {
      const token = localStorage.getItem('authToken'); // Get auth token from storage
      
      const response = await fetch(`${this.apiBaseUrl}/api/auth/translate/request`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`  // Include auth token
        },
        body: JSON.stringify({
          chapter_id: chapterId,
          target_language: target_language
        })
      });

      if (!response.ok) {
        throw new Error(`Failed to request translation: ${response.status} ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error requesting translation:', error);
      throw error;
    }
  }

  /**
   * Get translated content for an existing session
   */
  async getTranslationSession(sessionId) {
    try {
      const token = localStorage.getItem('authToken'); // Get auth token from storage
      
      const response = await fetch(`${this.apiBaseUrl}/api/auth/translate/session/${sessionId}`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${token}`  // Include auth token
        }
      });

      if (!response.ok) {
        throw new Error(`Failed to get translation session: ${response.status} ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error getting translation session:', error);
      throw error;
    }
  }

  /**
   * Get user profile from local storage or other storage mechanism
   */
  getUserProfile() {
    // In a real implementation, this would retrieve the user profile
    // from wherever it's stored
    const profileStr = localStorage.getItem('userProfile') || sessionStorage.getItem('userProfile');
    return profileStr ? JSON.parse(profileStr) : null;
  }
}

export default new TranslationService();