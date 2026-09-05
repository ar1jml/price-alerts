<template>
  <div class="login-page">

    <!-- =====================================================
         HERO / PRODUCT INTRO
    ====================================================== -->
    <section class="hero-panel">
      <div class="hero-content">

        <!-- Brand -->
        <div class="brand hero-brand">
          <div class="brand-icon">
            <font-awesome-icon icon="tags" />
          </div>

          <div>
            <h1>PriceTrack</h1>
            <span>Smart Price Monitoring</span>
          </div>
        </div>

        <!-- Hero message -->
        <div class="hero-message">
          <h2>
            Track Prices.<br />
            Make <span>Smarter Decisions.</span>
          </h2>

          <p>
            Monitor product prices, spot trends, and get real-time
            alerts — all in one place.
          </p>
        </div>

        <!-- Features -->
        <div class="features">

          <div class="feature">
            <div class="feature-icon">
              <font-awesome-icon icon="chart-line" />
            </div>

            <div>
              <h3>Track Prices</h3>
              <p>
                Monitor prices across multiple stores and products.
              </p>
            </div>
          </div>

          <div class="feature">
            <div class="feature-icon">
              <font-awesome-icon icon="bell" />
            </div>

            <div>
              <h3>Get Alerts</h3>
              <p>
                Be notified about price changes and deals.
              </p>
            </div>
          </div>

          <div class="feature">
            <div class="feature-icon">
              <font-awesome-icon icon="chart-column" />
            </div>

            <div>
              <h3>Analyze Trends</h3>
              <p>
                View historical data and identify patterns.
              </p>
            </div>
          </div>

          <div class="feature">
            <div class="feature-icon">
              <font-awesome-icon icon="shield-halved" />
            </div>

            <div>
              <h3>Save Money</h3>
              <p>
                Make better purchasing decisions and get the best deals.
              </p>
            </div>
          </div>

        </div>

        <!-- =================================================
             DASHBOARD PREVIEW
        ================================================== -->
        <div class="dashboard-preview">

          <!-- Sidebar -->
          <aside class="preview-sidebar">

            <div class="preview-logo">
              <font-awesome-icon icon="tags" />
              <span>PriceTrack</span>
            </div>

            <div class="preview-nav active">
              <font-awesome-icon icon="house" />
              <span>Dashboard</span>
            </div>

            <div class="preview-nav">
              <font-awesome-icon icon="box" />
              <span>Products</span>
            </div>

            <div class="preview-nav">
              <font-awesome-icon icon="store" />
              <span>Stores</span>
            </div>

            <div class="preview-nav">
              <font-awesome-icon icon="bell" />
              <span>Alerts</span>
              <small>3</small>
            </div>

            <div class="preview-nav">
              <font-awesome-icon icon="chart-line" />
              <span>Price History</span>
            </div>

            <div class="preview-nav">
              <font-awesome-icon icon="users" />
              <span>Users</span>
            </div>

            <div class="preview-bottom">

              <div class="preview-nav">
                <font-awesome-icon icon="gear" />
                <span>Settings</span>
              </div>

              <div class="preview-nav">
                <font-awesome-icon icon="right-from-bracket" />
                <span>Logout</span>
              </div>

            </div>

          </aside>

          <!-- Dashboard content -->
          <div class="preview-main">

            <!-- Search -->
            <div class="preview-search">
              <font-awesome-icon icon="magnifying-glass" />
              <span>Search products, stores, or categories...</span>
            </div>

            <!-- Heading -->
            <div class="preview-heading">
              <strong>Good morning, Arafat!</strong>

              <span>
                Here's what's happening with your prices today.
              </span>
            </div>

            <!-- Statistics -->
            <div class="preview-stats">

              <div class="preview-stat">
                <span>Total Products</span>
                <strong>48</strong>
                <small>↑ 12%</small>
              </div>

              <div class="preview-stat">
                <span>Monitored Stores</span>
                <strong>12</strong>
                <small>↑ 8%</small>
              </div>

              <div class="preview-stat">
                <span>Active Alerts</span>
                <strong>5</strong>
                <small>↑ 67%</small>
              </div>

            </div>

            <!-- Chart -->
            <div class="preview-chart">

              <div class="chart-title">
                <strong>Price Trends</strong>
                <span>Last 7 days</span>
              </div>

              <div class="chart-area">

                <div class="grid-line line-1"></div>
                <div class="grid-line line-2"></div>
                <div class="grid-line line-3"></div>
                <div class="grid-line line-4"></div>

                <svg
                  viewBox="0 0 500 120"
                  preserveAspectRatio="none"
                >
                  <polyline
                    points="0,70 70,82 140,55 210,72 280,42 350,60 430,35 500,50"
                    fill="none"
                    stroke="#2777ff"
                    stroke-width="3"
                  />

                  <polyline
                    points="0,85 70,70 140,78 210,65 280,75 350,58 430,68 500,55"
                    fill="none"
                    stroke="#20a66a"
                    stroke-width="3"
                  />

                  <polyline
                    points="0,105 70,92 140,97 210,88 280,94 350,82 430,90 500,75"
                    fill="none"
                    stroke="#f59e0b"
                    stroke-width="3"
                  />
                </svg>

              </div>

            </div>

          </div>

        </div>

      </div>
    </section>

    <!-- =====================================================
         LOGIN PANEL
    ====================================================== -->
    <section class="login-panel">

      <!-- Register link -->
      <div class="register-link">
        <span>New to PriceTrack?</span>

        <router-link to="/register">
          Create an account
          <font-awesome-icon icon="arrow-right" />
        </router-link>
      </div>

      <div class="login-container">

        <!-- Login brand -->
        <div class="login-brand">

          <div class="login-brand-icon">
            <font-awesome-icon icon="tags" />
          </div>

          <div>
            <h1>PriceTrack</h1>
            <p>Smart Price Monitoring</p>
          </div>

        </div>

        <!-- Heading -->
        <div class="login-heading">
          <h2>Welcome back</h2>
          <p>Sign in to your account to continue</p>
        </div>

        <!-- Login form -->
        <form @submit.prevent="handleLogin">

          <!-- Email -->
          <div class="form-group">
            <label for="email">Email address</label>

            <div class="input-wrapper">
              <font-awesome-icon icon="envelope" />

              <input
                id="email"
                v-model="email"
                type="email"
                placeholder="Enter your email"
                autocomplete="email"
                required
              />
            </div>
          </div>

          <!-- Password -->
          <div class="form-group">
            <label for="password">Password</label>

            <div class="input-wrapper">
              <font-awesome-icon icon="lock" />

              <input
                id="password"
                v-model="password"
                :type="showPassword ? 'text' : 'password'"
                placeholder="Enter your password"
                autocomplete="current-password"
                required
              />

              <button
                type="button"
                class="password-toggle"
                aria-label="Toggle password visibility"
                @click="showPassword = !showPassword"
              >
                <font-awesome-icon
                  :icon="showPassword ? 'eye-slash' : 'eye'"
                />
              </button>
            </div>
          </div>

          <!-- Options -->
          <div class="form-options">

            <label class="remember">
              <input
                v-model="rememberMe"
                type="checkbox"
              />

              <span>Remember me</span>
            </label>

            <router-link to="/forgot-password">
              Forgot password?
            </router-link>

          </div>

          <!-- Sign in -->
          <button
            type="submit"
            class="sign-in-button"
          >
            <span>Sign In</span>
            <font-awesome-icon icon="arrow-right" />
          </button>

        </form>

        <!-- Divider -->
        <div class="divider">
          <span></span>
          <p>OR</p>
          <span></span>
        </div>

        <!-- Google -->
        <button
          type="button"
          class="google-button"
          @click="loginWithGoogle"
        >
          <span class="google-icon">G</span>
          <span>Continue with Google</span>
        </button>

        <!-- Create account -->
        <div class="create-account">
          <span>Don't have an account?</span>

          <router-link to="/register">
            Create one
          </router-link>
        </div>

      </div>
    </section>

  </div>
