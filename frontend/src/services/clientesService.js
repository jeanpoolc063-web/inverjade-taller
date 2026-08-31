import api from './api'

const clientesService = {
  listar: (params) => api.get('/clientes/', { params }),
  obtener: (id) => api.get(`/clientes/${id}/`),
  crear: (data) => api.post('/clientes/', data),
  actualizar: (id, data) => api.put(`/clientes/${id}/`, data),
  eliminar: (id) => api.delete(`/clientes/${id}/`),
  cambiarEstado: (id, estado) => api.post(`/clientes/${id}/cambiar_estado/`, { estado }),
}

export default clientesService
