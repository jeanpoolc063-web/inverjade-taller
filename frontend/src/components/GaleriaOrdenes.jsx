import React, { useState, useEffect } from 'react'
import api from '../services/api'

function GaleriaOrdenes({ ordenId }) {
  const [fotos, setFotos] = useState([])
  const [cargando, setCargando] = useState(false)
  const [archivo, setArchivo] = useState(null)
  const [tipo, setTipo] = useState('antes')
  const [descripcion, setDescripcion] = useState('')
  const [enviando, setEnviando] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    if (ordenId) {
      cargarFotos()
    }
  }, [ordenId])

  const cargarFotos = async () => {
    setCargando(true)
    try {
      const response = await api.get('/ordenes/fotos/por_orden/', {
        params: { orden_id: ordenId }
      })
      setFotos(response.data)
      setError(null)
    } catch (err) {
      setError('Error al cargar fotos: ' + err.message)
      console.error(err)
    } finally {
      setCargando(false)
    }
  }

  const handleArchivoChange = (e) => {
    setArchivo(e.target.files[0])
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!archivo) {
      setError('Selecciona una imagen')
      return
    }

    setEnviando(true)
    const formData = new FormData()
    formData.append('orden_id', ordenId)
    formData.append('tipo', tipo)
    formData.append('imagen', archivo)
    formData.append('descripcion', descripcion)

    try {
      const response = await api.post('/ordenes/fotos/subir_foto/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      setFotos([...fotos, response.data])
      setArchivo(null)
      setDescripcion('')
      setTipo('antes')
      setError(null)
    } catch (err) {
      setError('Error al subir foto: ' + err.message)
      console.error(err)
    } finally {
      setEnviando(false)
    }
  }

  const getTipoColor = (tipoFoto) => {
    const colores = {
      'antes': 'bg-blue-100 text-blue-800',
      'durante': 'bg-yellow-100 text-yellow-800',
      'después': 'bg-green-100 text-green-800',
      'otro': 'bg-gray-100 text-gray-800',
    }
    return colores[tipoFoto] || 'bg-gray-100 text-gray-800'
  }

  return (
    <div className="galeria-ordenes">
      <h3 className="text-lg font-semibold mb-4">Galería de Fotos</h3>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {/* Formulario de carga */}
      <div className="card mb-6">
        <h4 className="font-semibold mb-3">Subir Foto</h4>
        <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <select
            value={tipo}
            onChange={(e) => setTipo(e.target.value)}
            className="border rounded px-3 py-2"
          >
            <option value="antes">Antes del trabajo</option>
            <option value="durante">Durante el trabajo</option>
            <option value="después">Después del trabajo</option>
            <option value="otro">Otro</option>
          </select>

          <input
            type="file"
            accept="image/*"
            onChange={handleArchivoChange}
            className="border rounded px-3 py-2"
            required
          />

          <input
            type="text"
            placeholder="Descripción (opcional)"
            value={descripcion}
            onChange={(e) => setDescripcion(e.target.value)}
            className="border rounded px-3 py-2 md:col-span-2"
          />

          <button
            type="submit"
            disabled={enviando}
            className="btn-primary md:col-span-2"
          >
            {enviando ? 'Subiendo...' : 'Subir Foto'}
          </button>
        </form>
      </div>

      {/* Galería de fotos */}
      {cargando ? (
        <p className="text-center py-4 text-gray-500">Cargando fotos...</p>
      ) : fotos.length === 0 ? (
        <p className="text-center py-4 text-gray-500">No hay fotos registradas</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {fotos.map((foto) => (
            <div key={foto.id} className="card">
              {foto.imagen && (
                <img
                  src={foto.imagen}
                  alt="Foto de orden"
                  className="w-full h-48 object-cover rounded mb-2"
                />
              )}
              <span className={`inline-block px-2 py-1 rounded text-xs font-semibold mb-2 ${getTipoColor(foto.tipo)}`}>
                {foto.tipo}
              </span>
              {foto.descripcion && (
                <p className="text-sm text-gray-600 mb-2">{foto.descripcion}</p>
              )}
              <p className="text-xs text-gray-400">
                {new Date(foto.fecha_captura).toLocaleString()}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default GaleriaOrdenes
