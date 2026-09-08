<template>
  <div class="alerts-page">

    <!-- Page Header -->
    <div class="page-header">
      <div>
        <h1>Alerts</h1>
        <p>Stay updated when product prices change.</p>
      </div>

      <button class="mark-all-btn" @click="markAllAsRead">
        Mark all as read
      </button>
    </div>

    <!-- Alert Summary -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon warning">!</div>
        <div>
          <span>Active Alerts</span>
          <strong>{{ activeAlerts }}</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon drop">↓</div>
        <div>
          <span>Price Drops</span>
          <strong>{{ priceDrops }}</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon increase">↑</div>
        <div>
          <span>Price Increases</span>
          <strong>{{ priceIncreases }}</strong>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon read">✓</div>
        <div>
          <span>Read Alerts</span>
          <strong>{{ readAlerts }}</strong>
        </div>
      </div>
    </div>

    <!-- Filters -->
    <div class="filters-card">
      <div class="filter-group">
        <label>Filter</label>

        <select v-model="selectedFilter">
          <option value="all">All Alerts</option>
          <option value="unread">Unread</option>
          <option value="read">Read</option>
          <option value="drop">Price Drops</option>
          <option value="increase">Price Increases</option>
        </select>
      </div>
    </div>

    <!-- Alerts List -->
    <div class="alerts-card">

      <div class="alerts-header">
        <h2>Recent Alerts</h2>
        <span>{{ filteredAlerts.length }} alerts</span>
      </div>

      <div
        v-for="alert in filteredAlerts"
        :key="alert.id"
        :class="[
          'alert-item',
          { unread: !alert.read }
        ]"
      >

        <!-- Alert Icon -->
        <div
          :class="[
            'alert-icon',
            alert.type
          ]"
        >
          <span v-if="alert.type === 'drop'">↓</span>
          <span v-else>↑</span>
        </div>

        <!-- Alert Content -->
        <div class="alert-content">

          <div class="alert-title-row">
            <h3>{{ alert.product }}</h3>

            <span
              v-if="!alert.read"
              class="unread-badge"
            >
              New
            </span>
          </div>

          <p>{{ alert.message }}</p>

          <div class="alert-meta">
            <span>{{ alert.store }}</span>
            <span>•</span>
            <span>{{ alert.time }}</span>
          </div>

        </div>

        <!-- Price -->
        <div class="alert-price">
          <strong>${{ alert.price.toFixed(2) }}</strong>

          <span
            :class="[
              'percentage',
              alert.type
            ]"
          >
            {{ alert.type === 'drop' ? '-' : '+' }}{{ alert.percentage }}%
          </span>
        </div>

        <!-- Action -->
        <button
          class="read-btn"
          @click="toggleRead(alert)"
        >
          {{ alert.read ? 'Unread' : 'Mark read' }}
        </button>

      </div>

      <!-- Empty State -->
      <div
        v-if="filteredAlerts.length === 0"
        class="empty-state"
      >
        <div class="empty-icon">🔔</div>
        <h3>No alerts found</h3>
        <p>There are no alerts matching your current filter.</p>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const selectedFilter = ref('all')

const alerts = ref([
  {
    id: 1,
    product: 'Apple AirPods Pro',
    store: 'Amazon',
    type: 'drop',
    price: 199.99,
    percentage: 13.04,
    message: 'Price dropped from $229.99 to $199.99',
    time: '10 minutes ago',
    read: false
  },
  {
    id: 2,
    product: 'Samsung Galaxy S24',
    store: 'Walmart',
    type: 'drop',
    price: 699.99,
    percentage: 6.67,
    message: 'Price dropped from $749.99 to $699.99',
    time: '35 minutes ago',
    read: false
  },
  {
    id: 3,
    product: 'Sony WH-1000XM5',
    store: 'Best Buy',
    type: 'increase',
    price: 349.99,
    percentage: 6.08,
    message: 'Price increased from $329.99 to $349.99',
    time: '1 hour ago',
    read: true
  },
  {
    id: 4,
    product: 'Logitech MX Master 3S',
    store: 'Amazon',
    type: 'drop',
    price: 89.99,
    percentage: 10,
    message: 'Price dropped from $99.99 to $89.99',
    time: '2 hours ago',
    read: false
  },
  {
    id: 5,
    product: 'Nintendo Switch OLED',
    store: 'eBay',
    type: 'increase',
    price: 319.99,
    percentage: 4.5,
    message: 'Price increased from $306.20 to $319.99',
    time: '3 hours ago',
    read: true
  }
])

