// frontend/src/pages/signup.js
import React from 'react';
import Layout from '@theme/Layout';
import SignupForm from '../components/SignupForm';

export default function SignupPage() {
  return (
    <Layout title="Sign Up" description="Create an account for the Physical AI & Humanoid Robotics Book">
      <div style={{ 
        display: 'flex', 
        justifyContent: 'center', 
        alignItems: 'center', 
        minHeight: '80vh',
        padding: '2rem 0'
      }}>
        <SignupForm />
      </div>
    </Layout>
  );
}