<template>
  <div class="users-page">

    <!-- Page Header -->
    <div class="page-header">
      <div>
        <h1>Users</h1>
        <p>Manage users and their access to PriceTrack.</p>
      </div>

      <button class="add-user-btn" @click="openAddUser">
        + Add User
      </button>
    </div>

    <!-- Stats -->
    <div class="stats-grid">
      <div class="stat-card">
        <span>Total Users</span>
        <strong>{{ users.length }}</strong>
      </div>

      <div class="stat-card">
        <span>Active Users</span>
        <strong>{{ activeUsers }}</strong>
      </div>

      <div class="stat-card">
        <span>Administrators</span>
        <strong>{{ adminUsers }}</strong>
      </div>

      <div class="stat-card">
        <span>Inactive Users</span>
        <strong>{{ inactiveUsers }}</strong>
      </div>
    </div>

    <!-- Users Card -->
    <div class="users-card">

      <!-- Toolbar -->
      <div class="users-toolbar">

        <div class="search-box">
          <span>⌕</span>

          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search users..."
          />
        </div>

        <select v-model="roleFilter">
          <option value="all">All Roles</option>
          <option value="Admin">Admin</option>
          <option value="User">User</option>
        </select>

        <select v-model="statusFilter">
          <option value="all">All Status</option>
          <option value="Active">Active</option>
          <option value="Inactive">Inactive</option>
        </select>

      </div>

      <!-- Table -->
      <div class="table-wrapper">

        <table>

          <thead>
            <tr>
              <th>User</th>
              <th>Email</th>
              <th>Role</th>
              <th>Status</th>
              <th>Joined</th>
              <th>Actions</th>
            </tr>
          </thead>

          <tbody>

            <tr
              v-for="user in filteredUsers"
              :key="user.id"
            >

              <td>
                <div class="user-info">

                  <div class="avatar">
                    {{ getInitials(user.name) }}
                  </div>

                  <div>
                    <strong>{{ user.name }}</strong>
                  </div>

                </div>
              </td>

              <td class="email">
                {{ user.email }}
              </td>

              <td>
                <span
                  :class="[
                    'role-badge',
                    user.role.toLowerCase()
                  ]"
                >
                  {{ user.role }}
                </span>
              </td>

              <td>
                <span
                  :class="[
                    'status-badge',
                    user.status.toLowerCase()
                  ]"
                >
                  <span class="status-dot"></span>
                  {{ user.status }}
                </span>
              </td>

              <td>
                {{ user.joined }}
              </td>

              <td>
                <div class="actions">

                  <button
                    class="action-btn"
                    @click="editUser(user)"
                  >
                    Edit
                  </button>

                  <button
                    class="delete-btn"
                    @click="deleteUser(user.id)"
                  >
                    Delete
                  </button>

                </div>
              </td>

            </tr>

            <tr v-if="filteredUsers.length === 0">
              <td colspan="6" class="empty-state">
                No users found.
              </td>
            </tr>

          </tbody>

        </table>

      </div>

    </div>

    <!-- Add / Edit Modal -->
    <div
      v-if="showModal"
      class="modal-overlay"
      @click.self="closeModal"
    >

      <div class="modal">

        <div class="modal-header">
          <div>
            <h2>
              {{ editingUser ? 'Edit User' : 'Add User' }}
            </h2>

            <p>
              {{
                editingUser
                  ? 'Update user information.'
                  : 'Create a new PriceTrack user.'
              }}
            </p>
          </div>

          <button
            class="close-btn"
            @click="closeModal"
          >
            ×
          </button>
        </div>

        <form @submit.prevent="saveUser">

          <div class="form-group">
            <label>Name</label>

            <input
              v-model="form.name"
              type="text"
              placeholder="Enter full name"
              required
            />
          </div>

          <div class="form-group">
            <label>Email</label>

            <input
              v-model="form.email"
              type="email"
              placeholder="Enter email address"
              required
            />
          </div>

          <div class="form-row">

            <div class="form-group">
              <label>Role</label>

              <select v-model="form.role">
                <option value="User">User</option>
                <option value="Admin">Admin</option>
              </select>
            </div>

            <div class="form-group">
              <label>Status</label>

              <select v-model="form.status">
                <option value="Active">Active</option>
                <option value="Inactive">Inactive</option>
              </select>
            </div>

          </div>

          <div class="modal-actions">

            <button
              type="button"
              class="cancel-btn"
              @click="closeModal"
            >
              Cancel
            </button>

            <button
              type="submit"
              class="save-btn"
            >
              {{ editingUser ? 'Save Changes' : 'Add User' }}
            </button>

          </div>

        </form>

      </div>

    </div>

  </div>
