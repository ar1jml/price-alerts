<template>
  <div class="stores-page">

    <!-- Page Header -->
    <div class="page-header">
      <div>
        <h1>Stores</h1>
        <p>Manage the stores you're monitoring for product prices.</p>
      </div>

      <button class="add-store-button" @click="openAddModal">
        <span>+</span>
        Add Store
      </button>
    </div>

    <!-- Stats -->
    <div class="stats-grid">

      <div class="stat-card">
        <div class="stat-icon">🏪</div>

        <div>
          <span>Total Stores</span>
          <strong>{{ stores.length }}</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">✓</div>

        <div>
          <span>Active Stores</span>
          <strong>{{ activeStores }}</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">📦</div>

        <div>
          <span>Products Monitored</span>
          <strong>{{ totalProducts }}</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">🔄</div>

        <div>
          <span>Recent Updates</span>
          <strong>{{ recentUpdates }}</strong>
        </div>
      </div>

    </div>

    <!-- Store List -->
    <div class="stores-card">

      <!-- Card Header -->
      <div class="card-header">
        <div>
          <h2>Monitored Stores</h2>
          <p>Stores currently connected to PriceTrack.</p>
        </div>

        <div class="store-count">
          {{ filteredStores.length }} stores
        </div>
      </div>

      <!-- Search and Filter -->
      <div class="filters">

        <div class="search-box">
          <span>⌕</span>

          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search stores..."
          />
        </div>

        <select v-model="statusFilter">
          <option value="All">All Status</option>
          <option value="Active">Active</option>
          <option value="Inactive">Inactive</option>
        </select>

      </div>

      <!-- Table -->
      <div class="table-wrapper">

        <table>

          <thead>
            <tr>
              <th>Store</th>
              <th>Status</th>
              <th>Products</th>
              <th>Last Update</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>

            <tr
              v-for="store in filteredStores"
              :key="store.id"
            >

              <!-- Store -->
              <td>
                <div class="store-info">

                  <div class="store-logo">
                    {{ store.name.charAt(0) }}
                  </div>

                  <div>
                    <strong>{{ store.name }}</strong>
                    <span>{{ store.website }}</span>
                  </div>

                </div>
              </td>

              <!-- Status -->
              <td>
                <span
                  class="status"
                  :class="store.status.toLowerCase()"
                >
                  <span class="status-dot"></span>
                  {{ store.status }}
                </span>
              </td>

              <!-- Products -->
              <td>
                <span class="product-number">
                  {{ store.products }}
                </span>
              </td>

              <!-- Last Update -->
              <td>
                <span class="last-update">
                  {{ store.lastUpdate }}
                </span>
              </td>

              <!-- Actions -->
              <td>
                <div class="actions">

                  <button
                    class="action-button"
                    title="Edit"
                    @click="editStore(store)"
                  >
                    ✎
                  </button>

                  <button
                    class="action-button delete"
                    title="Delete"
                    @click="deleteStore(store.id)"
                  >
                    🗑
                  </button>

                </div>
              </td>

            </tr>

            <!-- Empty State -->
            <tr v-if="filteredStores.length === 0">
              <td colspan="5">
                <div class="empty-state">
                  <div>🏪</div>
                  <h3>No stores found</h3>
                  <p>Try changing your search or filter.</p>
                </div>
              </td>
            </tr>

          </tbody>

        </table>

      </div>

    </div>

    <!-- Add/Edit Store Modal -->
    <div
      v-if="showModal"
      class="modal-overlay"
      @click.self="closeModal"
    >

      <div class="modal">

        <div class="modal-header">
          <div>
            <h2>
              {{ editingStore ? 'Edit Store' : 'Add Store' }}
            </h2>

            <p>
              {{
                editingStore
                  ? 'Update the store information.'
                  : 'Add a store to start monitoring prices.'
              }}
            </p>
          </div>

          <button
            class="close-button"
            @click="closeModal"
          >
            ×
          </button>
        </div>

        <form @submit.prevent="saveStore">

          <div class="form-group">
            <label>Store Name</label>

            <input
              v-model="form.name"
              type="text"
              placeholder="e.g. Amazon"
              required
            />
          </div>

          <div class="form-group">
            <label>Website</label>

            <input
              v-model="form.website"
              type="text"
              placeholder="e.g. amazon.com"
              required
            />
          </div>

          <div class="form-group">
            <label>Status</label>

            <select v-model="form.status">
              <option value="Active">Active</option>
              <option value="Inactive">Inactive</option>
            </select>
          </div>

          <div class="modal-actions">

            <button
              type="button"
              class="cancel-button"
              @click="closeModal"
            >
              Cancel
            </button>

            <button
              type="submit"
              class="save-button"
            >
              {{ editingStore ? 'Save Changes' : 'Add Store' }}
            </button>

          </div>

        </form>

      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const searchQuery = ref('')
