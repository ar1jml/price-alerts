<template>
  <div class="login-page">
    <header class="site-header">
      <router-link to="/login" class="site-brand" aria-label="PriceTrack home">
        <span class="site-brand-icon">
          <font-awesome-icon icon="tags" />
        </span>
        <span class="site-brand-copy">
          <strong>PriceTrack</strong>
          <small>Smart Price Monitoring</small>
        </span>
      </router-link>

      <nav class="site-nav" aria-label="Main navigation">
        <a class="nav-overview" href="#hero-title">Overview</a>
        <router-link to="/register?mode=signin" class="nav-signin">
          Sign in
        </router-link>
        <router-link to="/register" class="nav-cta">
          Create account
          <font-awesome-icon icon="arrow-right" />
        </router-link>
      </nav>
    </header>

    <main class="login-main">
    <!-- =====================================================
         HERO / PRODUCT INTRO
    ====================================================== -->
    <section class="hero-panel" aria-labelledby="hero-title">
      <div class="hero-content">
        <!-- Hero message -->
        <div class="hero-message">
          <h1 id="hero-title">
            Track Prices.<br />
            Make <span>Smarter Decisions.</span>
          </h1>

          <p>
            Monitor product prices, spot trends, and get real-time
            alerts — all in one place.
          </p>
        </div>

        <div class="hero-actions">
          <router-link to="/register" class="hero-primary-cta">
            Start tracking for free
            <font-awesome-icon icon="arrow-right" />
          </router-link>
        </div>

      </div>
    </section>
    </main>

    <footer class="site-footer">
      <div class="footer-copy">
        <span class="footer-eyebrow">SHOP SMARTER</span>
        <h2>Make every price drop count.</h2>
        <p>Track the products you love and catch the right deal.</p>
      </div>
      <div class="footer-actions">
        <router-link to="/register" class="footer-cta">
          Start tracking for free
          <font-awesome-icon icon="arrow-right" />
        </router-link>
        <a href="#hero-title" class="footer-secondary-cta">
          Explore overview
        </a>
        <router-link to="/register?mode=signin" class="footer-secondary-cta">
          Sign in
          <font-awesome-icon icon="arrow-right" />
        </router-link>
      </div>
    </footer>

  </div>
</template>


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
  --brand-navy: #071a3d;
  --brand-primary: #2777ff;
  --brand-primary-hover: #1768ef;
  --brand-surface: #071a3d;
  --brand-surface-raised: #0b2148;
  --brand-surface-input: #102a52;
  --brand-border: #1d3966;
  --brand-text: #edf4ff;
  --brand-muted: #a9b8d1;

  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  background: var(--brand-surface);
  font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif;
}

.login-main {
  display: grid;
  flex: 1;
  grid-template-columns: 1fr;
}

.site-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;

  min-height: 82px;
  padding: 0 clamp(28px, 5vw, 72px);

  border-bottom: 1px solid var(--brand-border);
  background: var(--brand-surface);
}

.site-brand {
  display: inline-flex;
  align-items: center;
  gap: 11px;

  color: var(--brand-text);
  text-decoration: none;
}

.site-brand-icon {
  width: 42px;
  height: 42px;

  display: flex;
  align-items: center;
  justify-content: center;

  border-radius: 12px;
  background: var(--brand-primary);
  color: #ffffff;
  box-shadow: 0 8px 18px rgba(39, 119, 255, 0.2);
}

.site-brand-icon svg {
  width: 18px;
}

.site-brand-copy {
  display: grid;
  gap: 2px;
}

.site-brand-copy strong {
  font-size: 17px;
  letter-spacing: -0.3px;
}

.site-brand-copy small {
  color: var(--brand-muted);
  font-size: 10px;
}

.site-nav {
  display: flex;
  align-items: center;
  gap: clamp(16px, 2.4vw, 32px);
}

.site-nav > a {
  color: var(--brand-muted);
  font-size: 12px;
  font-weight: 500;
  text-decoration: none;
  transition: color 0.2s;
}

.site-nav > a:hover {
  color: var(--brand-primary);
}

.site-nav .nav-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;

  padding: 11px 16px;
  border: 1px solid var(--brand-border);
  border-radius: 9px;
  background: var(--brand-surface-raised);
  color: var(--brand-primary-hover);
  font-weight: 650;
}

.site-nav .nav-cta:hover {
  border-color: #315486;
  background: var(--brand-surface-input);
}

.nav-cta svg {
  width: 10px;
}

.site-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 28px;

  padding: 30px clamp(28px, 5vw, 72px);

  background: var(--brand-navy);
  color: #ffffff;
}

.footer-copy {
  display: grid;
  gap: 6px;
}

.footer-eyebrow {
  color: #73aaff;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 1.4px;
}

.footer-copy h2 {
  margin: 0;
  font-size: 20px;
  letter-spacing: -0.4px;
}

.footer-copy p {
  margin: 0;
  color: #a9b8d1;
  font-size: 12px;
}

