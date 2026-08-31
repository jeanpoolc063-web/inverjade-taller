import React, { useState } from 'react'

function Vehiculos() {
  const [vehiculos, setVehiculos] = useState([])

  return (
    <div className="vehiculos">
      <h2>Gestión de Vehículos</h2>
      <button className="btn-primary">+ Nuevo Vehículo</button>
      <table className="table">
        <thead>
          <tr>
            <th>Placa</th>
            <th>Marca</th>
            <th>Modelo</th>
            <th>Año</th>
            <th>Cliente</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {vehiculos.length === 0 ? (
            <tr><td colSpan="6">No hay vehículos registrados</td></tr>
          ) : (
            vehiculos.map(vehiculo => (
              <tr key={vehiculo.id}>
                <td>{vehiculo.placa}</td>
                <td>{vehiculo.marca}</td>
                <td>{vehiculo.modelo}</td>
                <td>{vehiculo.ano}</td>
                <td>{vehiculo.cliente}</td>
                <td>
                  <button>Editar</button>
                  <button>Eliminar</button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  )
}

export default Vehiculos
