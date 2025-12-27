/**
 * Service to interact with the personalization API
 */

class PersonalizationService {
  constructor(apiBaseUrl = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000') {
    this.apiBaseUrl = apiBaseUrl;
  }

  /**
   * Request personalized content for a specific chapter based on user profile
   */
  async requestPersonalization(chapterId, userBackground) {
    try {
      const response = await fetch(`${this.apiBaseUrl}/api/personalize/request`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.getAuthToken()}`
        },
        body: JSON.stringify({
          chapter_id: chapterId,
          user_background: userBackground
        })
      });

      if (!response.ok) {
        throw new Error(`Failed to request personalization: ${response.status} ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error requesting personalization:', error);
      throw error;
    }
  }

  /**
   * Get personalized content for an existing session
   */
  async getPersonalizationSession(sessionId) {
    try {
      const response = await fetch(`${this.apiBaseUrl}/api/personalize/session/${sessionId}`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${this.getAuthToken()}`
        }
      });

      if (!response.ok) {
        throw new Error(`Failed to get personalization session: ${response.status} ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error getting personalization session:', error);
      throw error;
    }
  }

  /**
   * Get the authentication token from local storage or other storage mechanism
   */
  getAuthToken() {
    // In a real implementation, this would retrieve the JWT token
    // from wherever it's stored (e.g., localStorage, secure cookie)
    return localStorage.getItem('authToken') || sessionStorage.getItem('authToken');
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

export default new PersonalizationService();