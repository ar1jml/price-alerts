<template>
  <div class="dashboard">

    <!-- Mobile Overlay -->
    <div
      v-if="mobileMenuOpen"
      class="mobile-overlay"
      @click="mobileMenuOpen = false"
    ></div>

    <!-- Sidebar -->
    <aside
      class="sidebar"
      :class="{ 'sidebar-open': mobileMenuOpen }"
    >
      <div class="sidebar-header">
        <div class="logo">
          <div class="logo-icon">P</div>
          <span>PriceTrack</span>
        </div>
      </div>

      <nav class="sidebar-nav">

        <router-link
          to="/dashboard"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">▦</span>
          <span>Dashboard</span>
        </router-link>

        <router-link
          to="/dashboard/products"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">□</span>
          <span>Products</span>
        </router-link>

        <router-link
  to="/dashboard/stores"
  class="nav-item"
  @click="mobileMenuOpen = false"
>
  <span class="nav-icon">⌂</span>
  <span>Stores</span>
</router-link>
        <router-link
          to="/dashboard/alerts"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">♢</span>
          <span>Alerts</span>
        </router-link>

        <router-link
          to="/price-history"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">↗</span>
          <span>Price History</span>
        </router-link>

        <router-link
          to="/users"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">♙</span>
          <span>Users</span>
        </router-link>

      </nav>

      <div class="sidebar-bottom">

        <router-link
          to="/settings"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">⚙</span>
          <span>Settings</span>
        </router-link>

        <button
          class="nav-item logout-button"
          @click="logout"
        >
          <span class="nav-icon">↪</span>
          <span>Logout</span>
        </button>

      </div>
    </aside>

    <!-- Main Area -->
    <div class="main-area">

      <!-- Topbar -->
      <header class="topbar">

        <button
          class="mobile-menu-button"
          @click="mobileMenuOpen = !mobileMenuOpen"
        >
          ☰
        </button>

        <div class="search-wrapper">
          <span class="search-icon">⌕</span>

          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search products..."
          />
        </div>

        <div class="topbar-right">

          <button class="notification-button">
            ♢
            <span class="notification-dot"></span>
          </button>

          <div class="user-menu">
            <div class="user-avatar">
              A
            </div>

            <div class="user-info">
              <strong>Arafat</strong>
              <span>Admin</span>
            </div>
          </div>

        </div>
      </header>

      <!-- THIS IS WHERE DashboardHome / Products / Alerts APPEAR -->
      <main class="content">
        <router-view />
      </main>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const searchQuery = ref('')
const mobileMenuOpen = ref(false)

function logout() {
  router.push('/login')
}
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
  background: #f8fafc;
}

/* SIDEBAR */

.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;

  width: 250px;

  background: #ffffff;
  border-right: 1px solid #e5e7eb;

  display: flex;
  flex-direction: column;

  z-index: 1000;
}

.sidebar-header {
  height: 72px;
  display: flex;
  align-items: center;

  padding: 0 24px;

  border-bottom: 1px solid #e5e7eb;
}

.logo {
  display: flex;
  align-items: center;
  gap: 11px;

  font-size: 20px;
  font-weight: 700;

  color: #111827;
}

.logo-icon {
  width: 36px;
  height: 36px;

  border-radius: 9px;

  display: flex;
  align-items: center;
  justify-content: center;

  background: #2563eb;
  color: white;

  font-weight: 700;
}

.sidebar-nav {
  flex: 1;
  padding: 22px 14px;
}

.nav-item {
  width: 100%;

  display: flex;
  align-items: center;

  gap: 12px;

  padding: 12px 14px;
  margin-bottom: 5px;

  border-radius: 8px;

  border: none;
  background: transparent;

  color: #4b5563;

  text-decoration: none;

  font-size: 14px;
  font-family: inherit;

  cursor: pointer;

  box-sizing: border-box;

  text-align: left;
}

.nav-item:hover {
  background: #f3f4f6;
}

.nav-item.router-link-active {
  background: #eff6ff;
  color: #2563eb;
  font-weight: 600;
}

.nav-icon {
  width: 20px;
  text-align: center;
  font-size: 17px;
}

.sidebar-bottom {
  padding: 14px;

  border-top: 1px solid #e5e7eb;
}

.logout-button {
  text-align: left;
}

/* MAIN */

.main-area {
  margin-left: 250px;
  min-height: 100vh;
}

/* TOPBAR */

.topbar {
  height: 72px;

  background: #ffffff;
  border-bottom: 1px solid #e5e7eb;

  display: flex;
  align-items: center;

  padding: 0 28px;

  gap: 20px;

  position: sticky;
  top: 0;

  z-index: 100;
}

.search-wrapper {
  position: relative;
  width: 360px;
}

.search-wrapper input {
  width: 100%;
  height: 40px;

  box-sizing: border-box;

  padding: 0 15px 0 38px;

  border: 1px solid #e5e7eb;
  border-radius: 8px;

  outline: none;

  font-size: 14px;

  background: #f9fafb;
}

.search-wrapper input:focus {
  border-color: #2563eb;
  background: #ffffff;
}

.search-icon {
  position: absolute;

  left: 13px;
  top: 50%;

  transform: translateY(-50%);

  color: #9ca3af;

  font-size: 18px;

  z-index: 1;
}

.topbar-right {
  margin-left: auto;

  display: flex;
  align-items: center;

  gap: 24px;
}

.notification-button {
  position: relative;

  border: none;
  background: transparent;

  cursor: pointer;

  font-size: 20px;

  color: #4b5563;
}

.notification-dot {
  position: absolute;

  top: 0;
  right: 0;

  width: 7px;
  height: 7px;

  background: #ef4444;

  border-radius: 50%;
}

.user-menu {
  display: flex;
  align-items: center;

  gap: 10px;
}

.user-avatar {
  width: 38px;
  height: 38px;

  border-radius: 50%;

  background: #2563eb;
  color: white;

  display: flex;
  align-items: center;
  justify-content: center;

  font-weight: 600;
}

.user-info strong {
  display: block;

  font-size: 14px;
  color: #111827;
}

.user-info span {
  display: block;

  margin-top: 2px;

  color: #6b7280;

  font-size: 12px;
}

/* CONTENT */

.content {
  padding: 26px 28px 40px;
}

/* MOBILE */

.mobile-menu-button {
  display: none;

  border: none;
  background: transparent;

  font-size: 24px;

  cursor: pointer;

  color: #374151;
}

.mobile-overlay {
  display: none;
}

@media (max-width: 900px) {

  .sidebar {
    transform: translateX(-100%);
    transition: transform 0.25s ease;
  }

  .sidebar.sidebar-open {
    transform: translateX(0);
  }

  .main-area {
    margin-left: 0;
  }

  .mobile-menu-button {
    display: block;
  }

  .mobile-overlay {
    display: block;

    position: fixed;
    inset: 0;

    background: rgba(0, 0, 0, 0.35);

    z-index: 999;
  }

  .search-wrapper {
    width: 260px;
  }
}

@media (max-width: 600px) {

  .topbar {
    padding: 0 16px;
  }

  .search-wrapper {
    flex: 1;
    width: auto;
  }

  .user-info {
    display: none;
  }

  .content {
    padding: 20px 16px 30px;
  }

  .topbar-right {
    gap: 10px;
  }
}
</style>