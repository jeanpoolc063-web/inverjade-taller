import React, { useState, useEffect } from 'react'
import vehiculosService from '../services/vehiculosService'

function Vehiculos() {
  const [vehiculos, setVehiculos] = useState([])
  const [cargando, setCargando] = useState(false)
  const [error, setError] = useState(null)
  const [formularioVisible, setFormularioVisible] = useState(false)
  const [formulario, setFormulario] = useState({
    cliente: '',
    placa: '',
    marca: '',
    modelo: '',
    ano: new Date().getFullYear(),
    vin: '',
    color: '',
    tipo: 'automovil',
  })

  useEffect(() => {
    cargarVehiculos()
  }, [])

  const cargarVehiculos = async () => {
    setCargando(true)
    try {
      const response = await vehiculosService.listar()
      setVehiculos(response.data.results || response.data)
      setError(null)
    } catch (err) {
      setError('Error al cargar vehículos: ' + err.message)
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
      await vehiculosService.crear(formulario)
      setFormulario({
        cliente: '',
        placa: '',
        marca: '',
        modelo: '',
        ano: new Date().getFullYear(),
        vin: '',
        color: '',
        tipo: 'automovil',
      })
      setFormularioVisible(false)
      cargarVehiculos()
    } catch (err) {
      setError('Error al crear vehículo: ' + err.message)
    }
  }

  return (
    <div className="vehiculos">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold">Gestión de Vehículos</h2>
        <button 
          onClick={() => setFormularioVisible(!formularioVisible)}
          className="btn-primary"
        >
          + Nuevo Vehículo
        </button>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {formularioVisible && (
        <div className="card mb-6">
          <h3 className="text-lg font-semibold mb-4">Nuevo Vehículo</h3>
          <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              type="text"
              name="placa"
              placeholder="Placa (ej: ABC123)"
              value={formulario.placa}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="text"
              name="marca"
              placeholder="Marca (ej: Toyota)"
              value={formulario.marca}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="text"
              name="modelo"
              placeholder="Modelo (ej: Corolla)"
              value={formulario.modelo}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="number"
              name="ano"
              placeholder="Año"
              value={formulario.ano}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="text"
              name="vin"
              placeholder="VIN"
              value={formulario.vin}
              onChange={handleInputChange}
              className="border rounded px-3 py-2"
            />
            <input
              type="text"
              name="color"
              placeholder="Color"
              value={formulario.color}
              onChange={handleInputChange}
              className="border rounded px-3 py-2"
            />
            <select
              name="tipo"
              value={formulario.tipo}
              onChange={handleInputChange}
              className="border rounded px-3 py-2"
            >
              <option value="automovil">Automóvil</option>
              <option value="camioneta">Camioneta</option>
              <option value="moto">Moto</option>
              <option value="camion">Camión</option>
              <option value="otro">Otro</option>
            </select>
            <input
              type="number"
              name="cliente"
              placeholder="ID del Cliente"
              value={formulario.cliente}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <button type="submit" className="btn-primary md:col-span-2">
              Guardar Vehículo
            </button>
          </form>
        </div>
      )}

      {cargando ? (
        <p className="text-center py-4">Cargando vehículos...</p>
      ) : (
        <table className="table">
          <thead>
            <tr>
              <th>Placa</th>
              <th>Marca</th>
              <th>Modelo</th>
              <th>Año</th>
              <th>Tipo</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {vehiculos.length === 0 ? (
              <tr>
                <td colSpan="6" className="text-center py-4 text-gray-500">
                  No hay vehículos registrados
                </td>
              </tr>
            ) : (
              vehiculos.map(vehiculo => (
                <tr key={vehiculo.id}>
                  <td><strong>{vehiculo.placa}</strong></td>
                  <td>{vehiculo.marca}</td>
                  <td>{vehiculo.modelo}</td>
                  <td>{vehiculo.ano}</td>
                  <td>{vehiculo.tipo}</td>
                  <td>
                    <button className="text-blue-600 mr-2 hover:underline">Editar</button>
                    <button className="text-red-600 hover:underline">Eliminar</button>
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

export default Vehiculos
