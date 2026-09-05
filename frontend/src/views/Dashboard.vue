<template>
  <div class="dashboard">

    <!-- =========================
         MOBILE OVERLAY
    ========================== -->
    <div
      v-if="mobileMenuOpen"
      class="mobile-overlay"
      @click="mobileMenuOpen = false"
    ></div>


    <!-- =========================
         SIDEBAR
    ========================== -->
    <aside
      class="sidebar"
      :class="{ 'sidebar-open': mobileMenuOpen }"
    >

      <!-- Logo -->
      <div class="sidebar-brand">
        <div class="brand-icon">
          <font-awesome-icon icon="tags" />
        </div>

        <div>
          <h1>PriceTrack</h1>
          <span>Smart Price Monitoring</span>
        </div>
      </div>


      <!-- Main navigation -->
      <nav class="sidebar-nav">

        <router-link
          to="/dashboard"
          class="nav-item active"
          @click="mobileMenuOpen = false"
        >
          <font-awesome-icon icon="house" />
          <span>Dashboard</span>
        </router-link>

        <router-link
          to="/products"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <font-awesome-icon icon="box" />
          <span>Products</span>
        </router-link>

        <router-link
          to="/stores"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <font-awesome-icon icon="store" />
          <span>Stores</span>
        </router-link>

        <router-link
          to="/alerts"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <font-awesome-icon icon="bell" />
          <span>Alerts</span>
          <small>3</small>
        </router-link>

        <router-link
          to="/price-history"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <font-awesome-icon icon="chart-line" />
          <span>Price History</span>
        </router-link>

        <router-link
          to="/users"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <font-awesome-icon icon="users" />
          <span>Users</span>
        </router-link>

      </nav>


      <!-- Bottom navigation -->
      <div class="sidebar-bottom">

        <router-link
          to="/settings"
          class="nav-item"
          @click="mobileMenuOpen = false"
        >
          <font-awesome-icon icon="gear" />
          <span>Settings</span>
        </router-link>

        <button
          class="nav-item logout-button"
          @click="logout"
        >
          <font-awesome-icon icon="right-from-bracket" />
          <span>Logout</span>
        </button>

      </div>

    </aside>


    <!-- =========================
         MAIN AREA
    ========================== -->
    <main class="main-area">


      <!-- =========================
           TOP BAR
      ========================== -->
      <header class="topbar">

        <!-- Mobile menu -->
        <button
          class="mobile-menu-button"
          @click="mobileMenuOpen = true"
        >
          <font-awesome-icon icon="bars" />
        </button>


        <!-- Search -->
        <div class="search-wrapper">

          <font-awesome-icon icon="magnifying-glass" />

          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search products, stores, or categories..."
          />

        </div>


        <!-- Right side -->
        <div class="topbar-right">

          <!-- Notifications -->
          <button class="notification-button">

            <font-awesome-icon icon="bell" />

            <span>3</span>

          </button>


          <!-- User -->
          <div class="user-menu">

            <div class="avatar">
              AJ
            </div>

            <div class="user-info">
              <strong>Arafat J.</strong>
              <span>Admin</span>
            </div>

            <font-awesome-icon
              icon="chevron-down"
              class="user-chevron"
            />

          </div>

        </div>

      </header>


      <!-- =========================
           CONTENT
      ========================== -->
      <div class="content">


        <!-- Page heading -->
        <section class="page-header">

          <div>
            <h2>Good morning, Arafat!</h2>

            <p>
              Here's what's happening with your prices today.
            </p>
          </div>

          <div class="current-date">
            <span>Sep 5, 2026</span>

            <font-awesome-icon icon="calendar" />
          </div>

        </section>


        <!-- =========================
             STAT CARDS
        ========================== -->
        <section class="stats-grid">

          <div class="stat-card">

            <div class="stat-icon blue">
              <font-awesome-icon icon="box" />
            </div>

            <div class="stat-content">
              <span>Total Products</span>

              <strong>48</strong>

              <div class="stat-change positive">
                ↑ 12%
              </div>

              <small>vs. last week</small>
            </div>

          </div>


          <div class="stat-card">

            <div class="stat-icon green">
              <font-awesome-icon icon="store" />
            </div>

            <div class="stat-content">
              <span>Monitored Stores</span>

              <strong>12</strong>

              <div class="stat-change positive">
                ↑ 8%
              </div>

              <small>vs. last week</small>
            </div>

          </div>


          <div class="stat-card">

            <div class="stat-icon red">
              <font-awesome-icon icon="bell" />
            </div>

            <div class="stat-content">
              <span>Active Alerts</span>

              <strong>5</strong>

              <div class="stat-change negative">
                ↑ 67%
              </div>

              <small>vs. last week</small>
            </div>

          </div>


          <div class="stat-card">

            <div class="stat-icon purple">
              <font-awesome-icon icon="tags" />
            </div>

            <div class="stat-content">
              <span>Price Changes (24h)</span>

              <strong>23</strong>

              <div class="stat-change positive">
                ↑ 31%
              </div>

              <small>vs. yesterday</small>
            </div>

          </div>

        </section>


        <!-- =========================
             MAIN GRID
        ========================== -->
        <section class="dashboard-grid">


          <!-- =======================
               LEFT COLUMN
          ======================== -->
          <div class="left-column">


            <!-- Price Trends -->
            <section class="card chart-card">

              <div class="card-header">

                <h3>Price Trends</h3>

                <select v-model="period">
                  <option>Last 7 days</option>
                  <option>Last 30 days</option>
                  <option>Last 3 months</option>
                </select>

              </div>


              <div class="chart">

                <!-- Y axis -->
                <div class="y-axis">
                  <span>$30</span>
                  <span>$25</span>
                  <span>$20</span>
                  <span>$15</span>
                  <span>$10</span>
                </div>


                <div class="chart-body">

                  <!-- Grid -->
                  <div class="chart-grid">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>


                  <!-- SVG chart -->
                  <svg
                    class="line-chart"
                    viewBox="0 0 700 220"
                    preserveAspectRatio="none"
                  >

                    <!-- Product A -->
                    <polyline
                      points="
                        0,75
                        100,105
                        200,65
                        300,105
                        400,45
                        500,90
                        600,65
                        700,45
                      "
                      fill="none"
                      stroke="#2777ff"
                      stroke-width="3"
                    />

                    <!-- Product B -->
                    <polyline
                      points="
                        0,135
                        100,120
                        200,95
                        300,140
                        400,105
                        500,145
                        600,120
                        700,105
                      "
                      fill="none"
                      stroke="#20a66a"
                      stroke-width="3"
                    />

                    <!-- Product C -->
                    <polyline
                      points="
                        0,185
                        100,155
                        200,170
                        300,185
                        400,165
                        500,185
                        600,165
                        700,155
                      "
                      fill="none"
                      stroke="#f59e0b"
                      stroke-width="3"
                    />

                    <!-- Product A points -->
                    <g fill="#2777ff">
                      <circle cx="0" cy="75" r="4" />
                      <circle cx="100" cy="105" r="4" />
                      <circle cx="200" cy="65" r="4" />
                      <circle cx="300" cy="105" r="4" />
                      <circle cx="400" cy="45" r="4" />
                      <circle cx="500" cy="90" r="4" />
                      <circle cx="600" cy="65" r="4" />
                      <circle cx="700" cy="45" r="4" />
                    </g>

                    <!-- Product B points -->
                    <g fill="#20a66a">
                      <circle cx="0" cy="135" r="4" />
                      <circle cx="100" cy="120" r="4" />
                      <circle cx="200" cy="95" r="4" />
                      <circle cx="300" cy="140" r="4" />
                      <circle cx="400" cy="105" r="4" />
                      <circle cx="500" cy="145" r="4" />
                      <circle cx="600" cy="120" r="4" />
                      <circle cx="700" cy="105" r="4" />
                    </g>

                    <!-- Product C points -->
                    <g fill="#f59e0b">
                      <circle cx="0" cy="185" r="4" />
                      <circle cx="100" cy="155" r="4" />
                      <circle cx="200" cy="170" r="4" />
                      <circle cx="300" cy="185" r="4" />
                      <circle cx="400" cy="165" r="4" />
                      <circle cx="500" cy="185" r="4" />
                      <circle cx="600" cy="165" r="4" />
                      <circle cx="700" cy="155" r="4" />
                    </g>

                  </svg>


                  <!-- X axis -->
                  <div class="x-axis">
                    <span>Aug 29</span>
                    <span>Aug 30</span>
                    <span>Aug 31</span>
                    <span>Sep 1</span>
                    <span>Sep 2</span>
                    <span>Sep 3</span>
                    <span>Sep 4</span>
                  </div>

                </div>

              </div>


              <!-- Legend -->
              <div class="chart-legend">

                <span>
                  <i class="legend-blue"></i>
                  Product A
                </span>

                <span>
                  <i class="legend-green"></i>
                  Product B
                </span>

                <span>
                  <i class="legend-orange"></i>
                  Product C
                </span>

              </div>

            </section>


            <!-- =======================
                 POPULAR PRODUCTS
            ======================== -->
            <section class="card products-card">

              <div class="card-header">

                <h3>Popular Products</h3>

                <button class="view-all">
                  View all
                  <font-awesome-icon icon="arrow-right" />
                </button>

              </div>


              <div class="products-table-wrapper">

                <table class="products-table">

                  <thead>
                    <tr>
                      <th>Product</th>
                      <th>Category</th>
                      <th>Best Price</th>
                      <th>Lowest Store</th>
                      <th>Trend</th>
                      <th></th>
                    </tr>
                  </thead>

                  <tbody>

                    <tr
                      v-for="product in products"
                      :key="product.name"
                    >

                      <td>
                        <div class="product-name">

                          <div class="product-image">
                            {{ product.emoji }}
                          </div>

                          <strong>{{ product.name }}</strong>

                        </div>
                      </td>

                      <td>{{ product.category }}</td>

                      <td>
                        <strong>
                          {{ product.price }}
                        </strong>
                      </td>

                      <td>{{ product.store }}</td>

                      <td>
                        <span class="table-trend">
                          ↓ {{ product.change }}%
                        </span>
                      </td>

                      <td>
                        <div class="mini-chart">
                          <svg viewBox="0 0 80 25">
                            <polyline
                              :points="product.chart"
                              fill="none"
                              stroke="#2777ff"
                              stroke-width="1.7"
                            />
                          </svg>
                        </div>
                      </td>

                    </tr>

                  </tbody>

                </table>

              </div>

            </section>

          </div>


          <!-- =======================
               RIGHT COLUMN
          ======================== -->
          <section class="card alerts-card">

            <div class="card-header">

              <h3>Recent Alerts</h3>

              <button class="view-all">
                View all
                <font-awesome-icon icon="arrow-right" />
              </button>

            </div>


            <div class="alerts-list">

              <div
                v-for="alert in alerts"
                :key="alert.name"
                class="alert-item"
              >

                <div class="alert-product-image">
                  {{ alert.emoji }}
                </div>


                <div class="alert-info">

                  <strong>{{ alert.name }}</strong>

                  <span>{{ alert.store }}</span>

                  <small>{{ alert.time }}</small>

                </div>


                <div class="alert-price">

                  <strong
                    :class="alert.direction === 'down'
                      ? 'price-down'
                      : 'price-up'"
                  >
                    {{ alert.price }}
                  </strong>

                  <span
                    :class="alert.direction === 'down'
                      ? 'price-down'
                      : 'price-up'"
                  >
                    {{ alert.direction === 'down' ? '↓' : '↑' }}
                    {{ alert.change }}%
                  </span>

                </div>


                <font-awesome-icon
                  icon="chevron-right"
                  class="alert-arrow"
                />

              </div>

            </div>

          </section>

        </section>

      </div>

    </main>

  </div>
