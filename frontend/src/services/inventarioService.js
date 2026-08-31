import api from './api'

const inventarioService = {
  listar: (params) => api.get('/inventario/', { params }),
  obtener: (id) => api.get(`/inventario/${id}/`),
  crear: (data) => api.post('/inventario/', data),
  actualizar: (id, data) => api.put(`/inventario/${id}/`, data),
  eliminar: (id) => api.delete(`/inventario/${id}/`),
  registrarMovimiento: (id, movimiento) => api.post(`/inventario/${id}/registrar_movimiento/`, movimiento),
  bajoStock: () => api.get('/inventario/bajo_stock/'),
}

export default inventarioService