</template>

<script setup>
import { computed, reactive, ref } from 'vue'

const searchQuery = ref('')
const roleFilter = ref('all')
const statusFilter = ref('all')

const showModal = ref(false)
const editingUser = ref(null)

const users = ref([
  {
    id: 1,
    name: 'John Doe',
    email: 'john@example.com',
    role: 'Admin',
    status: 'Active',
    joined: 'Sep 01, 2026'
  },
  {
    id: 2,
    name: 'Sara Ali',
    email: 'sara@example.com',
    role: 'User',
    status: 'Active',
    joined: 'Sep 03, 2026'
  },
  {
    id: 3,
    name: 'Michael John',
    email: 'michael@example.com',
    role: 'User',
    status: 'Inactive',
    joined: 'Aug 28, 2026'
  },
  {
    id: 4,
    name: 'David Smith',
    email: 'david@example.com',
    role: 'User',
    status: 'Active',
    joined: 'Aug 25, 2026'
  }
])

const form = reactive({
  name: '',
  email: '',
  role: 'User',
  status: 'Active'
})

const filteredUsers = computed(() => {
  return users.value.filter(user => {

    const matchesSearch =
      user.name.toLowerCase().includes(
        searchQuery.value.toLowerCase()
      ) ||
      user.email.toLowerCase().includes(
        searchQuery.value.toLowerCase()
      )

    const matchesRole =
      roleFilter.value === 'all' ||
      user.role === roleFilter.value

    const matchesStatus =
      statusFilter.value === 'all' ||
      user.status === statusFilter.value

    return (
      matchesSearch &&
      matchesRole &&
      matchesStatus
    )
  })
})

const activeUsers = computed(() =>
  users.value.filter(
    user => user.status === 'Active'
  ).length
)

const inactiveUsers = computed(() =>
  users.value.filter(
    user => user.status === 'Inactive'
  ).length
)

const adminUsers = computed(() =>
  users.value.filter(
    user => user.role === 'Admin'
  ).length
)

function getInitials(name) {
  return name
    .split(' ')
    .map(word => word[0])
    .join('')
    .substring(0, 2)
    .toUpperCase()
}

function openAddUser() {
  editingUser.value = null

  form.name = ''
  form.email = ''
  form.role = 'User'
  form.status = 'Active'

  showModal.value = true
}

function editUser(user) {
  editingUser.value = user

  form.name = user.name
  form.email = user.email
  form.role = user.role
  form.status = user.status

  showModal.value = true
}

function saveUser() {

  if (editingUser.value) {

    Object.assign(
      editingUser.value,
      {
        name: form.name,
        email: form.email,
        role: form.role,
        status: form.status
      }
    )

  } else {

    users.value.push({
      id: Date.now(),
      name: form.name,
      email: form.email,
      role: form.role,
      status: form.status,
      joined: new Date().toLocaleDateString(
        'en-US',
        {
          month: 'short',
          day: '2-digit',
          year: 'numeric'
        }
      )
    })

  }

  closeModal()
}

function deleteUser(id) {
  const confirmed = window.confirm(
    'Are you sure you want to delete this user?'
  )

  if (!confirmed) return

  users.value = users.value.filter(
    user => user.id !== id
  )
}

function closeModal() {
  showModal.value = false
  editingUser.value = null
}
</script>

<style scoped>

.users-page {
  min-height: 100vh;
  padding: 48px;
  background: #f8fafc;
  font-family: Georgia, 'Times New Roman', serif;
  color: #111827;
}

/* Header */

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 32px;
}