</template>


<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const searchQuery = ref('')
const period = ref('Last 7 days')
const mobileMenuOpen = ref(false)

const products = [
  {
    name: 'Whole Milk (1L)',
    category: 'Dairy',
    price: '$1.99',
    store: 'Walmart',
    change: 12,
    emoji: '🥛',
    chart: '0,15 10,20 20,10 30,18 40,8 50,15 60,10 70,12 80,8'
  },
  {
    name: 'Bananas (1kg)',
    category: 'Fruits',
    price: '$0.79',
    store: 'Kroger',
    change: 8,
    emoji: '🍌',
    chart: '0,17 10,10 20,18 30,7 40,15 50,5 60,14 70,9 80,12'
  },
  {
    name: 'Bread (White)',
    category: 'Bakery',
    price: '$1.29',
    store: 'Aldi',
    change: 5,
    emoji: '🍞',
    chart: '0,12 10,17 20,8 30,15 40,10 50,18 60,7 70,13 80,9'
  },
  {
    name: 'Eggs (12 pack)',
    category: 'Dairy',
    price: '$2.99',
    store: 'Target',
    change: 20,
    emoji: '🥚',
    chart: '0,16 10,8 20,18 30,7 40,15 50,10 60,17 70,9 80,12'
  },
  {
    name: 'Chicken Breast (1kg)',
    category: 'Meat',
    price: '$5.49',
    store: 'Walmart',
    change: 7,
    emoji: '🍗',
    chart: '0,13 10,19 20,10 30,15 40,8 50,17 60,10 70,15 80,9'
  }
]

