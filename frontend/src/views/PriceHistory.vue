<template>
  <div class="price-history-page">
    <!-- Header -->
    <div class="page-header">
      <div>
        <h1>Price History</h1>
        <p>Track how product prices change over time.</p>
      </div>

      <button class="refresh-btn" @click="refreshData">
        ↻ Refresh
      </button>
    </div>

    <!-- Product selector -->
    <div class="filter-card">
      <div class="filter-group">
        <label>Product</label>

        <select v-model="selectedProduct">
          <option value="iphone">iPhone 15</option>
          <option value="samsung">Samsung Galaxy S24</option>
          <option value="macbook">MacBook Air M3</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Store</label>

        <select v-model="selectedStore">
          <option value="all">All Stores</option>
          <option value="amazon">Amazon</option>
          <option value="bestbuy">Best Buy</option>
          <option value="walmart">Walmart</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Period</label>

        <select v-model="selectedPeriod">
          <option value="7">Last 7 days</option>
          <option value="30">Last 30 days</option>
          <option value="90">Last 3 months</option>
          <option value="365">Last year</option>
        </select>
      </div>
    </div>

    <!-- Product information -->
    <div class="product-card">
      <div class="product-info">
        <div class="product-image">
          📦
        </div>

        <div>
          <h2>{{ product.name }}</h2>
          <p>{{ product.store }}</p>
        </div>
      </div>

      <div class="current-price">
        <span>Current Price</span>
        <strong>${{ product.currentPrice.toFixed(2) }}</strong>
      </div>
    </div>

    <!-- Statistics -->
    <div class="stats-grid">
      <div class="stat-card">
        <span>Lowest Price</span>
        <strong>${{ lowestPrice.toFixed(2) }}</strong>
        <small>Best price recorded</small>
      </div>

      <div class="stat-card">
        <span>Highest Price</span>
        <strong>${{ highestPrice.toFixed(2) }}</strong>
        <small>Highest price recorded</small>
      </div>

      <div class="stat-card">
        <span>Average Price</span>
        <strong>${{ averagePrice.toFixed(2) }}</strong>
        <small>Average historical price</small>
      </div>

      <div class="stat-card">
        <span>Price Change</span>
        <strong :class="priceChange >= 0 ? 'increase' : 'decrease'">
          {{ priceChange >= 0 ? '+' : '' }}{{ priceChange.toFixed(1) }}%
        </strong>
        <small>Compared with previous price</small>
      </div>
    </div>

    <!-- Chart -->
    <div class="chart-card">
      <div class="chart-header">
        <div>
          <h2>Price Trend</h2>
          <p>Historical price changes</p>
        </div>

        <div class="chart-legend">
          <span class="legend-line"></span>
          Price
        </div>
      </div>

      <div class="chart">
        <div class="y-axis">
          <span>$900</span>
          <span>$850</span>
          <span>$800</span>
          <span>$750</span>
          <span>$700</span>
        </div>

        <div class="chart-area">
          <div class="grid-line line-1"></div>
          <div class="grid-line line-2"></div>
          <div class="grid-line line-3"></div>
          <div class="grid-line line-4"></div>
          <div class="grid-line line-5"></div>

          <svg
            viewBox="0 0 800 300"
            preserveAspectRatio="none"
            class="price-chart"
          >
            <polyline
              points="0,190 100,170 200,205 300,140 400,155 500,110 600,125 700,85 800,105"
              fill="none"
              stroke="currentColor"
              stroke-width="4"
              stroke-linecap="round"
              stroke-linejoin="round"
            />

            <circle cx="0" cy="190" r="5" />
            <circle cx="100" cy="170" r="5" />
            <circle cx="200" cy="205" r="5" />
            <circle cx="300" cy="140" r="5" />
            <circle cx="400" cy="155" r="5" />
            <circle cx="500" cy="110" r="5" />
            <circle cx="600" cy="125" r="5" />
            <circle cx="700" cy="85" r="5" />
            <circle cx="800" cy="105" r="5" />
          </svg>

          <div class="x-axis">
            <span>Sep 1</span>
            <span>Sep 3</span>
            <span>Sep 5</span>
            <span>Sep 7</span>
            <span>Sep 9</span>
            <span>Sep 11</span>
            <span>Sep 13</span>
            <span>Sep 15</span>
          </div>
        </div>
      </div>
    </div>

    <!-- History table -->
    <div class="history-card">
      <div class="history-header">
        <div>
          <h2>Price Records</h2>
          <p>Recent price observations for this product.</p>
        </div>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Date</th>
              <th>Store</th>
              <th>Price</th>
              <th>Change</th>
            </tr>
          </thead>

          <tbody>
            <tr
              v-for="(record, index) in priceHistory"
              :key="record.date"
            >
              <td>{{ record.date }}</td>

              <td>{{ record.store }}</td>

              <td class="price">
                ${{ record.price.toFixed(2) }}
              </td>

              <td>
                <span
                  :class="
                    index === priceHistory.length - 1
                      ? 'change neutral'
                      : record.price < priceHistory[index + 1].price
                        ? 'change down'
                        : 'change up'
                  "
                >
                  {{
                    index === priceHistory.length - 1
                      ? '—'
                      : record.price < priceHistory[index + 1].price
                        ? '↓ Lower'
                        : '↑ Higher'
                  }}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'

const selectedProduct = ref('iphone')
const selectedStore = ref('all')
const selectedPeriod = ref('30')

