import api from './api'

const vehiculosService = {
  listar: (params) => api.get('/vehiculos/', { params }),
  obtener: (id) => api.get(`/vehiculos/${id}/`),
  crear: (data) => api.post('/vehiculos/', data),
  actualizar: (id, data) => api.put(`/vehiculos/${id}/`, data),
  eliminar: (id) => api.delete(`/vehiculos/${id}/`),
}

export default vehiculosService