const alerts = [
  {
    name: 'Milk 2% (1L)',
    store: 'Walmart',
    time: '2 hours ago',
    price: '$2.49',
    change: 18,
    direction: 'down',
    emoji: '🥛'
  },
  {
    name: 'Bananas (1kg)',
    store: 'Kroger',
    time: '4 hours ago',
    price: '$0.79',
    change: 12,
    direction: 'down',
    emoji: '🍌'
  },
  {
    name: 'iPhone 15',
    store: 'Best Buy',
    time: '6 hours ago',
    price: '$799.99',
    change: 5,
    direction: 'up',
    emoji: '📱'
  },
  {
    name: 'Eggs (12 pack)',
    store: 'Target',
    time: '8 hours ago',
    price: '$2.99',
    change: 20,
    direction: 'down',
    emoji: '🥚'
  },
  {
    name: 'Cheerios (General Mills)',
    store: 'Walmart',
    time: '12 hours ago',
    price: '$3.49',
    change: 14,
    direction: 'up',
    emoji: '🥣'
  }
]

function logout() {
  router.push('/login')
}
</script>


<style scoped>

/* =========================================================
   RESET
========================================================= */

* {
  box-sizing: border-box;
}

.dashboard {
  min-height: 100vh;
  width: 100%;

  display: flex;

  background: #f5f8fc;

  color: #17233b;

  font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif;
}


