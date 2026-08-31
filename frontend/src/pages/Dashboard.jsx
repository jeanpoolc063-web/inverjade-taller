import React, { useState, useEffect } from 'react'
import reportesService from '../services/reportesService'

function Dashboard() {
  const [resumen, setResumen] = useState(null)
  const [cargando, setCargando] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    cargarResumen()
  }, [])

  const cargarResumen = async () => {
    try {
      const response = await reportesService.resumen()
      setResumen(response.data)
      setError(null)
    } catch (err) {
      setError('Error al cargar resumen: ' + err.message)
      console.error(err)
    } finally {
      setCargando(false)
    }
  }

  if (cargando) {
    return <div className="text-center py-8">Cargando dashboard...</div>
  }

  if (error) {
    return (
      <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
        {error}
      </div>
    )
  }

  return (
    <div className="dashboard">
      <h2 className="text-3xl font-bold mb-2">Dashboard - INVERJADE</h2>
      <p className="text-gray-600 mb-6">Bienvenido al sistema de gestión del taller de latonería y pintura</p>
      
      {resumen && (
        <div className="dashboard-grid">
          <div className="card">
            <h3 className="text-gray-600 text-sm font-semibold uppercase">Total de Clientes</h3>
            <p className="text-3xl font-bold text-blue-600 mt-2">{resumen.total_clientes}</p>
          </div>
          <div className="card">
            <h3 className="text-gray-600 text-sm font-semibold uppercase">Total de Órdenes</h3>
            <p className="text-3xl font-bold text-green-600 mt-2">{resumen.total_ordenes}</p>
          </div>
          <div className="card">
            <h3 className="text-gray-600 text-sm font-semibold uppercase">Órdenes Pendientes</h3>
            <p className="text-3xl font-bold text-yellow-600 mt-2">{resumen.ordenes_pendientes}</p>
          </div>
          <div className="card">
            <h3 className="text-gray-600 text-sm font-semibold uppercase">En Proceso</h3>
            <p className="text-3xl font-bold text-purple-600 mt-2">{resumen.ordenes_en_proceso}</p>
          </div>
          <div className="card">
            <h3 className="text-gray-600 text-sm font-semibold uppercase">Ingresos Totales</h3>
            <p className="text-3xl font-bold text-green-700 mt-2">${resumen.ingresos_totales?.toLocaleString()}</p>
          </div>
          <div className="card">
            <h3 className="text-gray-600 text-sm font-semibold uppercase">Ingresos (30 días)</h3>
            <p className="text-3xl font-bold text-blue-700 mt-2">${resumen.ingresos_30_dias?.toLocaleString()}</p>
          </div>
          <div className="card">
            <h3 className="text-gray-600 text-sm font-semibold uppercase">Bajo Stock</h3>
            <p className="text-3xl font-bold text-red-600 mt-2">{resumen.articulos_bajo_stock}</p>
          </div>
        </div>
      )}
    </div>
  )
}

export default Dashboard