</template>



<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const email = ref('')
const password = ref('')
const rememberMe = ref(false)
const showPassword = ref(false)

function handleLogin() {
  console.log({
    email: email.value,
    password: password.value,
    rememberMe: rememberMe.value
  })

  router.push('/dashboard')
}

function loginWithGoogle() {
  console.log('Google login')
}
</script>


<style>
html,
body,
#app {
  margin: 0;
  padding: 0;
  width: 100%;
  min-height: 100%;
}

body {
  overflow-x: hidden;
}
</style>


<style scoped>

/* =========================================================
   BASE
========================================================= */

* {
  box-sizing: border-box;
}

.login-page {
  width: 100%;
  min-height: 100vh;
  display: grid;
  grid-template-columns: 58% 42%;
  overflow-x: hidden;
  font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif;
}


/* =========================================================
   HERO
========================================================= */

.hero-panel {
  min-width: 0;
  background: #071a3d;
  color: #ffffff;
  overflow: hidden;
}

.hero-content {
  padding: 52px;
}


/* Brand */

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-icon {
  width: 46px;
  height: 46px;
  border-radius: 12px;

  display: flex;
  align-items: center;
  justify-content: center;

  background: #2777ff;
  color: #ffffff;

  box-shadow: 0 8px 20px rgba(39, 119, 255, 0.25);
}