const products = {
  iphone: {
    name: 'iPhone 15',
    store: 'Amazon',
    currentPrice: 799.99
  },

  samsung: {
    name: 'Samsung Galaxy S24',
    store: 'Best Buy',
    currentPrice: 749.99
  },

  macbook: {
    name: 'MacBook Air M3',
    store: 'Amazon',
    currentPrice: 1099.99
  }
}

const product = computed(() => products[selectedProduct.value])

const priceHistory = ref([
  {
    date: 'Sep 15, 2026',
    store: 'Amazon',
    price: 799.99
  },
  {
    date: 'Sep 13, 2026',
    store: 'Amazon',
    price: 819.99
  },
  {
    date: 'Sep 11, 2026',
    store: 'Amazon',
    price: 789.99
  },
  {
    date: 'Sep 9, 2026',
    store: 'Amazon',
    price: 829.99
  },
  {
    date: 'Sep 7, 2026',
    store: 'Amazon',
    price: 849.99
  },
  {
    date: 'Sep 5, 2026',
    store: 'Amazon',
    price: 819.99
  },
  {
    date: 'Sep 3, 2026',
    store: 'Amazon',
    price: 839.99
  },
  {
    date: 'Sep 1, 2026',
    store: 'Amazon',
    price: 859.99
  }
])

const prices = computed(() =>
  priceHistory.value.map(record => record.price)
)

const lowestPrice = computed(() =>
  Math.min(...prices.value)
)

const highestPrice = computed(() =>
  Math.max(...prices.value)
)

const averagePrice = computed(() =>
  prices.value.reduce((sum, price) => sum + price, 0) /
  prices.value.length
)

const priceChange = computed(() => {
  const first = prices.value[prices.value.length - 1]
  const current = prices.value[0]

  return ((current - first) / first) * 100
})

function refreshData() {
  console.log('Refreshing price history...')
}
</script>

<style scoped>
.price-history-page {
  padding: 32px;
  max-width: 1400px;
  margin: 0 auto;
  background: #f8fafc;
  min-height: 100vh;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 28px;
}

.page-header h1 {
  margin: 0;
  font-size: 30px;
  color: #111827;
}

.page-header p {
  margin-top: 6px;
  color: #6b7280;
}

.refresh-btn {
  border: none;
  padding: 11px 18px;
  border-radius: 8px;
  background: #111827;
  color: white;
  cursor: pointer;
  font-weight: 600;
}

.filter-card,
.product-card,
.chart-card,
.history-card,
.stat-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
}

.filter-card {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding: 22px;
  margin-bottom: 20px;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.filter-group label {
  font-size: 13px;
  font-weight: 600;
  color: #374151;
}

.filter-group select {
  padding: 11px;
  border: 1px solid #d1d5db;
  border-radius: 7px;
  background: white;
}

.product-card {
  padding: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.product-info {
  display: flex;
  align-items: center;
  gap: 16px;
}

.product-image {
  width: 55px;
  height: 55px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f3f4f6;
  border-radius: 10px;
  font-size: 25px;
}

.product-info h2 {
  margin: 0;
  font-size: 20px;
}

.product-info p {
  margin: 5px 0 0;
  color: #6b7280;
}

.current-price {
  text-align: right;
}

.current-price span,
.stat-card span {
  display: block;
  color: #6b7280;
  font-size: 13px;
}

.current-price strong {
  display: block;
  margin-top: 5px;
  font-size: 28px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-bottom: 20px;
}

.stat-card {
  padding: 22px;
}

.stat-card strong {
  display: block;
  margin: 8px 0;
  font-size: 24px;
}

.stat-card small {
  color: #9ca3af;
}

.increase {
  color: #dc2626;
}

.decrease {
  color: #16a34a;
}

.chart-card {
  padding: 24px;
  margin-bottom: 20px;
}

.chart-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 25px;
}

.chart-header h2,
.history-header h2 {
  margin: 0;
}

.chart-header p,
.history-header p {
  margin: 5px 0 0;
  color: #6b7280;
}

.chart-legend {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
}

.legend-line {
  width: 25px;
  height: 3px;
  background: currentColor;
}

.chart {
  display: flex;
  height: 330px;
}

.y-axis {
  width: 55px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding-bottom: 30px;
  color: #9ca3af;
  font-size: 12px;
}

.chart-area {
  position: relative;
  flex: 1;
}

.grid-line {
  position: absolute;
  left: 0;
  right: 0;
  border-top: 1px dashed #e5e7eb;
}

.line-1 {
  top: 0;
}

.line-2 {
  top: 25%;
}

.line-3 {
  top: 50%;
}

.line-4 {
  top: 75%;
}

.line-5 {
  top: 100%;
}

.price-chart {
  position: absolute;
  inset: 0 0 30px 0;
  width: 100%;
  height: calc(100% - 30px);
  color: #2563eb;
  overflow: visible;
}

.price-chart circle {
  fill: currentColor;
}

.x-axis {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  color: #9ca3af;
  font-size: 12px;
}

.history-card {
  padding: 24px;
}

.history-header {
  margin-bottom: 20px;
}

.table-wrapper {
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 15px;
  text-align: left;
  border-bottom: 1px solid #f0f0f0;
}

th {
  font-size: 12px;
  color: #6b7280;
  text-transform: uppercase;
}

.price {
  font-weight: 600;
}

.change {
  font-size: 13px;
  font-weight: 600;
}

.down {
  color: #16a34a;
}

.up {
  color: #dc2626;
}

.neutral {
  color: #6b7280;
}

@media (max-width: 900px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .filter-card {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 600px) {
  .price-history-page {
    padding: 18px;
  }

  .page-header,
  .product-card {
    align-items: flex-start;
    flex-direction: column;
    gap: 18px;
  }

  .current-price {
    text-align: left;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>