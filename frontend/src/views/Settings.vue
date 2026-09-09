<template>
  <div class="settings-page">
    <!-- Page Header -->
    <div class="page-header">
      <div>
        <h1>Settings</h1>
        <p>Manage your account and application preferences.</p>
      </div>
    </div>

    <!-- Profile Settings -->
    <section class="settings-card">
      <div class="section-header">
        <div>
          <h2>Profile Information</h2>
          <p>Update your personal account information.</p>
        </div>
      </div>

      <div class="form-grid">
        <div class="form-group">
          <label>Full Name</label>
          <input v-model="profile.name" type="text" />
        </div>

        <div class="form-group">
          <label>Email Address</label>
          <input v-model="profile.email" type="email" />
        </div>
      </div>

      <div class="profile-preview">
        <div class="avatar">
          {{ initials }}
        </div>

        <div>
          <strong>{{ profile.name }}</strong>
          <span>{{ profile.email }}</span>
        </div>
      </div>

      <div class="card-footer">
        <button class="primary-btn" @click="saveProfile">
          Save Changes
        </button>
      </div>
    </section>

    <!-- Password -->
    <section class="settings-card">
      <div class="section-header">
        <div>
          <h2>Password</h2>
          <p>Change your password to keep your account secure.</p>
        </div>
      </div>

      <div class="form-grid">
        <div class="form-group">
          <label>Current Password</label>
          <input
            v-model="password.current"
            type="password"
            placeholder="Enter current password"
          />
        </div>

        <div class="form-group">
          <label>New Password</label>
          <input
            v-model="password.newPassword"
            type="password"
            placeholder="Enter new password"
          />
        </div>

        <div class="form-group">
          <label>Confirm New Password</label>
          <input
            v-model="password.confirmPassword"
            type="password"
            placeholder="Confirm new password"
          />
        </div>
      </div>

      <div class="card-footer">
        <button class="secondary-btn" @click="changePassword">
          Change Password
        </button>
      </div>
    </section>

    <!-- Notifications -->
    <section class="settings-card">
      <div class="section-header">
        <div>
          <h2>Notifications</h2>
          <p>Choose which notifications you want to receive.</p>
        </div>
      </div>

      <div class="settings-list">

        <div class="setting-row">
          <div>
            <strong>Price Alerts</strong>
            <span>Receive notifications when product prices change.</span>
          </div>

          <label class="switch">
            <input v-model="notifications.priceAlerts" type="checkbox" />
            <span class="slider"></span>
          </label>
        </div>

        <div class="setting-row">
          <div>
            <strong>Email Notifications</strong>
            <span>Receive important updates by email.</span>
          </div>

          <label class="switch">
            <input v-model="notifications.email" type="checkbox" />
            <span class="slider"></span>
          </label>
        </div>

        <div class="setting-row">
          <div>
            <strong>Weekly Summary</strong>
            <span>Receive a weekly summary of price activity.</span>
          </div>

          <label class="switch">
            <input v-model="notifications.weeklySummary" type="checkbox" />
            <span class="slider"></span>
          </label>
        </div>

      </div>
    </section>

    <!-- Preferences -->
    <section class="settings-card">
      <div class="section-header">
        <div>
          <h2>Preferences</h2>
          <p>Customize how PriceTrack works for you.</p>
        </div>
      </div>

      <div class="form-grid">

        <div class="form-group">
          <label>Currency</label>

          <select v-model="preferences.currency">
            <option value="USD">USD - US Dollar</option>
            <option value="ETB">ETB - Ethiopian Birr</option>
            <option value="EUR">EUR - Euro</option>
            <option value="GBP">GBP - British Pound</option>
          </select>
        </div>

        <div class="form-group">
          <label>Theme</label>

          <select v-model="preferences.theme">
            <option value="light">Light</option>
            <option value="dark">Dark</option>
            <option value="system">System Default</option>
          </select>
        </div>

      </div>

      <div class="card-footer">
        <button class="primary-btn" @click="savePreferences">
          Save Preferences
        </button>
      </div>
    </section>

    <!-- Danger Zone -->
    <section class="settings-card danger-card">
      <div class="section-header">
        <div>
          <h2>Danger Zone</h2>
          <p>Actions in this section can affect your account.</p>
        </div>
      </div>

      <div class="danger-row">
        <div>
          <strong>Deactivate Account</strong>
          <span>
            Temporarily disable your PriceTrack account.
          </span>
        </div>

        <button class="danger-btn" @click="deactivateAccount">
          Deactivate
        </button>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed, reactive } from 'vue'

const profile = reactive({
  name: 'Arafat',
  email: 'arafat@example.com'
})

const password = reactive({
  current: '',
  newPassword: '',
  confirmPassword: ''
})

const notifications = reactive({
  priceAlerts: true,
  email: true,
  weeklySummary: false
})

const preferences = reactive({
  currency: 'USD',
  theme: 'light'
})

const initials = computed(() => {
  return profile.name
    .split(' ')
    .map(word => word[0])
    .join('')
    .substring(0, 2)
    .toUpperCase()
})

