import React, { useState } from 'react';
import axios from 'axios';

function Login() {
  const [form, setForm] = useState({ email: '', password: '' });
  const [msg, setMsg] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:5000/login', form);
      const token = res.data.token;
      localStorage.setItem('token', token); // Save token
      setMsg('Login successful!');
    } catch (err) {
      setMsg('Login failed');
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input type="email" placeholder="Email" onChange={(e) => setForm({ ...form, email: e.target.value })} required />
        <input type="password" placeholder="Password" onChange={(e) => setForm({ ...form, password: e.target.value })} required />
        <button type="submit">Login</button>
      </form>
      <p>{msg}</p>
    </div>
  );
}

export default Login;