const statusFilter = ref('All')

const showModal = ref(false)
const editingStore = ref(null)

const stores = ref([
  {
    id: 1,
    name: 'Amazon',
    website: 'amazon.com',
    status: 'Active',
    products: 18,
    lastUpdate: '5 minutes ago'
  },
  {
    id: 2,
    name: 'Walmart',
    website: 'walmart.com',
    status: 'Active',
    products: 12,
    lastUpdate: '12 minutes ago'
  },
  {
    id: 3,
    name: 'Best Buy',
    website: 'bestbuy.com',
    status: 'Active',
    products: 9,
    lastUpdate: '25 minutes ago'
  },
  {
    id: 4,
    name: 'Target',
    website: 'target.com',
    status: 'Inactive',
    products: 5,
    lastUpdate: '2 days ago'
  },
  {
    id: 5,
    name: 'eBay',
    website: 'ebay.com',
    status: 'Active',
    products: 7,
    lastUpdate: '35 minutes ago'
  }
])

const form = ref({
  name: '',
  website: '',
  status: 'Active'
})

const filteredStores = computed(() => {
  return stores.value.filter(store => {

    const matchesSearch =
      store.name
        .toLowerCase()
        .includes(searchQuery.value.toLowerCase()) ||
      store.website
        .toLowerCase()
        .includes(searchQuery.value.toLowerCase())

    const matchesStatus =
      statusFilter.value === 'All' ||
      store.status === statusFilter.value

    return matchesSearch && matchesStatus
  })
})

const activeStores = computed(() => {
  return stores.value.filter(
    store => store.status === 'Active'
  ).length
})

const totalProducts = computed(() => {
  return stores.value.reduce(
    (total, store) => total + store.products,
    0
  )
})

const recentUpdates = computed(() => {
  return stores.value.filter(
    store => store.lastUpdate.includes('minute')
  ).length
})

function openAddModal() {
  editingStore.value = null

  form.value = {
    name: '',
    website: '',
    status: 'Active'
  }

  showModal.value = true
}

function editStore(store) {
  editingStore.value = store

  form.value = {
    name: store.name,
    website: store.website,
    status: store.status
  }

  showModal.value = true
}

function saveStore() {
  if (editingStore.value) {

    editingStore.value.name = form.value.name
    editingStore.value.website = form.value.website
    editingStore.value.status = form.value.status

  } else {

    stores.value.push({
      id: Date.now(),
      name: form.value.name,
      website: form.value.website,
      status: form.value.status,
      products: 0,
      lastUpdate: 'Just now'
    })

  }

  closeModal()
}

function deleteStore(id) {
  const confirmed = window.confirm(
    'Are you sure you want to delete this store?'
  )

  if (!confirmed) return

  stores.value = stores.value.filter(
    store => store.id !== id
  )
}

function closeModal() {
  showModal.value = false
  editingStore.value = null
}
</script>

<style scoped>
.stores-page {
  width: 100%;
}

/* PAGE HEADER */

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

.add-store-button {
  display: flex;
  align-items: center;
  gap: 8px;

  padding: 10px 16px;

  border: none;
  border-radius: 8px;

  background: #2563eb;
  color: white;

  font-size: 14px;
  font-weight: 600;

  cursor: pointer;
}

.add-store-button:hover {
  background: #1d4ed8;
}

