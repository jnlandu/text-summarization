'use client';
import React, { useContext, useState } from 'react';
import axios from 'axios';
import AuthContext from "@/context/AuthContext";
import { useRouter } from "next/navigation";

const SignUp = () => {
  const { login } = useContext(AuthContext);
  const [registerEmail, setRegisterEmail] = useState('');
  const [registerPassword, setRegisterPassword] = useState('');
  const router = useRouter();

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const apiUrl = `${process.env.NEXT_PUBLIC_FASTAPI_API_URL}/auth` // ?? http://localhost:8000/auth`;
      const response = await axios.post(apiUrl, { // Ensure the trailing slash if your backend setup requires it
        username: registerEmail, // Changed 'Email' to 'username' if your backend expects 'username'
        password: registerPassword,
      });
      console.log('Registration successful', response.data);
      login(registerEmail, registerPassword); // Assuming 'login' handles the logic properly
    } catch(error) {
      console.error('Failed to register user:', error.response ? error.response.data : error);
    }
  }
  

  return (
    <div className="container login">
      <h2 className='mt-5'>Sign up </h2>
      <form onSubmit={handleRegister}>
        <div className="mb-3">
          <label htmlFor="registerEmail" className="form-label">Email</label>
          <input
            type="email"
            className="form-control"
            id="registerEmail"
            value={registerEmail}
            onChange={(e) => setRegisterEmail(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="registerPassword" className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            id="registerPassword"
            value={registerPassword}
            onChange={(e) => setRegisterPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">Register</button>
      </form>
      <div className="container mt-3">
        <small>Do you already have an account? </small> 
        <a className="text-primary" href="#"
        onClick={() => router.push('/login')}
        
        >Sign in</a>
      </div>
    </div>
  );
}

export default SignUp;