.brand-icon svg {
  width: 20px;
  height: 20px;
}

.brand h1 {
  margin: 0;
  font-size: 23px;
  font-weight: 700;
}

.brand span {
  display: block;
  margin-top: 2px;
  font-size: 11px;
  color: #9db0d0;
}


/* Hero message */

.hero-message {
  margin-top: 65px;
  max-width: 650px;
}

.hero-message h2 {
  margin: 0;
  font-size: clamp(38px, 4vw, 58px);
  line-height: 1.05;
  letter-spacing: -2px;
  font-weight: 700;
}

.hero-message h2 span {
  color: #4c94ff;
}

.hero-message p {
  max-width: 570px;
  margin: 24px 0 0;

  color: #a9b8d1;
  font-size: 16px;
  line-height: 1.7;
}


/* =========================================================
   FEATURES
========================================================= */

.features {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;

  margin-top: 46px;
}

.feature {
  min-width: 0;
}

.feature-icon {
  width: 42px;
  height: 42px;

  display: flex;
  align-items: center;
  justify-content: center;

  margin-bottom: 15px;

  border-radius: 10px;
  background: rgba(39, 119, 255, 0.14);
  color: #4c94ff;
}

.feature-icon svg {
  width: 17px;
  height: 17px;
}

.feature h3 {
  margin: 0 0 7px;
  font-size: 14px;
  font-weight: 600;
}

.feature p {
  margin: 0;
  color: #91a5c6;
  font-size: 11px;
  line-height: 1.55;
}


/* =========================================================
   DASHBOARD PREVIEW
========================================================= */

.dashboard-preview {
  display: flex;

  width: 100%;
  max-width: 900px;
  height: 360px;

  margin-top: 48px;

  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 15px;

  overflow: hidden;

  background: #ffffff;

  box-shadow:
    0 25px 60px rgba(0, 0, 0, 0.3);
}


/* Sidebar */

.preview-sidebar {
  width: 145px;
  min-width: 145px;

  padding: 18px 10px;

  background: #0b2148;
  color: #ffffff;
}

.preview-logo {
  display: flex;
  align-items: center;
  gap: 7px;

  padding: 0 7px;
  margin-bottom: 22px;
}

.preview-logo svg {
  width: 13px;
  height: 13px;
  color: #4c94ff;
}

.preview-logo span {
  font-size: 10px;
  font-weight: 700;
}

.preview-nav {
  display: flex;
  align-items: center;
  gap: 8px;

  min-width: 0;

  padding: 9px 8px;
  margin-bottom: 3px;

  border-radius: 6px;

  color: #91a5c6;
}

.preview-nav.active {
  background: rgba(39, 119, 255, 0.15);
  color: #ffffff;
}

.preview-nav svg {
  width: 11px;
  height: 11px;
  min-width: 11px;
}

.preview-nav span {
  min-width: 0;

  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;

  font-size: 8px;
}

.preview-nav small {
  margin-left: auto;

  padding: 2px 5px;

  border-radius: 10px;

  background: #2777ff;
  color: #ffffff;

  font-size: 7px;
}

.preview-bottom {
  margin-top: 55px;
}


/* Dashboard main */

.preview-main {
  flex: 1;
  min-width: 0;

  padding: 18px;

  background: #f7f9fc;
  overflow: hidden;
}


/* Search */

.preview-search {
  display: flex;
  align-items: center;
  gap: 8px;

  height: 32px;

  padding: 0 10px;

  border: 1px solid #e5e9f0;
  border-radius: 6px;

  background: #ffffff;

  color: #9aa5b5;

  font-size: 8px;
}

.preview-search svg {
  width: 10px;
  min-width: 10px;
}


/* Heading */

.preview-heading {
  margin: 18px 0 15px;
}

.preview-heading strong {
  display: block;

  margin-bottom: 4px;

  color: #17233b;

  font-size: 13px;
}

