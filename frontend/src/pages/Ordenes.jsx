import React, { useState, useEffect } from 'react'
import ordenesService from '../services/ordenesService'

function Ordenes() {
  const [ordenes, setOrdenes] = useState([])
  const [cargando, setCargando] = useState(false)
  const [error, setError] = useState(null)
  const [formularioVisible, setFormularioVisible] = useState(false)
  const [formulario, setFormulario] = useState({
    cliente: '',
    vehiculo: '',
    descripcion: '',
    costo_estimado: '',
    fecha_vencimiento: '',
  })

  useEffect(() => {
    cargarOrdenes()
  }, [])

  const cargarOrdenes = async () => {
    setCargando(true)
    try {
      const response = await ordenesService.listar()
      setOrdenes(response.data.results || response.data)
      setError(null)
    } catch (err) {
      setError('Error al cargar órdenes: ' + err.message)
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
      await ordenesService.crear(formulario)
      setFormulario({
        cliente: '',
        vehiculo: '',
        descripcion: '',
        costo_estimado: '',
        fecha_vencimiento: '',
      })
      setFormularioVisible(false)
      cargarOrdenes()
    } catch (err) {
      setError('Error al crear orden: ' + err.message)
    }
  }

  const getEstadoColor = (estado) => {
    const colores = {
      'pendiente': 'bg-yellow-100 text-yellow-800',
      'en_proceso': 'bg-blue-100 text-blue-800',
      'pausada': 'bg-gray-100 text-gray-800',
      'completada': 'bg-green-100 text-green-800',
      'cancelada': 'bg-red-100 text-red-800',
    }
    return colores[estado] || 'bg-gray-100 text-gray-800'
  }

  return (
    <div className="ordenes">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold">Órdenes de Trabajo</h2>
        <button 
          onClick={() => setFormularioVisible(!formularioVisible)}
          className="btn-primary"
        >
          + Nueva Orden
        </button>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {formularioVisible && (
        <div className="card mb-6">
          <h3 className="text-lg font-semibold mb-4">Nueva Orden de Trabajo</h3>
          <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              type="number"
              name="cliente"
              placeholder="ID del Cliente"
              value={formulario.cliente}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="number"
              name="vehiculo"
              placeholder="ID del Vehículo"
              value={formulario.vehiculo}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <textarea
              name="descripcion"
              placeholder="Descripción del trabajo"
              value={formulario.descripcion}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2 md:col-span-2"
            ></textarea>
            <input
              type="number"
              name="costo_estimado"
              placeholder="Costo Estimado"
              value={formulario.costo_estimado}
              onChange={handleInputChange}
              step="0.01"
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="date"
              name="fecha_vencimiento"
              value={formulario.fecha_vencimiento}
              onChange={handleInputChange}
              className="border rounded px-3 py-2"
            />
            <button type="submit" className="btn-primary md:col-span-2">
              Crear Orden
            </button>
          </form>
        </div>
      )}

      {cargando ? (
        <p className="text-center py-4">Cargando órdenes...</p>
      ) : (
        <table className="table">
          <thead>
            <tr>
              <th>Orden #</th>
              <th>Cliente</th>
              <th>Vehículo</th>
              <th>Estado</th>
              <th>Costo</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {ordenes.length === 0 ? (
              <tr>
                <td colSpan="6" className="text-center py-4 text-gray-500">
                  No hay órdenes registradas
                </td>
              </tr>
            ) : (
              ordenes.map(orden => (
                <tr key={orden.id}>
                  <td><strong>{orden.numero_orden}</strong></td>
                  <td>{orden.cliente_nombre}</td>
                  <td>{orden.vehiculo_info}</td>
                  <td>
                    <span className={`px-2 py-1 rounded text-xs font-semibold ${getEstadoColor(orden.estado)}`}>
                      {orden.estado}
                    </span>
                  </td>
                  <td>${orden.costo_estimado?.toLocaleString()}</td>
                  <td>
                    <button className="text-blue-600 mr-2 hover:underline text-sm">Ver</button>
                    <button className="text-green-600 hover:underline text-sm">Editar</button>
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

export default Ordenes
