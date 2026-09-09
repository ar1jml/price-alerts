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
      <!-- Sidebar Header -->
      <div class="sidebar-header">
        <div class="logo">
          <div class="logo-icon">P</div>
          <span>PriceTrack</span>
        </div>
      </div>

      <!-- Navigation -->
      <nav class="sidebar-nav">

        <!-- Dashboard -->
        <router-link
          to="/dashboard"
          class="nav-item"
          active-class="nav-item-active"
          exact-active-class="nav-item-active"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">▦</span>
          <span>Dashboard</span>
        </router-link>

        <!-- Products -->
        <router-link
          to="/dashboard/products"
          class="nav-item"
          active-class="nav-item-active"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">□</span>
          <span>Products</span>
        </router-link>

        <!-- Stores -->
        <router-link
          to="/dashboard/stores"
          class="nav-item"
          active-class="nav-item-active"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">⌂</span>
          <span>Stores</span>
        </router-link>

        <!-- Alerts -->
        <router-link
          to="/dashboard/alerts"
          class="nav-item"
          active-class="nav-item-active"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">♢</span>
          <span>Alerts</span>
        </router-link>

        <!-- Price History -->
        <router-link
          to="/price-history"
          class="nav-item"
          active-class="nav-item-active"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">↗</span>
          <span>Price History</span>
        </router-link>

        <!-- Users -->
        <router-link
          to="/users"
          class="nav-item"
          active-class="nav-item-active"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">♙</span>
          <span>Users</span>
        </router-link>

      </nav>

      <!-- Bottom Navigation -->
      <div class="sidebar-bottom">

        <!-- Settings -->
        <router-link
          to="/dashboard/settings"
          class="nav-item"
          active-class="nav-item-active"
          exact-active-class="nav-item-active"
          @click="mobileMenuOpen = false"
        >
          <span class="nav-icon">⚙</span>
          <span>Settings</span>
        </router-link>

        <!-- Logout -->
        <button
          type="button"
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

        <!-- Mobile Menu -->
        <button
          type="button"
          class="mobile-menu-button"
          aria-label="Open menu"
          @click="mobileMenuOpen = !mobileMenuOpen"
        >
          ☰
        </button>

        <!-- Search -->
        <div class="search-wrapper">
          <span class="search-icon">⌕</span>

          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search products..."
            aria-label="Search products"
          />
        </div>

        <!-- Right Side -->
        <div class="topbar-right">

          <!-- Notifications -->
          <button
            type="button"
            class="notification-button"
            aria-label="Notifications"
          >
            ♢
            <span class="notification-dot"></span>
          </button>

          <!-- User -->
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

      <!-- Page Content -->
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
  mobileMenuOpen.value = false
  router.push('/login')
}
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
  background: #f8fafc;
}

/* =========================
   SIDEBAR
========================= */

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

  flex-shrink: 0;
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

  overflow-y: auto;
}

/* Navigation Item */

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

  transition:
    background 0.2s ease,
    color 0.2s ease;
}

.nav-item:hover {
  background: #f3f4f6;
}

/* Active Navigation Item */

.nav-item-active {
  background: #eff6ff;
  color: #2563eb;
  font-weight: 600;
}

.nav-icon {
  width: 20px;

  display: flex;
  align-items: center;
  justify-content: center;

  text-align: center;

  font-size: 17px;

  flex-shrink: 0;
}

/* Bottom */

.sidebar-bottom {
  padding: 14px;

  border-top: 1px solid #e5e7eb;

  flex-shrink: 0;
}

.logout-button {
  appearance: none;
}

/* =========================
   MAIN AREA
========================= */

.main-area {
  margin-left: 250px;

  min-height: 100vh;
}

/* =========================
   TOPBAR
========================= */

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

/* Search */

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

  color: #111827;
}

.search-wrapper input::placeholder {
  color: #9ca3af;
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

  pointer-events: none;
}

/* Topbar Right */

.topbar-right {
  margin-left: auto;

  display: flex;
  align-items: center;

  gap: 24px;
}

/* Notifications */

.notification-button {
  position: relative;

  width: 32px;
  height: 32px;

  display: flex;
  align-items: center;
  justify-content: center;

  border: none;
  background: transparent;

  cursor: pointer;

  font-size: 20px;

  color: #4b5563;
}

.notification-button:hover {
  color: #2563eb;
}

.notification-dot {
  position: absolute;

  top: 3px;
  right: 3px;

  width: 7px;
  height: 7px;

  background: #ef4444;

  border-radius: 50%;
}

/* User */

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

/* =========================
   CONTENT
========================= */

.content {
  padding: 26px 28px 40px;
}

/* =========================
   MOBILE
========================= */

.mobile-menu-button {
  display: none;

  width: 38px;
  height: 38px;

  border: none;
  border-radius: 8px;

  background: transparent;

  font-size: 24px;

  cursor: pointer;

  color: #374151;
}

.mobile-menu-button:hover {
  background: #f3f4f6;
}

.mobile-overlay {
  display: none;
}

/* =========================
   TABLET
========================= */

@media (max-width: 900px) {

  .sidebar {
    transform: translateX(-100%);

    transition: transform 0.25s ease;

    box-shadow: 4px 0 20px rgba(0, 0, 0, 0.08);
  }

  .sidebar.sidebar-open {
    transform: translateX(0);
  }

  .main-area {
    margin-left: 0;
  }

  .mobile-menu-button {
    display: flex;
    align-items: center;
    justify-content: center;
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

/* =========================
   MOBILE
========================= */

@media (max-width: 600px) {

  .topbar {
    padding: 0 16px;

    gap: 12px;
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

  .notification-button {
    display: none;
  }
}
</style>