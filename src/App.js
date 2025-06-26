import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './component/Login';
import Signup from './component/Signup';
import Dashboard from './component/Dashboard';
import './component/Login.css';

function App() {
  const [showSignup, setShowSignup] = useState(false);
  const [user, setUser] = useState(null);

  if (user) {
    return <Dashboard user={user} />;
  }

  return (
    <div className="App">
      {showSignup ? (
        <Signup onShowLogin={() => setShowSignup(false)} />
      ) : (
        <Login onShowSignup={() => setShowSignup(true)} onLogin={setUser} />
      )}
    </div>
  );
}

export default App;
