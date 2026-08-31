import React from 'react'
import { Link } from 'react-router-dom'
import './Navbar.css'

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <h1>INVERJADE</h1>
        <p>Gestión de Taller</p>
      </div>
      <ul className="navbar-menu">
        <li><Link to="/">Dashboard</Link></li>
        <li><Link to="/clientes">Clientes</Link></li>
        <li><Link to="/vehiculos">Vehículos</Link></li>
        <li><Link to="/ordenes">Órdenes</Link></li>
        <li><Link to="/inventario">Inventario</Link></li>
      </ul>
    </nav>
  )
}

export default Navbar
