import React from 'react'

function Dashboard() {
  return (
    <div className="dashboard">
      <h2>Dashboard - INVERJADE</h2>
      <p>Bienvenido al sistema de gestión del taller de latonería y pintura</p>
      <div className="dashboard-grid">
        <div className="card">
          <h3>Clientes</h3>
          <p>0</p>
        </div>
        <div className="card">
          <h3>Vehículos</h3>
          <p>0</p>
        </div>
        <div className="card">
          <h3>Órdenes Pendientes</h3>
          <p>0</p>
        </div>
        <div className="card">
          <h3>Ingresos Totales</h3>
          <p>$0</p>
        </div>
      </div>
    </div>
  )
}

export default Dashboard