/* =========================================================
   SIDEBAR
========================================================= */

.sidebar {
  position: fixed;

  left: 0;
  top: 0;
  bottom: 0;

  width: 256px;

  display: flex;
  flex-direction: column;

  padding: 20px 14px;

  background:
    linear-gradient(
      180deg,
      #0b1d3b 0%,
      #081a37 100%
    );

  color: #ffffff;

  z-index: 100;
}


/* Brand */

.sidebar-brand {
  display: flex;
  align-items: center;

  gap: 11px;

  padding: 0 10px;

  margin-bottom: 38px;
}

.brand-icon {
  width: 42px;
  height: 42px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 11px;

  background: #2777ff;

  box-shadow:
    0 8px 20px rgba(39, 119, 255, .3);
}

.brand-icon svg {
  width: 19px;
}

.sidebar-brand h1 {
  margin: 0;

  font-size: 21px;
  font-weight: 700;
}

.sidebar-brand span {
  display: block;

  margin-top: 2px;

  color: #aab9d2;

  font-size: 10px;
}


/* Navigation */

.sidebar-nav {
  display: flex;
  flex-direction: column;

  gap: 4px;
}

.nav-item {
  width: 100%;

  display: flex;
  align-items: center;

  gap: 16px;

  padding: 12px 18px;

  border: none;
  border-radius: 7px;

  background: transparent;

  color: #d8e1f0;

  text-decoration: none;

  font-size: 14px;

  cursor: pointer;

  transition:
    background .2s,
    color .2s;
}