.preview-heading span {
  color: #8b96a8;
  font-size: 8px;
}


/* Stats */

.preview-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.preview-stat {
  min-width: 0;

  padding: 12px;

  border: 1px solid #e7ebf1;
  border-radius: 8px;

  background: #ffffff;
}

.preview-stat span {
  display: block;

  color: #8b96a8;

  font-size: 7px;
}

.preview-stat strong {
  display: block;

  margin: 5px 0;

  color: #17233b;

  font-size: 19px;
}

.preview-stat small {
  color: #20a66a;
  font-size: 7px;
}


/* Chart */

.preview-chart {
  margin-top: 12px;

  padding: 12px;

  border: 1px solid #e7ebf1;
  border-radius: 8px;

  background: #ffffff;
}

.chart-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chart-title strong {
  color: #17233b;
  font-size: 9px;
}

.chart-title span {
  color: #8b96a8;
  font-size: 7px;
}

.chart-area {
  position: relative;

  height: 100px;

  margin-top: 8px;

  overflow: hidden;
}

.grid-line {
  position: absolute;
  left: 0;
  right: 0;

  height: 1px;

  background: #edf0f5;
}

.line-1 {
  top: 20%;
}

.line-2 {
  top: 40%;
}

.line-3 {
  top: 60%;
}

.line-4 {
  top: 80%;
}

.chart-area svg {
  position: absolute;

  width: 100%;
  height: 100%;

  left: 0;
  top: 0;
}


/* =========================================================
   LOGIN PANEL
========================================================= */

.login-panel {
  position: relative;

  min-width: 0;
  min-height: 100vh;

  display: flex;
  align-items: center;
  justify-content: center;

  padding: 70px 50px;

  background: #ffffff;
}

.login-container {
  width: 100%;
  max-width: 420px;
}


/* Register */

.register-link {
  position: absolute;

  top: 28px;
  right: 42px;

  display: flex;
  align-items: center;
  gap: 6px;

  font-size: 12px;
  color: #8b96a8;
}

.register-link a {
  display: flex;
  align-items: center;
  gap: 5px;

  color: #2777ff;

  font-weight: 600;
  text-decoration: none;
}

.register-link svg {
  width: 10px;
}


/* Login brand */

.login-brand {
  display: flex;
  align-items: center;
  gap: 11px;

  margin-bottom: 42px;
}

.login-brand-icon {
  width: 43px;
  height: 43px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 11px;

  background: #2777ff;
  color: #ffffff;
}

.login-brand-icon svg {
  width: 18px;
  height: 18px;
}

.login-brand h1 {
  margin: 0;

  color: #17233b;

  font-size: 21px;
}

.login-brand p {
  margin: 2px 0 0;

  color: #9aa5b5;

  font-size: 10px;
}


/* Heading */

.login-heading {
  margin-bottom: 30px;
}

.login-heading h2 {
  margin: 0 0 8px;

  color: #17233b;

  font-size: 30px;
  letter-spacing: -0.5px;
}

.login-heading p {
  margin: 0;

  color: #8b96a8;

  font-size: 13px;
}


/* =========================================================
   FORM
========================================================= */

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;

  margin-bottom: 8px;

  color: #344054;

  font-size: 12px;
  font-weight: 600;
}

.input-wrapper {
  position: relative;

  display: flex;
  align-items: center;

  height: 50px;

  border: 1px solid #dfe4ec;
  border-radius: 8px;

  background: #ffffff;

  transition: border-color 0.2s, box-shadow 0.2s;
}

.input-wrapper:focus-within {
  border-color: #2777ff;

  box-shadow: 0 0 0 3px rgba(39, 119, 255, 0.08);
}

.input-wrapper > svg {
  width: 14px;
  min-width: 14px;

  margin-left: 15px;

  color: #9aa5b5;
}

.input-wrapper input {
  flex: 1;

  min-width: 0;

  height: 100%;

  padding: 0 13px;

  border: none;
  outline: none;

  background: transparent;

  color: #17233b;

  font-size: 13px;
}

.input-wrapper input::placeholder {
  color: #a7afbd;
}


/* Password */

.password-toggle {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 42px;
  height: 100%;

  border: none;
  background: transparent;

  color: #9aa5b5;

  cursor: pointer;
}

.password-toggle svg {
  width: 14px;
}


/* Options */

.form-options {
  display: flex;
  align-items: center;
  justify-content: space-between;

  margin: 5px 0 23px;

  font-size: 11px;
}

