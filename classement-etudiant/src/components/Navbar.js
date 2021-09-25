import React from 'react'
import { Link } from 'react-router-dom';

export default function Navbar() {
    return (
        <div className="navbar">
          <div className="logo">
            <div className="text text-logo">Classament-etudiant</div>
          </div>
          <div className="login-sign">
            <Link className="btn btn-login" to="/login">Login</Link>
            <Link className="btn btn-sign" to="/sign">Sign</Link>
          </div>
        </div>
      
    )
}