.footer-actions {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.footer-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  min-height: 44px;
  padding: 0 18px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 9px;
  background: var(--brand-primary);
  color: #ffffff;
  font-size: 12px;
  font-weight: 650;
  text-decoration: none;
  white-space: nowrap;
  transition: background 0.2s, transform 0.2s, box-shadow 0.2s;
}

.footer-cta:hover {
  background: var(--brand-primary-hover);
  box-shadow: 0 8px 20px rgba(39, 119, 255, 0.25);
  transform: translateY(-1px);
}

.footer-cta svg {
  width: 11px;
}

.footer-secondary-cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  min-height: 44px;
  padding: 0 18px;
  border: 1px solid var(--brand-border);
  border-radius: 9px;
  background: var(--brand-surface-raised);
  color: var(--brand-text);
  font-size: 12px;
  font-weight: 650;
  text-decoration: none;
  white-space: nowrap;
  transition: background 0.2s, border-color 0.2s;
}

.footer-secondary-cta:hover {
  border-color: #315486;
  background: var(--brand-surface-input);
}

.footer-secondary-cta svg {
  width: 11px;
}


/* =========================================================
   HERO
========================================================= */

.hero-panel {
  min-height: 0;
  min-width: 0;
  background: var(--brand-navy);
  color: #ffffff;
  overflow: hidden;
}

.hero-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: min(100%, 1440px);
  margin: 0 auto;
  padding: 68px clamp(36px, 6vw, 88px);
}


/* Hero message */

.hero-message {
  margin-top: 18px;
  max-width: 650px;
}

.hero-message h1 {
  margin: 0;
  font-size: clamp(38px, 4vw, 58px);
  line-height: 1.05;
  letter-spacing: -2px;
  font-weight: 700;
}

.hero-message h1 span {
  color: var(--brand-primary);
}

.hero-message p {
  max-width: 570px;
  margin: 24px 0 0;

  color: #a9b8d1;
  font-size: 16px;
  line-height: 1.7;
}

.hero-actions {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 18px;

  margin-top: 27px;
}

.hero-primary-cta {
  display: inline-flex;
  align-items: center;
  gap: 10px;

  min-height: 46px;
  font-size: 12px;
  font-weight: 650;
  text-decoration: none;
  transition: background 0.2s, color 0.2s, transform 0.2s;
}

.hero-primary-cta {
  padding: 0 17px;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 9px;
  background: var(--brand-primary);
  color: #ffffff;
  box-shadow: 0 9px 22px rgba(0, 0, 0, 0.18);
}

.hero-primary-cta:hover {
  background: var(--brand-primary-hover);
  transform: translateY(-1px);
}

.hero-actions svg {
  width: 10px;
}


/* =========================================================
   LARGE TABLET
========================================================= */

@media (max-width: 1200px) {

  .hero-content {
    padding: 45px;
  }

}


/* =========================================================
   TABLET
========================================================= */

@media (max-width: 992px) {

  .login-main {
    grid-template-columns: 1fr;
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

}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 768px) {

  .site-header {
    min-height: 72px;
    padding: 0 20px;
  }

  .site-nav {
    gap: 12px;
  }

  .site-nav > a:not(.nav-cta):not(.nav-signin) {
    display: none;
  }

  .login-main {
    display: block;
  }


  /* HERO */

  .hero-content {
    padding: 32px 20px 35px;
  }

  .hero-message {
    margin-top: 0;
    margin-bottom: 0;
  }

  .hero-actions {
    margin-top: 22px;
  }

  .hero-message h1 {
    font-size: 38px;
    line-height: 1.08;
    letter-spacing: -1.5px;
  }

  .hero-message p {
    margin-top: 18px;

    font-size: 14px;
    line-height: 1.65;
  }


  .site-footer {
    align-items: flex-start;
    flex-direction: column;
    gap: 18px;
    padding: 26px 20px;
  }

  .footer-cta {
    min-height: 42px;
  }

}


/* =========================================================
   SMALL MOBILE
========================================================= */

@media (max-width: 480px) {

  .site-header {
    min-height: 66px;
    padding: 0 16px;
  }

  .site-brand-icon {
    width: 38px;
    height: 38px;
  }

  .site-brand-copy small {
    display: none;
  }

  .site-nav .nav-cta {
    padding: 9px 11px;
    font-size: 11px;
  }

  .site-nav .nav-signin {
    font-size: 11px;
  }

  .site-footer {
    padding: 24px 16px;
  }

  .footer-copy h2 {
    font-size: 18px;
  }

  .footer-copy p {
    font-size: 11px;
  }

  .hero-content {
    padding: 28px 16px 30px;
  }

  .hero-message h1 {
    font-size: 32px;
  }

  .hero-message p {
    font-size: 13px;
  }

  .hero-actions {
    align-items: stretch;
    flex-direction: column;
    gap: 8px;
    max-width: 280px;
  }

  .hero-primary-cta {
    justify-content: center;
  }

}


/* =========================================================
   VERY SMALL PHONES
========================================================= */

@media (max-width: 360px) {

  .hero-message h1 {
    font-size: 29px;
  }

}

</style>