import React from 'react'
import ProtectedRoute from '../../components/ProtectedRoute'
import Header from '../../components/Header'

const AdminLogin = () => {
  return (
    <ProtectedRoute>
      <Header/>
    </ProtectedRoute>
  )
}

export default AdminLogin