.nav-item svg {
  width: 19px;
  min-width: 19px;
}

.nav-item:hover {
  background: rgba(255,255,255,.06);
}

.nav-item.active {
  background: #2777ff;

  color: #ffffff;

  box-shadow:
    0 5px 14px rgba(39,119,255,.28);
}

.nav-item small {
  margin-left: auto;

  width: 24px;
  height: 24px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 50%;

  background: #f04444;

  color: white;

  font-size: 11px;
}

.sidebar-bottom {
  margin-top: auto;

  display: flex;
  flex-direction: column;

  gap: 5px;
}


/* =========================================================
   MAIN AREA
========================================================= */

.main-area {
  width: calc(100% - 256px);

  margin-left: 256px;

  min-width: 0;
}


/* =========================================================
   TOPBAR
========================================================= */

.topbar {
  height: 72px;

  display: flex;
  align-items: center;

  padding: 0 26px;

  background: #ffffff;

  border-bottom: 1px solid #e5eaf1;
}


/* Search */

.search-wrapper {
  width: 455px;
  height: 39px;

  display: flex;
  align-items: center;

  gap: 12px;

  padding: 0 13px;

  border: 1px solid #dfe6f0;

  border-radius: 8px;

  background: #f8fafc;

  color: #7d8ba3;
}

.search-wrapper svg {
  width: 15px;
}

.search-wrapper input {
  flex: 1;

  min-width: 0;

  border: none;
  outline: none;

  background: transparent;

  color: #17233b;

  font-size: 13px;
}

.search-wrapper input::placeholder {
  color: #8190a8;
}


/* Right */

.topbar-right {
  margin-left: auto;

  display: flex;
  align-items: center;

  gap: 27px;
}

.notification-button {
  position: relative;

  width: 30px;
  height: 40px;

  border: none;

  background: transparent;

  color: #253754;

  cursor: pointer;
}

.notification-button svg {
  width: 20px;
}

.notification-button span {
  position: absolute;

  top: 1px;
  right: -3px;

  width: 17px;
  height: 17px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 50%;

  background: #ef4444;

  color: white;

  font-size: 9px;
}


.user-menu {
  display: flex;
  align-items: center;

  gap: 10px;

  cursor: pointer;
}

.avatar {
  width: 40px;
  height: 40px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 50%;

  background: #2777ff;

  color: white;

  font-size: 13px;
  font-weight: 600;
}

.user-info {
  display: flex;
  flex-direction: column;

  gap: 2px;
}

.user-info strong {
  font-size: 12px;
}

.user-info span {
  font-size: 9px;

  color: #8290a7;
}

.user-chevron {
  width: 10px;

  color: #5e6d83;
}


/* Mobile button */

.mobile-menu-button {
  display: none;

  border: none;

  background: transparent;

  color: #17233b;

  font-size: 20px;
}


/* =========================================================
   CONTENT
========================================================= */

.content {
  padding: 20px 26px 40px;
}


/* Header */

.page-header {
  display: flex;
  align-items: center;
  justify-content: space-between;

  margin-bottom: 24px;
}

.page-header h2 {
  margin: 0 0 4px;

  font-size: 25px;
  letter-spacing: -.5px;
}

.page-header p {
  margin: 0;

  color: #657691;

  font-size: 14px;
}

.current-date {
  display: flex;
  align-items: center;

  gap: 9px;

  color: #61728e;

  font-size: 11px;
}

.current-date svg {
  width: 15px;
}


/* =========================================================
   STATS
========================================================= */

.stats-grid {
  display: grid;

  grid-template-columns:
    repeat(4, minmax(0, 1fr));

  gap: 18px;

  margin-bottom: 20px;
}

.stat-card {
  min-width: 0;

  display: flex;

  gap: 18px;

  padding: 16px;

  border: 1px solid #dfe7f1;

  border-radius: 8px;

  background: #ffffff;

  box-shadow:
    0 2px 8px rgba(28, 52, 84, .025);
}

