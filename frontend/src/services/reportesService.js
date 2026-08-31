import api from './api'

const reportesService = {
  resumen: () => api.get('/reportes/resumen/'),
  ingresosPorFecha: () => api.get('/reportes/ingresos-por-fecha/'),
  ordenesPorCliente: () => api.get('/reportes/ordenes-por-cliente/'),
  estadoOrdenes: () => api.get('/reportes/estado-ordenes/'),
}

export default reportesService
