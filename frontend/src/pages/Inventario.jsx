import React, { useState } from 'react'

function Inventario() {
  const [items, setItems] = useState([])

  return (
    <div className="inventario">
      <h2>Gestión de Inventario</h2>
      <button className="btn-primary">+ Nuevo Artículo</button>
      <table className="table">
        <thead>
          <tr>
            <th>Código</th>
            <th>Descripción</th>
            <th>Categoría</th>
            <th>Stock</th>
            <th>Precio</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {items.length === 0 ? (
            <tr><td colSpan="6">No hay artículos en inventario</td></tr>
          ) : (
            items.map(item => (
              <tr key={item.id}>
                <td>{item.codigo}</td>
                <td>{item.descripcion}</td>
                <td>{item.categoria}</td>
                <td>{item.stock}</td>
                <td>${item.precio}</td>
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

export default Inventario