.stat-icon {
  width: 62px;
  height: 62px;

  min-width: 62px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 50%;
}

.stat-icon svg {
  width: 27px;
}

.stat-icon.blue {
  background: #e9f1ff;
  color: #2777ff;
}

.stat-icon.green {
  background: #e4f8ef;
  color: #20a66a;
}

.stat-icon.red {
  background: #ffe8e8;
  color: #f04444;
}

.stat-icon.purple {
  background: #eeeaff;
  color: #7058e8;
}

.stat-content {
  min-width: 0;
}

.stat-content > span {
  display: block;

  color: #556884;

  font-size: 12px;

  white-space: nowrap;
}

.stat-content strong {
  display: block;

  margin: 7px 0;

  font-size: 27px;
  line-height: 1;
}

.stat-change {
  font-size: 13px;
  font-weight: 600;
}

.stat-change.positive {
  color: #20a66a;
}

.stat-change.negative {
  color: #f04444;
}

.stat-content small {
  display: block;

  margin-top: 4px;

  color: #71819b;

  font-size: 10px;
}


/* =========================================================
   DASHBOARD GRID
========================================================= */

.dashboard-grid {
  display: grid;

  grid-template-columns:
    minmax(0, 2fr)
    minmax(330px, .85fr);

  gap: 18px;

  align-items: start;
}

.left-column {
  min-width: 0;

  display: flex;
  flex-direction: column;

  gap: 18px;
}


/* =========================================================
   CARD
========================================================= */

.card {
  min-width: 0;

  border: 1px solid #dfe7f1;

  border-radius: 9px;

  background: #ffffff;

  box-shadow:
    0 2px 8px rgba(28, 52, 84, .025);
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: 18px 18px 14px;
}

.card-header h3 {
  margin: 0;

  font-size: 18px;
}

.card-header select {
  height: 34px;

  padding: 0 12px;

  border: 1px solid #dce5ef;

  border-radius: 7px;

  background: #ffffff;

  color: #344765;

  outline: none;

  font-size: 11px;
}


/* =========================================================
   CHART
========================================================= */

.chart-card {
  padding-bottom: 16px;
}

.chart {
  display: flex;

  height: 245px;

  padding: 4px 18px 0;
}

.y-axis {
  width: 38px;

  display: flex;
  flex-direction: column;
  justify-content: space-between;

  padding: 4px 0 31px;

  color: #71819b;

  font-size: 10px;
}

.chart-body {
  position: relative;

  flex: 1;

  min-width: 0;

  padding-bottom: 30px;
}