.page-header h1 {
  margin: 0;
  font-size: 42px;
  font-weight: 700;
}

.page-header p {
  margin: 8px 0 0;
  color: #64748b;
  font-size: 18px;
}

.add-user-btn {
  border: none;
  background: #2563eb;
  color: white;
  padding: 13px 20px;
  border-radius: 8px;
  font-family: inherit;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
}

.add-user-btn:hover {
  background: #1d4ed8;
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
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 24px;
}

.stat-card span {
  color: #64748b;
  font-size: 14px;
}

.stat-card strong {
  display: block;
  margin-top: 8px;
  font-size: 30px;
}

/* Main card */

.users-card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  overflow: hidden;
}

/* Toolbar */

.users-toolbar {
  display: flex;
  gap: 14px;
  padding: 20px;
  border-bottom: 1px solid #e5e7eb;
}

.search-box {
  flex: 1;
  max-width: 420px;
  display: flex;
  align-items: center;
  gap: 10px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  padding: 0 14px;
}

.search-box span {
  color: #64748b;
  font-size: 22px;
}

.search-box input {
  width: 100%;
  border: none;
  outline: none;
  padding: 12px 0;
  font-family: inherit;
  font-size: 15px;
}

.users-toolbar select {
  border: 1px solid #d1d5db;
  border-radius: 8px;
  padding: 0 14px;
  background: white;
  font-family: inherit;
  font-size: 14px;
}

/* Table */

.table-wrapper {
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th {
  padding: 16px 20px;
  text-align: left;
  background: #f8fafc;
  color: #64748b;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

td {
  padding: 18px 20px;
  border-top: 1px solid #f1f5f9;
  font-size: 14px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #dbeafe;
  color: #2563eb;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 13px;
}

.email {
  color: #64748b;
}

/* Badges */

.role-badge,
.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.role-badge.admin {
  background: #ede9fe;
  color: #6d28d9;
}

.role-badge.user {
  background: #eff6ff;
  color: #2563eb;
}

.status-badge.active {
  background: #f0fdf4;
  color: #15803d;
}

.status-badge.inactive {
  background: #fef2f2;
  color: #dc2626;
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: currentColor;
}

/* Actions */

.actions {
  display: flex;
  gap: 8px;
}

.action-btn,
.delete-btn {
  border: none;
  background: none;
  cursor: pointer;
  font-family: inherit;
  font-weight: 600;
  font-size: 13px;
}

.action-btn {
  color: #2563eb;
}

.delete-btn {
  color: #dc2626;
}

/* Empty */

.empty-state {
  text-align: center;
  padding: 50px;
  color: #64748b;
}

/* Modal */

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  width: 500px;
  max-width: calc(100% - 30px);
  background: white;
  border-radius: 14px;
  padding: 28px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 25px;
}

.modal-header h2 {
  margin: 0;
  font-size: 26px;
}

.modal-header p {
  margin: 5px 0 0;
  color: #64748b;
}

.close-btn {
  border: none;
  background: none;
  font-size: 28px;
  cursor: pointer;
  color: #64748b;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 7px;
  margin-bottom: 18px;
}

.form-group label {
  font-size: 13px;
  font-weight: 600;
}

.form-group input,
.form-group select {
  padding: 12px;
  border: 1px solid #d1d5db;
  border-radius: 7px;
  outline: none;
  font-family: inherit;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 25px;
}

.cancel-btn,
.save-btn {
  padding: 11px 18px;
  border-radius: 7px;
  font-family: inherit;
  font-weight: 600;
  cursor: pointer;
}

.cancel-btn {
  background: white;
  border: 1px solid #d1d5db;
}

.save-btn {
  border: none;
  background: #2563eb;
  color: white;
}

/* Responsive */

@media (max-width: 900px) {

  .users-page {
    padding: 25px;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

}

@media (max-width: 600px) {

  .page-header {
    flex-direction: column;
    gap: 15px;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .users-toolbar {
    flex-direction: column;
  }

  .search-box {
    max-width: none;
  }

  .users-toolbar select {
    min-height: 42px;
  }

  .form-row {
    grid-template-columns: 1fr;
  }

}

</style>