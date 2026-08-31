import React, { useState } from 'react'

function Ordenes() {
  const [ordenes, setOrdenes] = useState([])

  return (
    <div className="ordenes">
      <h2>Órdenes de Trabajo</h2>
      <button className="btn-primary">+ Nueva Orden</button>
      <table className="table">
        <thead>
          <tr>
            <th>Orden #</th>
            <th>Cliente</th>
            <th>Vehículo</th>
            <th>Estado</th>
            <th>Fecha</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {ordenes.length === 0 ? (
            <tr><td colSpan="6">No hay órdenes registradas</td></tr>
          ) : (
            ordenes.map(orden => (
              <tr key={orden.id}>
                <td>{orden.numero}</td>
                <td>{orden.cliente}</td>
                <td>{orden.vehiculo}</td>
                <td>{orden.estado}</td>
                <td>{orden.fecha}</td>
                <td>
                  <button>Ver</button>
                  <button>Editar</button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  )
}

export default Ordenes