.chart-grid {
  position: absolute;

  left: 0;
  right: 0;
  top: 5px;
  bottom: 30px;

  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.chart-grid span {
  width: 100%;
  height: 1px;

  background: #edf1f6;
}

.line-chart {
  position: absolute;

  left: 0;
  right: 0;
  top: 5px;

  width: 100%;
  height: calc(100% - 35px);
}

.x-axis {
  position: absolute;

  left: 0;
  right: 0;
  bottom: 4px;

  display: flex;
  justify-content: space-between;

  color: #71819b;

  font-size: 9px;
}

.chart-legend {
  display: flex;
  justify-content: center;

  gap: 28px;

  color: #61728e;

  font-size: 10px;
}

.chart-legend span {
  display: flex;
  align-items: center;

  gap: 6px;
}

.chart-legend i {
  width: 8px;
  height: 8px;

  display: inline-block;

  border-radius: 50%;
}

.legend-blue {
  background: #2777ff;
}

.legend-green {
  background: #20a66a;
}

.legend-orange {
  background: #f59e0b;
}


/* =========================================================
   PRODUCTS
========================================================= */

.products-card {
  overflow: hidden;
}

.view-all {
  display: flex;
  align-items: center;

  gap: 5px;

  border: none;

  background: transparent;

  color: #2777ff;

  font-size: 11px;

  cursor: pointer;
}

.view-all svg {
  width: 10px;
}

.products-table-wrapper {
  width: 100%;

  overflow-x: auto;

  padding: 0 18px 10px;
}

.products-table {
  width: 100%;

  border-collapse: collapse;

  min-width: 620px;
}

.products-table th {
  padding: 8px 6px;

  background: #f5f8fc;

  color: #5e708e;

  font-size: 10px;

  text-align: left;

  font-weight: 600;
}

.products-table td {
  padding: 9px 6px;

  border-bottom: 1px solid #edf1f5;

  color: #344765;

  font-size: 10px;
}

.products-table tbody tr:last-child td {
  border-bottom: none;
}

.product-name {
  display: flex;
  align-items: center;

  gap: 9px;
}

.product-name strong {
  color: #17233b;

  font-size: 11px;
}

.product-image {
  width: 29px;
  height: 29px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 6px;

  background: #f6f8fb;

  font-size: 18px;
}

.table-trend {
  color: #20a66a;

  font-weight: 600;
}

.mini-chart {
  width: 75px;
  height: 25px;
}

.mini-chart svg {
  width: 100%;
  height: 100%;
}


/* =========================================================
   ALERTS
========================================================= */

.alerts-card {
  min-width: 0;
}

.alerts-list {
  padding: 0 18px 8px;
}

.alert-item {
  display: grid;

  grid-template-columns:
    56px
    minmax(0, 1fr)
    auto
    10px;

  align-items: center;

  gap: 12px;

  min-height: 91px;

  border-top: 1px solid #edf1f5;
}

.alert-product-image {
  width: 56px;
  height: 56px;

  display: flex;
  align-items: center;
  justify-content: center;

  border: 1px solid #e1e8f1;

  border-radius: 8px;

  background: #f9fbfd;

  font-size: 29px;
}

.alert-info {
  min-width: 0;

  display: flex;
  flex-direction: column;

  gap: 3px;
}

.alert-info strong {
  overflow: hidden;

  color: #17233b;

  font-size: 12px;

  white-space: nowrap;
  text-overflow: ellipsis;
}

.alert-info span {
  color: #5e708e;

  font-size: 10px;
}

.alert-info small {
  color: #7c8ca5;

  font-size: 9px;
}

.alert-price {
  display: flex;
  flex-direction: column;
  align-items: flex-end;

  gap: 4px;

  white-space: nowrap;
}

.alert-price strong {
  font-size: 12px;
}

.alert-price span {
  font-size: 10px;
  font-weight: 600;
}

.price-down {
  color: #20a66a;
}

.price-up {
  color: #f04444;
}

.alert-arrow {
  width: 8px;

  color: #71819b;
}


/* =========================================================
   MOBILE OVERLAY
========================================================= */

.mobile-overlay {
  display: none;
}


/* =========================================================
   TABLET
========================================================= */

@media (max-width: 1200px) {

  .sidebar {
    width: 220px;
  }

  .main-area {
    width: calc(100% - 220px);
    margin-left: 220px;
  }

  .content {
    padding-left: 20px;
    padding-right: 20px;
  }

  .dashboard-grid {
    grid-template-columns: 1fr;
  }

  .alerts-card {
    width: 100%;
  }

  .alerts-list {
    display: grid;

    grid-template-columns: 1fr 1fr;

    column-gap: 20px;
  }

  .alert-item {
    border-top: 1px solid #edf1f5;
  }

}


/* =========================================================
   TABLET / SMALL LAPTOP
========================================================= */

@media (max-width: 992px) {

  .sidebar {
    width: 210px;
  }

  .main-area {
    width: calc(100% - 210px);
    margin-left: 210px;
  }

  .stats-grid {
    grid-template-columns: 1fr 1fr;
  }

  .search-wrapper {
    width: 350px;
  }

}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 768px) {

  .sidebar {
    width: 260px;

    transform: translateX(-100%);

    transition: transform .25s ease;
  }

  .sidebar.sidebar-open {
    transform: translateX(0);
  }

  .mobile-overlay {
    position: fixed;

    inset: 0;

    display: block;

    background: rgba(0, 0, 0, .35);

    z-index: 90;
  }

  .main-area {
    width: 100%;
    margin-left: 0;
  }

  .topbar {
    height: 64px;

    padding: 0 16px;

    gap: 12px;
  }

  .mobile-menu-button {
    display: flex;

    width: 35px;
    height: 35px;

    align-items: center;
    justify-content: center;
  }

  .search-wrapper {
    flex: 1;

    width: auto;
    height: 38px;
  }

  .topbar-right {
    gap: 12px;
  }

  .user-info,
  .user-chevron {
    display: none;
  }

  .notification-button {
    width: 28px;
  }

  .avatar {
    width: 36px;
    height: 36px;
  }

  .content {
    padding: 20px 16px 35px;
  }

  .page-header {
    align-items: flex-start;

    gap: 15px;
  }

  .page-header h2 {
    font-size: 22px;
  }

  .page-header p {
    font-size: 12px;
    line-height: 1.5;
  }

  .current-date {
    display: none;
  }

  .stats-grid {
    grid-template-columns: 1fr 1fr;

    gap: 12px;
  }

  .stat-card {
    gap: 11px;

    padding: 13px;
  }

  .stat-icon {
    width: 45px;
    height: 45px;

    min-width: 45px;
  }

  .stat-icon svg {
    width: 20px;
  }

  .stat-content > span {
    font-size: 10px;
  }

  .stat-content strong {
    font-size: 21px;
  }

  .stat-change {
    font-size: 11px;
  }

  .stat-content small {
    font-size: 8px;
  }

  .dashboard-grid {
    display: flex;
    flex-direction: column;
  }

  .left-column,
  .alerts-card {
    width: 100%;
  }

  .chart {
    height: 220px;
  }

  .alerts-list {
    display: block;
  }

}


