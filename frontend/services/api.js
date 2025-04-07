import axios from 'axios';

// Create axios instance with base configuration
const api = axios.create({
    baseURL: 'http://localhost:8000/api',  // Adjust this URL based on your Django backend
    headers: {
        'Content-Type': 'application/json',
    }
});

// Password check endpoint
export const checkPassword = (password) => {
    return api.post('/check-password/', { password });
};

export default api;

