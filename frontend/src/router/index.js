import { createRouter, createWebHistory } from 'vue-router'

import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import DashboardHome from '../views/DashboardHome.vue'
import Products from '../views/Products.vue'
import Alerts from '../views/Alerts.vue'
import Stores from '../views/Stores.vue'
import PriceHistory from '../views/PriceHistory.vue'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },

  // Login
  {
    path: '/login',
    name: 'Login',
    component: Login
  },

  // Dashboard Layout
  {
    path: '/dashboard',
    component: Dashboard,

    children: [
      // Dashboard Home
      {
        path: '',
        name: 'DashboardHome',
        component: DashboardHome
      },

      // Products
      {
        path: 'products',
        name: 'Products',
        component: Products
      },

      // Stores
      {
        path: 'stores',
        name: 'Stores',
        component: Stores
      },
      {
  path: '/price-history',
  name: 'PriceHistory',
  component: PriceHistory
},

      // Alerts
      {
        path: 'alerts',
        name: 'Alerts',
        component: Alerts
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router