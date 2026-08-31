import api from './api'

const ordenesService = {
  listar: (params) => api.get('/ordenes/', { params }),
  obtener: (id) => api.get(`/ordenes/${id}/`),
  crear: (data) => api.post('/ordenes/', data),
  actualizar: (id, data) => api.put(`/ordenes/${id}/`, data),
  cambiarEstado: (id, estado, costo_final) => api.post(`/ordenes/${id}/cambiar_estado/`, { estado, costo_final }),
  pendientes: () => api.get('/ordenes/pendientes/'),
  enProceso: () => api.get('/ordenes/en_proceso/'),
}

export default ordenesService