function saveProfile() {
  console.log('Profile saved:', profile)
  alert('Profile updated successfully.')
}

function changePassword() {
  if (!password.current || !password.newPassword) {
    alert('Please fill in all password fields.')
    return
  }

  if (password.newPassword !== password.confirmPassword) {
    alert('New passwords do not match.')
    return
  }

  console.log('Password changed')
  alert('Password changed successfully.')

  password.current = ''
  password.newPassword = ''
  password.confirmPassword = ''
}

function savePreferences() {
  console.log('Preferences saved:', preferences)
  alert('Preferences saved successfully.')
}

function deactivateAccount() {
  const confirmed = confirm(
    'Are you sure you want to deactivate your account?'
  )

  if (confirmed) {
    console.log('Account deactivation requested')
  }
}
</script>

<style scoped>
.settings-page {
  padding: 36px 40px 60px;
  max-width: 1200px;
  margin: 0 auto;
  font-family: Georgia, 'Times New Roman', serif;
}

/* Header */

.page-header {
  margin-bottom: 28px;
}

.page-header h1 {
  margin: 0 0 8px;
  font-size: 32px;
  font-weight: 700;
  color: #111827;
}

.page-header p {
  margin: 0;
  color: #6b7280;
  font-size: 16px;
}

/* Cards */

.settings-card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 14px;
  margin-bottom: 24px;
  overflow: hidden;
}

.section-header {
  padding: 24px 28px;
  border-bottom: 1px solid #edf1f5;
}

.section-header h2 {
  margin: 0 0 6px;
  font-size: 20px;
  color: #172033;
}

.section-header p {
  margin: 0;
  color: #7a8494;
  font-size: 14px;
}

/* Forms */

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 22px;
  padding: 26px 28px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
}

.form-group input,
.form-group select {
  height: 46px;
  border: 1px solid #d8dee8;
  border-radius: 8px;
  padding: 0 14px;
  font-family: inherit;
  font-size: 15px;
  color: #273142;
  background: white;
  outline: none;
}

.form-group input:focus,
.form-group select:focus {
  border-color: #2864dc;
  box-shadow: 0 0 0 3px rgba(40, 100, 220, 0.08);
}

/* Profile */

.profile-preview {
  margin: 0 28px 24px;
  padding: 18px;
  background: #f8fafc;
  border-radius: 10px;
  display: flex;
  align-items: center;
  gap: 14px;
}

.avatar {
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: #2864dc;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 18px;
}

.profile-preview div:last-child {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.profile-preview strong {
  color: #172033;
  font-size: 16px;
}

.profile-preview span {
  color: #7a8494;
  font-size: 14px;
}

/* Footer */

.card-footer {
  padding: 18px 28px;
  border-top: 1px solid #edf1f5;
  display: flex;
  justify-content: flex-end;
}

/* Buttons */

.primary-btn,
.secondary-btn,
.danger-btn {
  border: none;
  border-radius: 8px;
  padding: 11px 20px;
  font-family: inherit;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}

.primary-btn {
  background: #2864dc;
  color: white;
}

.primary-btn:hover {
  background: #1f56c2;
}

.secondary-btn {
  background: #eef4ff;
  color: #2864dc;
}

.secondary-btn:hover {
  background: #e1ebff;
}

/* Notification settings */

.settings-list {
  padding: 8px 28px;
}

.setting-row {
  min-height: 76px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  border-bottom: 1px solid #edf1f5;
}

.setting-row:last-child {
  border-bottom: none;
}

.setting-row div {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.setting-row strong {
  font-size: 15px;
  color: #273142;
}

.setting-row span {
  font-size: 13px;
  color: #7a8494;
}

/* Switch */

.switch {
  position: relative;
  width: 48px;
  height: 26px;
  flex-shrink: 0;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  inset: 0;
  background: #cbd5e1;
  border-radius: 30px;
  cursor: pointer;
  transition: 0.2s;
}

.slider::before {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  left: 3px;
  top: 3px;
  background: white;
  border-radius: 50%;
  transition: 0.2s;
}

.switch input:checked + .slider {
  background: #2864dc;
}

.switch input:checked + .slider::before {
  transform: translateX(22px);
}

/* Danger */

.danger-card {
  border-color: #fecaca;
}

.danger-card .section-header {
  background: #fffafa;
}

.danger-card h2 {
  color: #b91c1c;
}

.danger-row {
  padding: 22px 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}

.danger-row div {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.danger-row strong {
  color: #374151;
  font-size: 15px;
}

.danger-row span {
  color: #7a8494;
  font-size: 13px;
}

.danger-btn {
  color: #dc2626;
  background: #fff1f2;
  border: 1px solid #fecaca;
}

.danger-btn:hover {
  background: #fee2e2;
}

/* Responsive */

@media (max-width: 800px) {
  .settings-page {
    padding: 24px 18px 40px;
  }

  .form-grid {
    grid-template-columns: 1fr;
  }

  .danger-row {
    align-items: flex-start;
    flex-direction: column;
  }

  .card-footer {
    justify-content: flex-start;
  }
}
</style>