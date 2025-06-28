import React, { createContext, useState } from 'react';

// Dummy user and notifications for initial state
const initialUser = {
  username: 'johndoe',
  role: 'admin', // Change this to test different roles
  profile_picture: '',
  first_name: 'John',
  last_name: 'Doe',
};
const initialNotifications = [
  'Welcome to the dashboard!',
  'Your report is ready.',
];

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(initialUser);
  const [notifications, setNotifications] = useState(initialNotifications);

  return (
    <AuthContext.Provider value={{ user, setUser, notifications, setNotifications }}>
      {children}
    </AuthContext.Provider>
  );
};
