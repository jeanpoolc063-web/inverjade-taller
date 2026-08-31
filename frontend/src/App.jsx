import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Dashboard from './pages/Dashboard'
import Clientes from './pages/Clientes'
import Vehiculos from './pages/Vehiculos'
import Ordenes from './pages/Ordenes'
import Inventario from './pages/Inventario'
import './App.css'

function App() {
  return (
    <Router>
      <div className="app">
        <Navbar />
        <main className="container">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/clientes" element={<Clientes />} />
            <Route path="/vehiculos" element={<Vehiculos />} />
            <Route path="/ordenes" element={<Ordenes />} />
            <Route path="/inventario" element={<Inventario />} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App
