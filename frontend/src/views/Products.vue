<template>
  <div class="products-page">
    <!-- Header -->
    <div class="page-header">
      <div>
        <h1>Products</h1>
        <p>Monitor and track product prices across stores.</p>
      </div>

      <button class="add-btn" @click="showModal = true">
        + Add Product
      </button>
    </div>

    <!-- Stats -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon">📦</div>
        <div>
          <span>Total Products</span>
          <strong>{{ products.length }}</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">👁</div>
        <div>
          <span>Tracking</span>
          <strong>{{ trackedProducts }}</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">↓</div>
        <div>
          <span>Price Drops</span>
          <strong>{{ priceDrops }}</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">🔔</div>
        <div>
          <span>Alerts</span>
          <strong>{{ activeAlerts }}</strong>
        </div>
      </div>
    </div>

    <!-- Filters -->
    <div class="filters">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search products..."
      />

      <select v-model="selectedStore">
        <option value="">All Stores</option>
        <option
          v-for="store in stores"
          :key="store"
          :value="store"
        >
          {{ store }}
        </option>
      </select>
    </div>

    <!-- Products Table -->
    <div class="table-card">
      <div class="table-header">
        <h2>Tracked Products</h2>
        <span>{{ filteredProducts.length }} products</span>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Product</th>
              <th>Store</th>
              <th>Current Price</th>
              <th>Previous Price</th>
              <th>Change</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
          </thead>

          <tbody>
            <tr
              v-for="product in filteredProducts"
              :key="product.id"
            >
              <td>
                <div class="product-info">
                  <div class="product-image">
                    {{ product.name.charAt(0) }}
                  </div>

                  <div>
                    <strong>{{ product.name }}</strong>
                    <small>{{ product.category }}</small>
                  </div>
                </div>
              </td>

              <td>{{ product.store }}</td>

              <td>
                <strong>${{ product.currentPrice.toFixed(2) }}</strong>
              </td>

              <td>
                ${{ product.previousPrice.toFixed(2) }}
              </td>

              <td>
                <span
                  :class="[
                    'change',
                    product.change < 0 ? 'down' : 'up'
                  ]"
                >
                  {{ product.change > 0 ? '+' : '' }}{{ product.change }}%
                </span>
              </td>

              <td>
                <span
                  :class="[
                    'status',
                    product.tracking ? 'active' : 'paused'
                  ]"
                >
                  {{ product.tracking ? 'Tracking' : 'Paused' }}
                </span>
              </td>

              <td>
                <div class="actions">
                  <button
                    class="action-btn"
                    @click="viewProduct(product)"
                  >
                    View
                  </button>

                  <button
                    class="action-btn"
                    @click="toggleTracking(product)"
                  >
                    {{ product.tracking ? 'Pause' : 'Track' }}
                  </button>
                </div>
              </td>
            </tr>

            <tr v-if="filteredProducts.length === 0">
              <td colspan="7" class="empty">
                No products found.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Add Product Modal -->
    <div
      v-if="showModal"
      class="modal-overlay"
      @click.self="showModal = false"
    >
      <div class="modal">
        <div class="modal-header">
          <h2>Add Product</h2>

          <button
            class="close-btn"
            @click="showModal = false"
          >
            ×
          </button>
        </div>

        <form @submit.prevent="addProduct">
          <div class="form-group">
            <label>Product Name</label>
            <input
              v-model="newProduct.name"
              type="text"
              placeholder="Enter product name"
              required
            />
          </div>

          <div class="form-group">
            <label>Store</label>
            <select v-model="newProduct.store" required>
              <option value="">Select store</option>

              <option
                v-for="store in stores"
                :key="store"
                :value="store"
              >
                {{ store }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label>Current Price</label>
            <input
              v-model.number="newProduct.currentPrice"
              type="number"
              step="0.01"
              min="0"
              placeholder="0.00"
              required
            />
          </div>

          <div class="form-group">
            <label>Category</label>
            <input
              v-model="newProduct.category"
              type="text"
              placeholder="e.g. Electronics"
            />
          </div>

          <button type="submit" class="submit-btn">
            Add Product
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const stores = [
  'Amazon',
  'Walmart',
  'Best Buy',
  'eBay'
]

const products = ref([
  {
    id: 1,
    name: 'Apple AirPods Pro',
    category: 'Electronics',
    store: 'Amazon',
    currentPrice: 199.99,
    previousPrice: 229.99,
    change: -13.04,
    tracking: true
  },
  {
    id: 2,
    name: 'Samsung Galaxy S24',
    category: 'Smartphones',
    store: 'Walmart',
    currentPrice: 699.99,
    previousPrice: 749.99,
    change: -6.67,
    tracking: true
  },
  {
    id: 3,
    name: 'Sony WH-1000XM5',
    category: 'Headphones',
    store: 'Best Buy',
    currentPrice: 349.99,
    previousPrice: 329.99,
    change: 6.08,
    tracking: true
  },
  {
    id: 4,
    name: 'Logitech MX Master 3S',
    category: 'Computer Accessories',
    store: 'Amazon',
    currentPrice: 89.99,
    previousPrice: 99.99,
    change: -10.0,
    tracking: false
  },
  {
    id: 5,
    name: 'Nintendo Switch OLED',
    category: 'Gaming',
    store: 'eBay',
    currentPrice: 319.99,
    previousPrice: 319.99,
    change: 0,
    tracking: true
  }
])

const searchQuery = ref('')
const selectedStore = ref('')
const showModal = ref(false)

const newProduct = ref({
  name: '',
  store: '',
  currentPrice: 0,
  category: ''
})

const filteredProducts = computed(() => {
  return products.value.filter(product => {
    const matchesSearch =
      product.name
        .toLowerCase()
        .includes(searchQuery.value.toLowerCase())

    const matchesStore =
      !selectedStore.value ||
      product.store === selectedStore.value

    return matchesSearch && matchesStore
  })
})

const trackedProducts = computed(() => {
  return products.value.filter(
    product => product.tracking
  ).length
})

const priceDrops = computed(() => {
  return products.value.filter(
    product => product.change < 0
  ).length
})

const activeAlerts = computed(() => {
  return products.value.filter(
    product => product.change < -5
  ).length
})

function toggleTracking(product) {
  product.tracking = !product.tracking
}

function viewProduct(product) {
  console.log('Viewing product:', product)
}

function addProduct() {
  const product = {
    id: Date.now(),
    name: newProduct.value.name,
    category: newProduct.value.category || 'Other',
    store: newProduct.value.store,
    currentPrice: Number(newProduct.value.currentPrice),
    previousPrice: Number(newProduct.value.currentPrice),
    change: 0,
    tracking: true
  }

  products.value.push(product)

  newProduct.value = {
    name: '',
    store: '',
    currentPrice: 0,
    category: ''
  }

  showModal.value = false
}
</script>

<style scoped>
.products-page {
  min-height: 100vh;
  padding: 32px;
  background: #f8fafc;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 28px;
}

.page-header h1 {
  margin: 0 0 6px;
  font-size: 30px;
  color: #111827;
}

.page-header p {
  margin: 0;
  color: #6b7280;
}

.add-btn {
  border: none;
  background: #2563eb;
  color: white;
  padding: 12px 20px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
}

.add-btn:hover {
  background: #1d4ed8;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-bottom: 24px;
}

.stat-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 14px;
}