.remember {
  display: flex;
  align-items: center;
  gap: 7px;

  color: #687386;

  cursor: pointer;
}

.remember input {
  width: 14px;
  height: 14px;

  accent-color: #2777ff;
}

.form-options a {
  color: #2777ff;

  text-decoration: none;
  font-weight: 600;
}


/* Sign in */

.sign-in-button {
  width: 100%;
  height: 50px;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  border: none;
  border-radius: 8px;

  background: #2777ff;
  color: #ffffff;

  font-size: 13px;
  font-weight: 600;

  cursor: pointer;

  transition:
    transform 0.2s,
    box-shadow 0.2s,
    background 0.2s;
}

.sign-in-button:hover {
  background: #1768ef;

  box-shadow:
    0 8px 20px rgba(39, 119, 255, 0.2);

  transform: translateY(-1px);
}

.sign-in-button svg {
  width: 12px;
}


/* =========================================================
   DIVIDER
========================================================= */

.divider {
  display: flex;
  align-items: center;
  gap: 12px;

  margin: 27px 0;
}

.divider span {
  flex: 1;

  height: 1px;

  background: #e7ebf1;
}

.divider p {
  margin: 0;

  color: #a0a9b7;

  font-size: 9px;
  font-weight: 600;
}


/* =========================================================
   GOOGLE
========================================================= */

.google-button {
  width: 100%;
  height: 50px;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  border: 1px solid #dfe4ec;
  border-radius: 8px;

  background: #ffffff;
  color: #344054;

  font-size: 12px;
  font-weight: 600;

  cursor: pointer;

  transition:
    border-color 0.2s,
    background 0.2s;
}

.google-button:hover {
  background: #f8fafc;
  border-color: #cbd3df;
}

.google-icon {
  font-size: 17px;
  font-weight: 700;
  color: #4285f4;
}


/* Create account */

.create-account {
  display: flex;
  justify-content: center;
  gap: 5px;

  margin-top: 28px;

  color: #8b96a8;

  font-size: 11px;
}

.create-account a {
  color: #2777ff;

  text-decoration: none;

  font-weight: 600;
}


/* =========================================================
   LARGE TABLET
========================================================= */

@media (max-width: 1200px) {

  .login-page {
    grid-template-columns: 55% 45%;
  }

  .hero-content {
    padding: 45px;
  }

  .dashboard-preview {
    height: 330px;
  }

  .features {
    gap: 13px;
  }

}


/* =========================================================
   TABLET
========================================================= */

