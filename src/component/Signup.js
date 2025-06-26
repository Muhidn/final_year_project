import React, { useState } from 'react';
import './Login.css';

const Signup = ({ onShowLogin }) => {
  const [form, setForm] = useState({
    username: '',
    password: '',
    firstname: '',
    lastname: '',
    address: '',
    gender: '',
    email: '',
    phone: '',
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSignup = (e) => {
    e.preventDefault();
    // Add signup logic here
    alert(`Signed up as ${form.username}`);
  };

  return (
    <div className="login-container">
      <form className="login-form" onSubmit={handleSignup}>
        <h2>Sign Up</h2>
        <input type="text" name="username" placeholder="Username" value={form.username} onChange={handleChange} />
        <input type="password" name="password" placeholder="Password" value={form.password} onChange={handleChange} />
        <input type="text" name="firstname" placeholder="First Name" value={form.firstname} onChange={handleChange} />
        <input type="text" name="lastname" placeholder="Last Name" value={form.lastname} onChange={handleChange} />
        <input type="text" name="address" placeholder="Address" value={form.address} onChange={handleChange} />
        <select name="gender" value={form.gender} onChange={handleChange}>
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
        <input type="email" name="email" placeholder="Email" value={form.email} onChange={handleChange} />
        <input type="tel" name="phone" placeholder="Phone Number" value={form.phone} onChange={handleChange} />
        <button type="submit">Sign Up</button>
        <div className="signup-link">
          Already have an account?{' '}
          <span onClick={onShowLogin} className="link">Login</span>
        </div>
      </form>
    </div>
  );
};

export default Signup;
