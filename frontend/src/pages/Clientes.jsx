import React, { useState, useEffect } from 'react'
import clientesService from '../services/clientesService'

function Clientes() {
  const [clientes, setClientes] = useState([])
  const [cargando, setCargando] = useState(false)
  const [error, setError] = useState(null)
  const [formularioVisible, setFormularioVisible] = useState(false)
  const [formulario, setFormulario] = useState({
    nombre: '',
    tipo_documento: 'CC',
    numero_documento: '',
    telefono: '',
    email: '',
    direccion: '',
    ciudad: '',
  })

  useEffect(() => {
    cargarClientes()
  }, [])

  const cargarClientes = async () => {
    setCargando(true)
    try {
      const response = await clientesService.listar()
      setClientes(response.data.results || response.data)
      setError(null)
    } catch (err) {
      setError('Error al cargar clientes: ' + err.message)
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
      await clientesService.crear(formulario)
      setFormulario({
        nombre: '',
        tipo_documento: 'CC',
        numero_documento: '',
        telefono: '',
        email: '',
        direccion: '',
        ciudad: '',
      })
      setFormularioVisible(false)
      cargarClientes()
    } catch (err) {
      setError('Error al crear cliente: ' + err.message)
    }
  }

  const handleEliminar = async (id) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar este cliente?')) {
      try {
        await clientesService.eliminar(id)
        cargarClientes()
      } catch (err) {
        setError('Error al eliminar cliente: ' + err.message)
      }
    }
  }

  return (
    <div className="clientes">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold">Gestión de Clientes</h2>
        <button 
          onClick={() => setFormularioVisible(!formularioVisible)}
          className="btn-primary"
        >
          + Nuevo Cliente
        </button>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {formularioVisible && (
        <div className="card mb-6">
          <h3 className="text-lg font-semibold mb-4">Nuevo Cliente</h3>
          <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              type="text"
              name="nombre"
              placeholder="Nombre"
              value={formulario.nombre}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <select
              name="tipo_documento"
              value={formulario.tipo_documento}
              onChange={handleInputChange}
              className="border rounded px-3 py-2"
            >
              <option value="CC">Cédula de Ciudadanía</option>
              <option value="CE">Cédula de Extranjería</option>
              <option value="NIT">NIT</option>
              <option value="OTRO">Otro</option>
            </select>
            <input
              type="text"
              name="numero_documento"
              placeholder="Número de Documento"
              value={formulario.numero_documento}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="tel"
              name="telefono"
              placeholder="Teléfono"
              value={formulario.telefono}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="email"
              name="email"
              placeholder="Email"
              value={formulario.email}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="text"
              name="ciudad"
              placeholder="Ciudad"
              value={formulario.ciudad}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2"
            />
            <input
              type="text"
              name="direccion"
              placeholder="Dirección"
              value={formulario.direccion}
              onChange={handleInputChange}
              required
              className="border rounded px-3 py-2 md:col-span-2"
            />
            <button type="submit" className="btn-primary md:col-span-2">
              Guardar Cliente
            </button>
          </form>
        </div>
      )}

      {cargando ? (
        <p className="text-center py-4">Cargando clientes...</p>
      ) : (
        <table className="table">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Documento</th>
              <th>Teléfono</th>
              <th>Email</th>
              <th>Ciudad</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {clientes.length === 0 ? (
              <tr>
                <td colSpan="6" className="text-center py-4 text-gray-500">
                  No hay clientes registrados
                </td>
              </tr>
            ) : (
              clientes.map(cliente => (
                <tr key={cliente.id}>
                  <td>{cliente.nombre}</td>
                  <td>{cliente.numero_documento}</td>
                  <td>{cliente.telefono}</td>
                  <td>{cliente.email}</td>
                  <td>{cliente.ciudad}</td>
                  <td>
                    <button className="text-blue-600 mr-2 hover:underline">Editar</button>
                    <button 
                      onClick={() => handleEliminar(cliente.id)}
                      className="text-red-600 hover:underline"
                    >
                      Eliminar
                    </button>
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

export default Clientes