@media (max-width: 992px) {

  .login-page {
    display: block;
  }

  .hero-panel {
    min-height: auto;
  }

  .hero-content {
    padding: 50px 40px;
  }

  .hero-message {
    max-width: 720px;
  }

  .features {
    grid-template-columns: repeat(2, 1fr);
    gap: 25px;
  }

  .dashboard-preview {
    max-width: 900px;
    height: 360px;

    margin-left: auto;
    margin-right: auto;
  }

  .login-panel {
    min-height: auto;

    padding: 70px 40px;
  }

  .login-container {
    max-width: 500px;
  }

  .register-link {
    position: static;

    justify-content: center;

    margin-bottom: 35px;
  }

}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 768px) {

  .login-page {
    display: block;
    width: 100%;

    overflow-x: hidden;
  }


  /* HERO */

  .hero-content {
    padding: 32px 20px 35px;
  }

  .hero-brand {
    margin-bottom: 42px;
  }

  .brand-icon {
    width: 43px;
    height: 43px;
  }

  .brand h1 {
    font-size: 21px;
  }

  .brand span {
    font-size: 10px;
  }

  .hero-message {
    margin-top: 0;
    margin-bottom: 35px;
  }

  .hero-message h2 {
    font-size: 38px;
    line-height: 1.08;
    letter-spacing: -1.5px;
  }

  .hero-message p {
    margin-top: 18px;

    font-size: 14px;
    line-height: 1.65;
  }


  /* FEATURES */

  .features {
    grid-template-columns: 1fr 1fr;
    gap: 14px;

    margin-top: 0;
  }

  .feature {
    padding: 16px;

    border-radius: 10px;

    background: rgba(255, 255, 255, 0.035);
  }

  .feature-icon {
    width: 37px;
    height: 37px;

    margin-bottom: 11px;
  }

  .feature h3 {
    font-size: 13px;
  }

  .feature p {
    font-size: 10px;
    line-height: 1.5;
  }


  /* DASHBOARD */

  .dashboard-preview {
    width: 100%;
    height: 300px;

    margin-top: 32px;

    border-radius: 11px;
  }

  .preview-sidebar {
    width: 95px;
    min-width: 95px;

    padding: 12px 7px;
  }

  .preview-logo {
    margin-bottom: 16px;
  }

  .preview-logo span {
    font-size: 8px;
  }

  .preview-logo svg {
    width: 11px;
  }

  .preview-nav {
    padding: 7px 5px;
    gap: 5px;
  }

  .preview-nav span {
    font-size: 6.5px;
  }

  .preview-nav svg {
    width: 9px;
    height: 9px;
    min-width: 9px;
  }

  .preview-nav small {
    font-size: 5px;
  }

  .preview-bottom {
    margin-top: 25px;
  }

  .preview-main {
    padding: 12px;
  }

  .preview-search {
    height: 27px;

    font-size: 6.5px;
  }

  .preview-heading {
    margin: 14px 0 10px;
  }

  .preview-heading strong {
    font-size: 10px;
  }

  .preview-heading span {
    font-size: 6.5px;
  }

  .preview-stats {
    gap: 6px;
  }

  .preview-stat {
    padding: 8px 6px;
  }

  .preview-stat span {
    font-size: 5.5px;
  }

  .preview-stat strong {
    font-size: 14px;
  }

  .preview-stat small {
    font-size: 5.5px;
  }

  .preview-chart {
    margin-top: 8px;
    padding: 8px;
  }

  .chart-title strong {
    font-size: 7px;
  }

  .chart-title span {
    font-size: 5.5px;
  }

  .chart-area {
    height: 65px;
  }


  /* LOGIN */

  .login-panel {
    min-height: auto;

    padding: 45px 20px 50px;
  }

  .register-link {
    margin-bottom: 30px;

    font-size: 11px;
  }

  .login-brand {
    justify-content: center;

    margin-bottom: 30px;
  }

  .login-heading {
    text-align: center;

    margin-bottom: 28px;
  }

  .login-heading h2 {
    font-size: 27px;
  }

  .login-heading p {
    font-size: 12px;
  }

}


/* =========================================================
   SMALL MOBILE
========================================================= */

@media (max-width: 480px) {

  .hero-content {
    padding: 28px 16px 30px;
  }

  .hero-message h2 {
    font-size: 32px;
  }

  .hero-message p {
    font-size: 13px;
  }


  .features {
    gap: 9px;
  }

  .feature {
    padding: 13px 11px;
  }

  .feature-icon {
    width: 34px;
    height: 34px;
  }

  .feature h3 {
    font-size: 12px;
  }

  .feature p {
    font-size: 9px;
  }


  .dashboard-preview {
    height: 255px;
  }

  .preview-sidebar {
    width: 78px;
    min-width: 78px;
  }

  .preview-main {
    padding: 9px;
  }

  .preview-heading strong {
    font-size: 8px;
  }

  .preview-heading span {
    font-size: 5.5px;
  }

  .preview-stat {
    padding: 6px 4px;
  }

  .preview-stat strong {
    font-size: 11px;
  }

  .chart-area {
    height: 52px;
  }


  .login-panel {
    padding: 38px 16px 45px;
  }

  .login-heading h2 {
    font-size: 25px;
  }

  .input-wrapper,
  .sign-in-button,
  .google-button {
    height: 48px;
  }

}


/* =========================================================
   VERY SMALL PHONES
========================================================= */

@media (max-width: 360px) {

  .hero-message h2 {
    font-size: 29px;
  }

  .features {
    grid-template-columns: 1fr;
  }

  .feature {
    display: grid;

    grid-template-columns: auto 1fr;
    column-gap: 12px;

    align-items: center;
  }

  .feature-icon {
    grid-row: span 2;

    margin: 0;
  }

  .feature h3 {
    margin: 0;
  }

  .feature p {
    margin: 3px 0 0;
  }


  .dashboard-preview {
    height: 220px;
  }

  .preview-sidebar {
    width: 68px;
    min-width: 68px;
  }

  .preview-nav {
    padding: 6px 4px;
  }

  .preview-nav span {
    font-size: 5.5px;
  }

  .preview-main {
    padding: 7px;
  }

  .preview-heading strong {
    font-size: 7px;
  }

  .preview-heading span {
    font-size: 5px;
  }

}

</style>