.add-store-button span {
  font-size: 19px;
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

  font-size: 20px;
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

/* STORE CARD */

.stores-card {
  background: white;

  border: 1px solid #e5e7eb;

  border-radius: 12px;

  overflow: hidden;
}

.card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;

  padding: 20px;

  border-bottom: 1px solid #e5e7eb;
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

.store-count {
  color: #6b7280;

  font-size: 13px;
}

/* FILTERS */

.filters {
  display: flex;

  align-items: center;

  gap: 12px;

  padding: 18px 20px;

  border-bottom: 1px solid #e5e7eb;
}

.search-box {
  position: relative;

  flex: 1;

  max-width: 400px;
}

.search-box span {
  position: absolute;

  left: 13px;
  top: 50%;

  transform: translateY(-50%);

  color: #9ca3af;

  font-size: 18px;
}

.search-box input {
  width: 100%;
  height: 40px;

  box-sizing: border-box;

  padding: 0 15px 0 38px;

  border: 1px solid #d1d5db;

  border-radius: 8px;

  outline: none;

  font-size: 14px;
}

.search-box input:focus {
  border-color: #2563eb;
}

.filters select {
  height: 40px;

  padding: 0 12px;

  border: 1px solid #d1d5db;

  border-radius: 8px;

  background: white;

  color: #374151;

  outline: none;

  font-size: 14px;
}

/* TABLE */

.table-wrapper {
  overflow-x: auto;
}

table {
  width: 100%;

  border-collapse: collapse;

  min-width: 700px;
}

thead {
  background: #f9fafb;
}

th {
  padding: 13px 20px;

  text-align: left;

  color: #6b7280;

  font-size: 12px;

  font-weight: 600;

  text-transform: uppercase;

  letter-spacing: 0.03em;
}

td {
  padding: 16px 20px;

  border-top: 1px solid #f3f4f6;

  color: #374151;

  font-size: 14px;
}

tbody tr:hover {
  background: #fafafa;
}

/* STORE */

.store-info {
  display: flex;

  align-items: center;

  gap: 12px;
}

.store-logo {
  width: 42px;
  height: 42px;

  border-radius: 9px;

  background: #f3f4f6;

  display: flex;
  align-items: center;
  justify-content: center;

  color: #374151;

  font-weight: 700;
}

.store-info strong {
  display: block;

  color: #111827;

  font-size: 14px;
}

.store-info span {
  display: block;

  margin-top: 3px;

  color: #6b7280;

  font-size: 12px;
}

/* STATUS */

.status {
  display: inline-flex;

  align-items: center;

  gap: 7px;

  padding: 5px 9px;

  border-radius: 20px;

  font-size: 12px;

  font-weight: 600;
}

.status.active {
  background: #ecfdf5;
  color: #047857;
}

.status.inactive {
  background: #f3f4f6;
  color: #6b7280;
}

.status-dot {
  width: 6px;
  height: 6px;

  border-radius: 50%;

  background: currentColor;
}

.product-number {
  font-weight: 600;

  color: #111827;
}

.last-update {
  color: #6b7280;

  font-size: 13px;
}

/* ACTIONS */

.actions {
  display: flex;

  gap: 7px;
}

.action-button {
  width: 34px;
  height: 34px;

  border: 1px solid #e5e7eb;

  border-radius: 7px;

  background: white;

  cursor: pointer;

  color: #4b5563;
}

.action-button:hover {
  background: #f3f4f6;
}

.action-button.delete:hover {
  color: #dc2626;
  border-color: #fecaca;
  background: #fef2f2;
}

/* EMPTY */

.empty-state {
  text-align: center;

  padding: 50px 20px;
}

.empty-state > div {
  font-size: 35px;

  margin-bottom: 10px;
}

.empty-state h3 {
  margin: 0 0 5px;

  color: #111827;
}

.empty-state p {
  margin: 0;

  color: #6b7280;

  font-size: 14px;
}

/* MODAL */

.modal-overlay {
  position: fixed;

  inset: 0;

  background: rgba(17, 24, 39, 0.45);

  display: flex;

  align-items: center;
  justify-content: center;

  padding: 20px;

  z-index: 2000;
}

.modal {
  width: 100%;
  max-width: 480px;

  background: white;

  border-radius: 14px;

  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
}

.modal-header {
  display: flex;

  justify-content: space-between;
  align-items: flex-start;

  padding: 22px;

  border-bottom: 1px solid #e5e7eb;
}

.modal-header h2 {
  margin: 0 0 5px;

  font-size: 20px;

  color: #111827;
}

.modal-header p {
  margin: 0;

  color: #6b7280;

  font-size: 13px;
}

.close-button {
  border: none;

  background: transparent;

  font-size: 25px;

  color: #6b7280;

  cursor: pointer;
}

.modal form {
  padding: 22px;
}

.form-group {
  margin-bottom: 18px;
}

.form-group label {
  display: block;

  margin-bottom: 7px;

  color: #374151;

  font-size: 13px;

  font-weight: 600;
}

.form-group input,
.form-group select {
  width: 100%;

  height: 42px;

  box-sizing: border-box;

  padding: 0 12px;

  border: 1px solid #d1d5db;

  border-radius: 8px;

  outline: none;

  font-size: 14px;

  background: white;
}

.form-group input:focus,
.form-group select:focus {
  border-color: #2563eb;
}

.modal-actions {
  display: flex;

  justify-content: flex-end;

  gap: 10px;

  margin-top: 24px;
}

.cancel-button,
.save-button {
  padding: 10px 16px;

  border-radius: 8px;

  font-size: 14px;

  font-weight: 600;

  cursor: pointer;
}

.cancel-button {
  border: 1px solid #d1d5db;

  background: white;

  color: #374151;
}

.save-button {
  border: none;

  background: #2563eb;

  color: white;
}

.save-button:hover {
  background: #1d4ed8;
}

/* RESPONSIVE */

@media (max-width: 1100px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 700px) {

  .page-header {
    flex-direction: column;

    gap: 15px;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .filters {
    flex-direction: column;
    align-items: stretch;
  }

  .search-box {
    max-width: none;
  }

  .filters select {
    width: 100%;
  }
}
</style>