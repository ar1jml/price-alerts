<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()
const route = useRoute()
const isSignIn = ref(route.query.mode === 'signin')
const email = ref('')
const password = ref('')
const showPassword = ref(false)
const isSubmitting = ref(false)
const errorMessage = ref('')
const successMessage = ref('')
const apiBaseUrl = (import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000').replace(/\/$/, '')

function toggleMode() {
  if (isSubmitting.value) return

  isSignIn.value = !isSignIn.value
  password.value = ''
  showPassword.value = false
  errorMessage.value = ''
  successMessage.value = ''
}

function getErrorMessage(detail, status) {
  if (typeof detail === 'string') return detail
  if (Array.isArray(detail)) {
    return detail.map((issue) => issue.msg).join('. ')
  }
  return `Request failed (${status}). Please try again.`
}

async function submitForm() {
  isSubmitting.value = true
  errorMessage.value = ''
  successMessage.value = ''

  try {
    const response = await fetch(
      `${apiBaseUrl}/api/v1/auth/${isSignIn.value ? 'login' : 'register'}`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: email.value,
          password: password.value,
        }),
      },
    )
    const result = await response.json()

    if (!response.ok) {
      throw new Error(getErrorMessage(result.detail, response.status))
    }

    if (isSignIn.value) {
      if (typeof result.access_token !== 'string' || !result.access_token) {
        throw new Error('The server did not return an access token.')
      }

      window.localStorage.setItem('access_token', result.access_token)
      await router.push('/dashboard')
      return
    }

    isSignIn.value = true
    password.value = ''
    showPassword.value = false
    successMessage.value = 'Account created. Sign in to continue.'
  } catch (error) {
    errorMessage.value = error instanceof Error
      ? error.message
      : 'Unable to complete your request. Please try again.'
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <main class="auth-page">
    <header class="auth-header">
      <router-link to="/login" class="auth-brand" aria-label="PriceTrack home">
        <span class="auth-brand-icon">
          <font-awesome-icon icon="tags" />
        </span>
        <span class="auth-brand-copy">
          <strong>PriceTrack</strong>
          <small>Smart Price Monitoring</small>
        </span>
      </router-link>
      <router-link to="/login" class="home-link">Back to overview</router-link>
    </header>

    <section class="auth-main" aria-labelledby="auth-title">
      <div class="auth-intro">
        <span class="auth-eyebrow">SHOP SMARTER</span>
        <h1 id="auth-title">
          {{ isSignIn ? 'Welcome back.' : 'Make every price drop count.' }}
        </h1>
        <p>
          {{ isSignIn
            ? 'Sign in to keep track of the products and prices you care about.'
            : 'Create your account and start tracking the prices you care about.' }}
        </p>
      </div>

      <div class="auth-card-shell">
        <div class="auth-card">
          <form
            v-if="!isSignIn"
            class="auth-face"
            @submit.prevent="submitForm"
          >
            <div class="card-heading">
              <span class="card-eyebrow">GET STARTED</span>
              <h2>Create your account</h2>
              <p>It only takes a moment.</p>
            </div>

            <label class="auth-field" for="register-email">
              <span>Email address</span>
              <input
                id="register-email"
                v-model.trim="email"
                type="email"
                name="email"
                autocomplete="email"
                placeholder="you@example.com"
                required
              />
            </label>

            <div class="auth-field">
              <label for="register-password">Password</label>
              <div class="password-input">
                <input
                  id="register-password"
                  v-model="password"
                  :type="showPassword ? 'text' : 'password'"
                  name="password"
                  autocomplete="new-password"
                  minlength="8"
                  maxlength="128"
                  placeholder="At least 8 characters"
                  required
                />
                <button
                  class="password-toggle"
                  type="button"
                  :aria-label="showPassword ? 'Hide password' : 'Show password'"
                  :aria-pressed="showPassword"
                  @click="showPassword = !showPassword"
                >
                  <font-awesome-icon :icon="showPassword ? 'eye-slash' : 'eye'" aria-hidden="true" />
                </button>
              </div>
            </div>

            <p v-if="errorMessage" class="form-message is-error" role="alert">
              {{ errorMessage }}
            </p>
            <span v-else class="form-message-spacer" aria-hidden="true"></span>

            <button class="auth-submit" type="submit" :disabled="isSubmitting">
              {{ isSubmitting ? 'Creating account…' : 'Create account' }}
              <font-awesome-icon icon="arrow-right" />
            </button>

            <p class="auth-switch">
              Already have an account?
              <button type="button" @click="toggleMode">Sign in</button>
            </p>
          </form>

          <form
            v-else
            class="auth-face"
            @submit.prevent="submitForm"
          >
            <div class="card-heading">
              <span class="card-eyebrow">WELCOME BACK</span>
              <h2>Sign in</h2>
              <p>Continue tracking the prices you care about.</p>
            </div>

            <label class="auth-field" for="signin-email">
              <span>Email address</span>
              <input
                id="signin-email"
                v-model.trim="email"
                type="email"
                name="email"
                autocomplete="email"
                placeholder="you@example.com"
                required
              />
            </label>

            <div class="auth-field">
              <label for="signin-password">Password</label>
              <div class="password-input">
                <input
                  id="signin-password"
                  v-model="password"
                  :type="showPassword ? 'text' : 'password'"
                  name="password"
                  autocomplete="current-password"
                  maxlength="128"
                  placeholder="Enter your password"
                  required
                />
                <button
                  class="password-toggle"
                  type="button"
                  :aria-label="showPassword ? 'Hide password' : 'Show password'"
                  :aria-pressed="showPassword"
                  @click="showPassword = !showPassword"
                >
                  <font-awesome-icon :icon="showPassword ? 'eye-slash' : 'eye'" aria-hidden="true" />
                </button>
              </div>
            </div>

            <p v-if="errorMessage" class="form-message is-error" role="alert">
              {{ errorMessage }}
            </p>
            <p v-else-if="successMessage" class="form-message is-success" role="status">
              {{ successMessage }}
            </p>
            <span v-else class="form-message-spacer" aria-hidden="true"></span>

            <button class="auth-submit" type="submit" :disabled="isSubmitting">
              {{ isSubmitting ? 'Signing in…' : 'Sign in' }}
              <font-awesome-icon icon="arrow-right" />
            </button>

            <p class="auth-switch">
              New to PriceTrack?
              <button type="button" @click="toggleMode">Create an account</button>
            </p>
          </form>
        </div>
      </div>
    </section>

    <footer class="auth-footer">
      <span>PriceTrack</span>
      <span>Track prices. Make smarter decisions.</span>
    </footer>
  </main>
</template>

<style scoped>
* {
  box-sizing: border-box;
}

.auth-page {
  --brand-navy: #071a3d;
  --brand-primary: #2777ff;
  --brand-primary-hover: #1768ef;
  --brand-input: #102a52;
  --brand-border: #1d3966;
  --brand-text: #edf4ff;
  --brand-muted: #a9b8d1;

  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  background:
    radial-gradient(ellipse at 50% 45%, rgba(39, 119, 255, 0.1), transparent 44%),
    var(--brand-navy);
  color: var(--brand-text);
  text-align: left;
  font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif;
}

.auth-header {
  min-height: 82px;
  padding: 0 clamp(22px, 5vw, 72px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  border-bottom: 1px solid var(--brand-border);
}

.auth-brand {
  display: inline-flex;
  align-items: center;
  gap: 11px;
  color: var(--brand-text);
  text-decoration: none;
}

.auth-brand-icon {
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border-radius: 12px;
  background: var(--brand-primary);
  color: white;
  box-shadow: 0 8px 18px rgba(39, 119, 255, 0.2);
}

.auth-brand-icon svg {
  width: 18px;
}

.auth-brand-copy {
  display: grid;
  gap: 2px;
}

.auth-brand-copy strong {
  font-size: 17px;
  letter-spacing: -0.3px;
}

.auth-brand-copy small {
  color: var(--brand-muted);
  font-size: 10px;
}

.home-link {
  color: var(--brand-muted);
  font-size: 13px;
  text-decoration: none;
}

.home-link:hover {
  color: var(--brand-text);
}

.auth-main {
  flex: 1;
  width: min(100% - 40px, 1000px);
  margin: 0 auto;
  padding: 54px 0 64px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(340px, 440px);
  align-items: center;
  gap: clamp(42px, 8vw, 110px);
}

.auth-intro {
  max-width: 430px;
}

.auth-eyebrow,
.card-eyebrow {
  color: #73aaff;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 1.5px;
}

.auth-intro h1 {
  margin: 17px 0 14px;
  color: var(--brand-text);
  font-size: clamp(36px, 4.5vw, 56px);
  font-weight: 700;
  letter-spacing: -2px;
  line-height: 1.06;
}

.auth-intro p {
  max-width: 390px;
  margin: 0;
  color: var(--brand-muted);
  font-size: 15px;
  line-height: 1.7;
}

.auth-card-shell {
  width: 100%;
  height: 450px;
}

.auth-card {
  position: relative;
  width: 100%;
  height: 100%;
}

.auth-face {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 30px;
  border: 1px solid var(--brand-border);
  border-radius: 18px;
  background: linear-gradient(160deg, #0b2148, #081a38 78%);
  box-shadow: 0 24px 70px rgba(0, 0, 0, 0.28);
}

.card-heading {
  margin-bottom: 2px;
}

.card-heading h2 {
  margin: 8px 0 4px;
  color: var(--brand-text);
  font-size: 24px;
  letter-spacing: -0.6px;
}

.card-heading p {
  margin: 0;
  color: var(--brand-muted);
  font-size: 12px;
}

.auth-field {
  display: grid;
  gap: 7px;
  color: var(--brand-text);
  font-size: 12px;
  font-weight: 600;
}

.auth-field > label {
  cursor: pointer;
}

.password-input {
  position: relative;
}

.auth-field input {
  width: 100%;
  height: 46px;
  padding: 0 46px 0 13px;
  border: 1px solid var(--brand-border);
  border-radius: 8px;
  outline: none;
  background: var(--brand-input);
  color: var(--brand-text);
  font: inherit;
  font-weight: 400;
  transition: border-color 160ms ease, box-shadow 160ms ease;
}

.auth-field input::placeholder {
  color: #8193b1;
}

.auth-field input:focus {
  border-color: var(--brand-primary);
  box-shadow: 0 0 0 3px rgba(39, 119, 255, 0.16);
}

.password-toggle {
  position: absolute;
  top: 50%;
  right: 12px;
  display: grid;
  place-items: center;
  padding: 4px;
  transform: translateY(-50%);
  border: 0;
  background: transparent;
  color: var(--brand-muted);
  cursor: pointer;
}

.password-toggle:hover {
  color: var(--brand-text);
}

.password-toggle:focus-visible {
  border-radius: 4px;
  outline: 2px solid var(--brand-primary);
  outline-offset: 2px;
}

.password-toggle svg {
  width: 15px;
  height: 15px;
}

.form-message,
.form-message-spacer {
  min-height: 16px;
  margin: 0;
  font-size: 11px;
  line-height: 1.4;
}

.is-error {
  color: #ff9a9a;
}

.is-success {
  color: #8ce2b1;
}

.auth-submit {
  min-height: 46px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  border: 0;
  border-radius: 8px;
  background: var(--brand-primary);
  color: white;
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.auth-submit:hover:not(:disabled) {
  background: var(--brand-primary-hover);
  transform: translateY(-1px);
}

.auth-submit:disabled {
  cursor: wait;
  opacity: 0.7;
}

.auth-submit svg {
  width: 11px;
}

.auth-switch {
  margin: 0;
  color: var(--brand-muted);
  font-size: 11px;
  text-align: center;
}

.auth-switch button {
  padding: 0;
  border: 0;
  background: none;
  color: #73aaff;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}

.auth-switch button:hover {
  color: white;
}

.auth-footer {
  min-height: 58px;
  padding: 14px clamp(22px, 5vw, 72px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  border-top: 1px solid var(--brand-border);
  color: var(--brand-muted);
  font-size: 10px;
}

@media (max-width: 760px) {
  .auth-main {
    width: min(100% - 40px, 440px);
    padding: 42px 0;
    grid-template-columns: 1fr;
    gap: 28px;
  }

  .auth-intro {
    text-align: center;
  }

  .auth-intro h1 {
    margin-top: 12px;
    font-size: clamp(32px, 8vw, 44px);
  }

  .auth-intro p {
    margin: 0 auto;
    font-size: 13px;
  }
}

@media (max-width: 420px) {
  .auth-header {
    min-height: 70px;
    padding-inline: 16px;
  }

  .auth-brand-icon {
    width: 38px;
    height: 38px;
  }

  .auth-brand-copy small {
    display: none;
  }

  .home-link {
    font-size: 11px;
  }

  .auth-main {
    width: min(100% - 28px, 440px);
    padding: 32px 0;
  }

  .auth-card-shell {
    height: 446px;
  }

  .auth-face {
    padding: 24px 20px;
  }

  .auth-footer {
    align-items: flex-start;
    flex-direction: column;
    gap: 4px;
    padding: 12px 16px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .auth-field input,
  .auth-submit {
    transition-duration: 0.01ms;
  }
}
</style>