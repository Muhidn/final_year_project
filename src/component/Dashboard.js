import React from 'react';
import './Dashboard.css';

const Dashboard = ({ user }) => {
  return (
    <div className="dashboard-container">
      <h1>Welcome, {user.first_name} {user.last_name}</h1>
      <p><strong>Username:</strong> {user.username}</p>
      <p><strong>Email:</strong> {user.email}</p>
      <p><strong>Role:</strong> {user.role}</p>
      <p><strong>Address:</strong> {user.address}</p>
      <p><strong>Phone:</strong> {user.phone_number}</p>
      {/* Add more fields as needed */}
    </div>
  );
};

export default Dashboard;
