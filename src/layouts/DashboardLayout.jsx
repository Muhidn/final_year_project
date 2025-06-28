import React from 'react';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';
import 'bootstrap/dist/css/bootstrap.min.css';
import './DashboardLayout.css';

const DashboardLayout = ({ children }) => {
  return (
    <div className="container-fluid p-0 dashboard-layout">
      <Header />
      <div className="row g-0 dashboard-main">
        <div className="col-12 col-md-3 col-lg-2 sidebar p-0">
          <Sidebar />
        </div>
        <main className="col dashboard-content">{children}</main>
      </div>
    </div>
  );
};

export default DashboardLayout;