/* =========================================================
   SMALL MOBILE
========================================================= */

@media (max-width: 480px) {

  .topbar {
    padding: 0 11px;
  }

  .search-wrapper {
    gap: 7px;

    padding: 0 9px;
  }

  .search-wrapper input {
    font-size: 11px;
  }

  .notification-button {
    display: none;
  }

  .content {
    padding: 17px 12px 30px;
  }

  .page-header h2 {
    font-size: 19px;
  }

  .page-header p {
    font-size: 11px;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .stat-card {
    min-height: 82px;
  }

  .stat-icon {
    width: 50px;
    height: 50px;

    min-width: 50px;
  }

  .card-header {
    padding: 15px 13px 12px;
  }

  .card-header h3 {
    font-size: 16px;
  }

  .chart-card {
    overflow: hidden;
  }

  .chart {
    height: 205px;

    padding-left: 10px;
    padding-right: 10px;
  }

  .y-axis {
    width: 30px;

    font-size: 8px;
  }

  .x-axis {
    font-size: 7px;
  }

  .chart-legend {
    gap: 13px;

    font-size: 8px;
  }

  .products-table-wrapper {
    padding-left: 10px;
    padding-right: 10px;
  }

  .alerts-list {
    padding-left: 10px;
    padding-right: 10px;
  }

  .alert-item {
    grid-template-columns:
      48px
      minmax(0, 1fr)
      auto
      8px;

    gap: 8px;

    min-height: 82px;
  }

  .alert-product-image {
    width: 48px;
    height: 48px;

    font-size: 24px;
  }

  .alert-info strong {
    font-size: 10px;
  }

  .alert-info span,
  .alert-info small {
    font-size: 8px;
  }

  .alert-price strong {
    font-size: 10px;
  }

  .alert-price span {
    font-size: 8px;
  }

}


/* =========================================================
   VERY SMALL PHONES
========================================================= */

@media (max-width: 360px) {

  .search-wrapper {
    max-width: 180px;
  }

  .page-header h2 {
    font-size: 17px;
  }

  .page-header p {
    font-size: 10px;
  }

  .stat-card {
    padding: 11px;
  }

  .stat-icon {
    width: 43px;
    height: 43px;

    min-width: 43px;
  }

  .stat-content strong {
    font-size: 19px;
  }

}

</style>