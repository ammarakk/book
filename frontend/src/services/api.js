// frontend/src/services/api.js
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

class ApiService {
  constructor() {
    this.baseURL = API_BASE_URL;
    this.defaultHeaders = {
      'Content-Type': 'application/json',
    };
  }

  // Helper method to get auth token from localStorage
  getAuthToken() {
    return localStorage.getItem('authToken');
  }

  // Helper method to include auth token in headers
  getAuthHeaders() {
    const token = this.getAuthToken();
    return {
      ...this.defaultHeaders,
      ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    };
  }

  // Generic request method
  async request(endpoint, options = {}) {
    const url = `${this.baseURL}/api${endpoint}`;
    const config = {
      headers: {
        ...this.defaultHeaders,
        ...options.headers,
      },
      ...options,
    };

    // Add auth token if not already present and we have one
    if (!config.headers.Authorization && this.getAuthToken()) {
      config.headers = this.getAuthHeaders();
    }

    try {
      const response = await fetch(url, config);
      
      // If response is not ok, throw an error with the response
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
      }
      
      // Handle empty responses
      if (response.status === 204) {
        return null;
      }
      
      return await response.json();
    } catch (error) {
      console.error(`API request failed: ${endpoint}`, error);
      throw error;
    }
  }

  // Auth methods
  async signup(userData) {
    return this.request('/auth/signup', {
      method: 'POST',
      body: JSON.stringify(userData),
    });
  }

  async signin(credentials) {
    return this.request('/auth/signin', {
      method: 'POST',
      body: JSON.stringify(credentials),
    });
  }

  async signout() {
    // Remove token from localStorage
    localStorage.removeItem('authToken');
    return this.request('/auth/signout', {
      method: 'POST',
    });
  }

  // Content methods
  async getModules() {
    return this.request('/content/modules');
  }

  async getChaptersForModule(moduleId) {
    return this.request(`/content/modules/${moduleId}/chapters`);
  }

  async getChapter(chapterId) {
    return this.request(`/content/chapters/${chapterId}`);
  }

  // User methods
  async getPersonalizationSettings() {
    return this.request('/users/me/personalization');
  }

  async updatePersonalizationSettings(settings) {
    return this.request('/users/me/personalization', {
      method: 'PUT',
      body: JSON.stringify(settings),
    });
  }

  // Chat methods
  async createChatSession(sessionData) {
    return this.request('/chat/', {
      method: 'POST',
      body: JSON.stringify(sessionData),
    });
  }

  async sendChatMessage(sessionId, messageData) {
    return this.request(`/chat/${sessionId}/messages`, {
      method: 'POST',
      body: JSON.stringify(messageData),
    });
  }

  async getUserChatSessions() {
    return this.request('/chat/');
  }

  async getChatMessages(sessionId) {
    return this.request(`/chat/${sessionId}/messages`);
  }

  // Translation method
  async translateContent(translationData) {
    return this.request('/translate/', {
      method: 'POST',
      body: JSON.stringify(translationData),
    });
  }
}

export default new ApiService();