const filteredAlerts = computed(() => {
  if (selectedFilter.value === 'unread') {
    return alerts.value.filter(alert => !alert.read)
  }

  if (selectedFilter.value === 'read') {
    return alerts.value.filter(alert => alert.read)
  }

  if (selectedFilter.value === 'drop') {
    return alerts.value.filter(alert => alert.type === 'drop')
  }

  if (selectedFilter.value === 'increase') {
    return alerts.value.filter(alert => alert.type === 'increase')
  }

  return alerts.value
})

const activeAlerts = computed(() => {
  return alerts.value.filter(alert => !alert.read).length
})

const priceDrops = computed(() => {
  return alerts.value.filter(alert => alert.type === 'drop').length
})

const priceIncreases = computed(() => {
  return alerts.value.filter(alert => alert.type === 'increase').length
})

const readAlerts = computed(() => {
  return alerts.value.filter(alert => alert.read).length
})

function toggleRead(alert) {
  alert.read = !alert.read
}

function markAllAsRead() {
  alerts.value.forEach(alert => {
    alert.read = true
  })
}
</script>

<style scoped>
.alerts-page {
  min-height: 100vh;
  padding: 32px;
  background: #f8fafc;
}

/* Header */

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

.mark-all-btn {
  border: 1px solid #d1d5db;
  background: white;
  color: #374151;
  padding: 11px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
}

.mark-all-btn:hover {
  background: #f9fafb;
}

/* Stats */

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
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-weight: bold;
}

.stat-icon.warning {
  background: #fef3c7;
  color: #d97706;
}

.stat-icon.drop {
  background: #dcfce7;
  color: #16a34a;
}

.stat-icon.increase {
  background: #fee2e2;
  color: #dc2626;
}

.stat-icon.read {
  background: #eff6ff;
  color: #2563eb;
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

/* Filters */

.filters-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 18px;
  margin-bottom: 20px;
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 12px;
}

.filter-group label {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
}

.filter-group select {
  padding: 9px 12px;
  border: 1px solid #d1d5db;
  border-radius: 7px;
  background: white;
}

/* Alerts */

.alerts-card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  overflow: hidden;
}

.alerts-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  border-bottom: 1px solid #e5e7eb;
}

.alerts-header h2 {
  margin: 0;
  font-size: 18px;
  color: #111827;
}

.alerts-header span {
  color: #6b7280;
  font-size: 14px;
}

/* Alert Item */

.alert-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px;
  border-bottom: 1px solid #f1f5f9;
}

.alert-item:last-child {
  border-bottom: none;
}

.alert-item.unread {
  background: #f8fbff;
}

.alert-icon {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  font-weight: bold;
  flex-shrink: 0;
}

.alert-icon.drop {
  background: #dcfce7;
  color: #16a34a;
}

.alert-icon.increase {
  background: #fee2e2;
  color: #dc2626;
}

/* Content */

.alert-content {
  flex: 1;
  min-width: 0;
}

.alert-title-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.alert-title-row h3 {
  margin: 0;
  font-size: 15px;
  color: #111827;
}

.unread-badge {
  background: #dbeafe;
  color: #2563eb;
  padding: 3px 7px;
  border-radius: 10px;
  font-size: 10px;
  font-weight: 700;
}

.alert-content p {
  margin: 5px 0;
  color: #6b7280;
  font-size: 13px;
}

.alert-meta {
  display: flex;
  gap: 7px;
  color: #9ca3af;
  font-size: 12px;
}

/* Price */

.alert-price {
  min-width: 110px;
  text-align: right;
}

.alert-price strong {
  display: block;
  color: #111827;
  font-size: 15px;
}

.percentage {
  font-size: 12px;
  font-weight: 600;
}

.percentage.drop {
  color: #16a34a;
}

.percentage.increase {
  color: #dc2626;
}

/* Button */

.read-btn {
  border: 1px solid #d1d5db;
  background: white;
  padding: 8px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 12px;
  color: #374151;
}

.read-btn:hover {
  background: #f8fafc;
}

/* Empty */

.empty-state {
  text-align: center;
  padding: 60px 20px;
}

.empty-icon {
  font-size: 40px;
  margin-bottom: 10px;
}

.empty-state h3 {
  margin: 0 0 6px;
  color: #111827;
}

.empty-state p {
  margin: 0;
  color: #9ca3af;
}

/* Responsive */

@media (max-width: 1000px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 700px) {
  .alerts-page {
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

  .alert-item {
    flex-wrap: wrap;
  }

  .alert-price {
    text-align: left;
    margin-left: 60px;
  }

  .read-btn {
    margin-left: 60px;
  }
}
</style>