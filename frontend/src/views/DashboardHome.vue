<template>
  <div class="dashboard-home">

    <!-- Page Header -->
    <div class="page-header">
      <div>
        <h1>Good morning, Arafat!</h1>
        <p>Here's what's happening with your price monitoring.</p>
      </div>

      <div class="date">
        {{ currentDate }}
      </div>
    </div>

    <!-- Stats -->
    <div class="stats-grid">

      <div class="stat-card">
        <div class="stat-icon">
          📦
        </div>

        <div>
          <span>Total Products</span>
          <strong>48</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">
          🏪
        </div>

        <div>
          <span>Monitored Stores</span>
          <strong>12</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">
          🔔
        </div>

        <div>
          <span>Active Alerts</span>
          <strong>5</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">
          📈
        </div>

        <div>
          <span>Price Changes (24h)</span>
          <strong>23</strong>
        </div>
      </div>

    </div>

    <!-- Main Dashboard Grid -->
    <div class="dashboard-grid">

      <!-- Price Trends -->
      <div class="card chart-card">

        <div class="card-header">
          <div>
            <h2>Price Trends</h2>
            <p>Average product price over time</p>
          </div>

          <select v-model="period">
            <option>Last 7 days</option>
            <option>Last 30 days</option>
            <option>Last 3 months</option>
          </select>
        </div>

        <div class="chart">

          <svg
            viewBox="0 0 700 260"
            preserveAspectRatio="none"
          >

            <line x1="0" y1="40" x2="700" y2="40" />
            <line x1="0" y1="90" x2="700" y2="90" />
            <line x1="0" y1="140" x2="700" y2="140" />
            <line x1="0" y1="190" x2="700" y2="190" />
            <line x1="0" y1="240" x2="700" y2="240" />

            <polyline
              points="
                0,180
                70,155
                140,170
                210,120
                280,135
                350,95
                420,110
                490,70
                560,90
                630,55
                700,75
              "
              fill="none"
              stroke="currentColor"
              stroke-width="3"
            />

          </svg>

          <div class="chart-labels">
            <span>Mon</span>
            <span>Tue</span>
            <span>Wed</span>
            <span>Thu</span>
            <span>Fri</span>
            <span>Sat</span>
            <span>Sun</span>
          </div>

        </div>
      </div>

      <!-- Popular Products -->
      <div class="card products-card">

        <div class="card-header">
          <div>
            <h2>Popular Products</h2>
            <p>Most monitored products</p>
          </div>

          <router-link to="/dashboard/products">
            View all
          </router-link>
        </div>

        <div class="product-list">

          <div
            v-for="product in products"
            :key="product.id"
            class="product-row"
          >

            <div class="product-info">

              <div class="product-image">
                {{ product.name.charAt(0) }}
              </div>

              <div>
                <strong>{{ product.name }}</strong>
                <span>{{ product.store }}</span>
              </div>

            </div>

            <strong class="product-price">
              ${{ product.price }}
            </strong>

          </div>

        </div>

      </div>

    </div>

    <!-- Recent Alerts -->
    <div class="card alerts-card">

      <div class="card-header">
        <div>
          <h2>Recent Alerts</h2>
          <p>Your latest price monitoring alerts</p>
        </div>

        <router-link to="/dashboard/alerts">
          View all
        </router-link>
      </div>

      <div class="alerts-list">

        <div
          v-for="alert in alerts"
          :key="alert.id"
          class="alert-row"
        >

          <div class="alert-icon">
            🔔
          </div>

          <div class="alert-content">
            <strong>{{ alert.title }}</strong>
            <span>{{ alert.time }}</span>
          </div>

          <strong class="alert-price">
            {{ alert.price }}
          </strong>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const period = ref('Last 7 days')

const products = [
  {
    id: 1,
    name: 'iPhone 15 Pro',
    store: 'Amazon',
    price: '999'
  },
  {
    id: 2,
    name: 'Samsung Galaxy S24',
    store: 'Best Buy',
    price: '799'
  },
  {
    id: 3,
    name: 'MacBook Air M3',
    store: 'Amazon',
    price: '1,099'
  },
  {
    id: 4,
    name: 'Sony WH-1000XM5',
    store: 'Walmart',
    price: '349'
  }
]

const alerts = [
  {
    id: 1,
    title: 'iPhone 15 Pro price dropped',
    time: '10 minutes ago',
    price: '-$50'
  },
  {
    id: 2,
    title: 'Samsung Galaxy S24 price changed',
    time: '1 hour ago',
    price: '+$20'
  },
  {
    id: 3,
    title: 'MacBook Air M3 reached target price',
    time: '3 hours ago',
    price: '-$100'
  }
]

