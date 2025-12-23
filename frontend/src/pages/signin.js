// frontend/src/pages/signin.js
import React from 'react';
import Layout from '@theme/Layout';
import SigninForm from '../components/SigninForm';

export default function SigninPage() {
  return (
    <Layout title="Sign In" description="Sign in to your account for the Physical AI & Humanoid Robotics Book">
      <div style={{ 
        display: 'flex', 
        justifyContent: 'center', 
        alignItems: 'center', 
        minHeight: '80vh',
        padding: '2rem 0'
      }}>
        <SigninForm />
      </div>
    </Layout>
  );
}