.stat-icon {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  background: #eff6ff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
}

.stat-card span {
  display: block;
  color: #6b7280;
  font-size: 13px;
  margin-bottom: 5px;
}

.stat-card strong {
  font-size: 22px;
  color: #111827;
}

.filters {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
}

.filters input,
.filters select {
  border: 1px solid #d1d5db;
  background: white;
  padding: 11px 14px;
  border-radius: 8px;
  font-size: 14px;
}

.filters input {
  width: 300px;
}

.filters select {
  min-width: 160px;
}

.table-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  overflow: hidden;
}

.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  border-bottom: 1px solid #e5e7eb;
}

.table-header h2 {
  margin: 0;
  font-size: 18px;
  color: #111827;
}

.table-header span {
  color: #6b7280;
  font-size: 14px;
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
  padding: 16px 20px;
  text-align: left;
  border-bottom: 1px solid #f1f5f9;
  white-space: nowrap;
}

th {
  background: #f8fafc;
  color: #6b7280;
  font-size: 12px;
  text-transform: uppercase;
}

td {
  color: #374151;
  font-size: 14px;
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
  background: #eff6ff;
  color: #2563eb;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
}

.product-info strong {
  display: block;
  color: #111827;
}

.product-info small {
  display: block;
  margin-top: 3px;
  color: #9ca3af;
}

.change {
  font-weight: 600;
}

.change.down {
  color: #16a34a;
}

.change.up {
  color: #dc2626;
}

.status {
  display: inline-block;
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.status.active {
  background: #dcfce7;
  color: #15803d;
}

.status.paused {
  background: #f3f4f6;
  color: #6b7280;
}

.actions {
  display: flex;
  gap: 8px;
}

.action-btn {
  border: 1px solid #d1d5db;
  background: white;
  padding: 7px 10px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 12px;
}

.action-btn:hover {
  background: #f8fafc;
}

.empty {
  text-align: center;
  padding: 40px;
  color: #9ca3af;
}

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  width: 420px;
  max-width: calc(100% - 30px);
  background: white;
  border-radius: 12px;
  padding: 24px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 22px;
}

.modal-header h2 {
  margin: 0;
}

.close-btn {
  border: none;
  background: none;
  font-size: 26px;
  cursor: pointer;
  color: #6b7280;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  margin-bottom: 7px;
  font-size: 14px;
  font-weight: 600;
  color: #374151;
}

.form-group input,
.form-group select {
  width: 100%;
  box-sizing: border-box;
  padding: 11px 12px;
  border: 1px solid #d1d5db;
  border-radius: 7px;
  font-size: 14px;
}

.submit-btn {
  width: 100%;
  border: none;
  background: #2563eb;
  color: white;
  padding: 12px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  margin-top: 5px;
}

.submit-btn:hover {
  background: #1d4ed8;
}

@media (max-width: 900px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .products-page {
    padding: 20px;
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .filters {
    flex-direction: column;
  }

  .filters input {
    width: auto;
  }
}
</style>