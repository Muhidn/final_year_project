import React, { useContext } from 'react';
import NotificationBell from './NotificationBell';
import ProfilePicture from './ProfilePicture';
import { AuthContext } from '../context/AuthContext';
import './Header.css';

const Header = () => {
  const { user } = useContext(AuthContext);
  return (
    <header className="dashboard-header d-flex align-items-center justify-content-between px-4 py-2 border-bottom">
      <div className="header-left d-flex align-items-center gap-3">
        <i className="bi bi-speedometer2 fs-3 text-info"></i>
        <h2 className="mb-0 fs-4">Dashboard</h2>
      </div>
      <div className="header-right d-flex align-items-center gap-4">
        <NotificationBell showCount={false} />
        <ProfilePicture src={user?.profile_picture} />
        <span className="ms-2 fw-semibold">{user?.first_name} {user?.last_name}</span>
      </div>
    </header>
  );
};

export default Header;