const currentDate = computed(() => {
  return new Date().toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
})
</script>

<style scoped>
.dashboard-home {
  width: 100%;
}

/* HEADER */

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;

  margin-bottom: 28px;
}

.page-header h1 {
  margin: 0 0 6px;

  font-size: 28px;
  font-weight: 700;

  color: #111827;
}

.page-header p {
  margin: 0;

  color: #6b7280;
  font-size: 14px;
}

.date {
  color: #6b7280;
  font-size: 14px;
}

/* STATS */

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);

  gap: 20px;

  margin-bottom: 24px;
}

.stat-card {
  background: white;

  border: 1px solid #e5e7eb;
  border-radius: 12px;

  padding: 20px;

  display: flex;
  align-items: center;

  gap: 15px;
}

.stat-icon {
  width: 48px;
  height: 48px;

  border-radius: 10px;

  background: #eff6ff;

  display: flex;
  align-items: center;
  justify-content: center;

  font-size: 21px;
}

.stat-card span {
  display: block;

  color: #6b7280;

  font-size: 13px;

  margin-bottom: 5px;
}

.stat-card strong {
  display: block;

  color: #111827;

  font-size: 24px;
}

/* GRID */

.dashboard-grid {
  display: grid;

  grid-template-columns: 2fr 1fr;

  gap: 20px;

  margin-bottom: 24px;
}

.card {
  background: white;

  border: 1px solid #e5e7eb;

  border-radius: 12px;

  padding: 20px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;

  margin-bottom: 20px;
}

.card-header h2 {
  margin: 0 0 5px;

  font-size: 17px;

  color: #111827;
}

.card-header p {
  margin: 0;

  color: #6b7280;

  font-size: 13px;
}

.card-header a {
  color: #2563eb;

  text-decoration: none;

  font-size: 14px;

  font-weight: 500;
}

.card-header select {
  padding: 8px 10px;

  border: 1px solid #d1d5db;

  border-radius: 7px;

  background: white;

  font-size: 13px;

  outline: none;
}

/* CHART */

.chart {
  height: 270px;

  position: relative;
}

.chart svg {
  width: 100%;
  height: 240px;
}

.chart line {
  stroke: #e5e7eb;
  stroke-width: 1;
}

.chart polyline {
  color: #2563eb;
}

.chart-labels {
  display: flex;

  justify-content: space-between;

  padding: 0 5px;

  color: #9ca3af;

  font-size: 12px;
}

/* PRODUCTS */

.product-list {
  display: flex;

  flex-direction: column;
}

.product-row {
  display: flex;

  align-items: center;
  justify-content: space-between;

  padding: 13px 0;

  border-bottom: 1px solid #f3f4f6;
}

.product-row:last-child {
  border-bottom: none;
}

.product-info {
  display: flex;

  align-items: center;

  gap: 12px;
}

.product-image {
  width: 40px;
  height: 40px;

  border-radius: 8px;

  background: #f3f4f6;

  display: flex;
  align-items: center;
  justify-content: center;

  font-weight: 600;

  color: #374151;
}

.product-info strong {
  display: block;

  color: #111827;

  font-size: 14px;
}

.product-info span {
  display: block;

  color: #6b7280;

  font-size: 12px;

  margin-top: 3px;
}

.product-price {
  color: #111827;

  font-size: 14px;
}

/* ALERTS */

.alerts-card {
  margin-bottom: 20px;
}

.alerts-list {
  display: flex;

  flex-direction: column;
}

.alert-row {
  display: flex;

  align-items: center;

  gap: 14px;

  padding: 14px 0;

  border-bottom: 1px solid #f3f4f6;
}

.alert-row:last-child {
  border-bottom: none;
}

.alert-icon {
  width: 40px;
  height: 40px;

  flex-shrink: 0;

  border-radius: 8px;

  background: #fff7ed;

  display: flex;
  align-items: center;
  justify-content: center;
}

.alert-content {
  flex: 1;
}

.alert-content strong {
  display: block;

  color: #111827;

  font-size: 14px;
}

.alert-content span {
  display: block;

  color: #6b7280;

  font-size: 12px;

  margin-top: 3px;
}

.alert-price {
  font-size: 14px;

  color: #111827;
}

/* RESPONSIVE */

@media (max-width: 1100px) {

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .dashboard-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 600px) {

  .page-header {
    flex-direction: column;

    gap: 10px;
  }

  .page-header h1 {
    font-size: 23px;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .card {
    padding: 16px;
  }

  .card-header {
    gap: 10px;
  }

  .card-header select {
    max-width: 120px;
  }
}
</style>