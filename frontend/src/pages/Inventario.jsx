import React, { useState, useEffect } from 'react'
import inventarioService from '../services/inventarioService'

function Inventario() {
  const [items, setItems] = useState([])
  const [cargando, setCargando] = useState(false)
  const [error, setError] = useState(null)
  const [formularioVisible, setFormularioVisible] = useState(false)
  const [formulario, setFormulario] = useState({
    codigo: '',
    descripcion: '',
    categoria: 'pintura',
    stock_actual: 0,
    stock_minimo: 5,
    precio_unitario: '',
    unidad_medida: 'unidad',
    proveedor: '',
  })

  useEffect(() => {
    cargarInventario()
  }, [])

  const cargarInventario = async () => {
    setCargando(true)
    try {
      const response = await inventarioService.listar()
      setItems(response.data.results || response.data)
      setError(null)
    } catch (err) {
      setError('Error al cargar inventario: ' + err.message)
      console.error(err)
    } finally {
      setCargando(false)
    }
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormulario(prev => ({ ...prev, [name]: value }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      await inventarioService.crear(formulario)
      setFormulario({
        codigo: '',
        descripcion: '',
        categoria: 'pintura',
        stock_actual: 0,
        stock_minimo: 5,
        precio_unitario: '',
        unidad_medida: 'unidad',
        proveedor: '',
      })
      setFormularioVisible(false)
      cargarInventario()
    } catch (err) {
      setError('Error al crear artículo: ' + err.message)
    }
  }

  const getIndicadorStock = (item) => {
    if (item.debe_reabastecer) {
      return <span className="text-red-600 font-bold">⚠️ Bajo Stock</span>
    }
    return <span className="text-green-600">✓ OK</span>
  }

  return (
    <div className="inventario">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold">Gestión de Inventario</h2>
        <button 
          onClick={() => setFormularioVisible(!formularioVisible)}
          className="btn-primary"
        >
          + Nuevo Artículo
        </button>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {formularioVisible && (
        <div className="card mb-6">
          <h3 className="text-lg font-semibold mb-4">Nuevo Artículo</h3>
          <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              type="text"
              name="codigo"
              placeholder="Código"
              value={formulario.codigo}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <select
              name="categoria"
              value={formulario.categoria}
              onChange={handleInputChange}
              className="border rounded px-3 py-2"
            >
              <option value="pintura">Pintura</option>
              <option value="solvente">Solvente</option>
              <option value="herramienta">Herramienta</option>
              <option value="material">Material</option>
              <option value="repuesto">Repuesto</option>
              <option value="otro">Otro</option>
            </select>
            <input
              type="text"
              name="descripcion"
              placeholder="Descripción"
              value={formulario.descripcion}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2 md:col-span-2"
            />
            <input
              type="number"
              name="stock_actual"
              placeholder="Stock Actual"
              value={formulario.stock_actual}
              onChange={handleInputChange}
              className="border rounded px-3 py-2"
            />
            <input
              type="number"
              name="stock_minimo"
              placeholder="Stock Mínimo"
              value={formulario.stock_minimo}
              onChange={handleInputChange}
              className="border rounded px-3 py-2"
            />
            <input
              type="number"
              name="precio_unitario"
              placeholder="Precio Unitario"
              value={formulario.precio_unitario}
              onChange={handleInputChange}
              step="0.01"
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="text"
              name="unidad_medida"
              placeholder="Unidad de Medida"
              value={formulario.unidad_medida}
              onChange={handleInputChange}
              className="border rounded px-3 py-2"
            />
            <input
              type="text"
              name="proveedor"
              placeholder="Proveedor"
              value={formulario.proveedor}
              onChange={handleInputChange}
              className="border rounded px-3 py-2 md:col-span-2"
            />
            <button type="submit" className="btn-primary md:col-span-2">
              Guardar Artículo
            </button>
          </form>
        </div>
      )}

      {cargando ? (
        <p className="text-center py-4">Cargando inventario...</p>
      ) : (
        <table className="table">
          <thead>
            <tr>
              <th>Código</th>
              <th>Descripción</th>
              <th>Categoría</th>
              <th>Stock</th>
              <th>Precio</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {items.length === 0 ? (
              <tr>
                <td colSpan="7" className="text-center py-4 text-gray-500">
                  No hay artículos en inventario
                </td>
              </tr>
            ) : (
              items.map(item => (
                <tr key={item.id}>
                  <td><strong>{item.codigo}</strong></td>
                  <td>{item.descripcion}</td>
                  <td>{item.categoria}</td>
                  <td>{item.stock_actual}</td>
                  <td>${item.precio_unitario?.toLocaleString()}</td>
                  <td>{getIndicadorStock(item)}</td>
                  <td>
                    <button className="text-blue-600 mr-2 hover:underline text-sm">Editar</button>
                    <button className="text-red-600 hover:underline text-sm">Eliminar</button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      )}
    </div>
  )
}

export default Inventario
