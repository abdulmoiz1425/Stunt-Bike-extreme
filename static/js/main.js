/* Stunt Bike Extreme — Main JS */

/* Mobile nav toggle */
(function () {
  const toggle = document.getElementById('navToggle');
  const nav = document.getElementById('mainNav');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', function () {
    const isOpen = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', isOpen);
    /* Animate hamburger to X */
    const spans = toggle.querySelectorAll('span');
    if (isOpen) {
      spans[0].style.cssText = 'transform:rotate(45deg) translate(5px,6px)';
      spans[1].style.cssText = 'opacity:0';
      spans[2].style.cssText = 'transform:rotate(-45deg) translate(5px,-6px)';
    } else {
      spans.forEach(s => (s.style.cssText = ''));
    }
  });

  /* Close nav on outside click */
  document.addEventListener('click', function (e) {
    if (!nav.contains(e.target) && !toggle.contains(e.target)) {
      nav.classList.remove('open');
      toggle.querySelectorAll('span').forEach(s => (s.style.cssText = ''));
    }
  });
})();

/* FAQ accordion */
function toggleFAQ(btn) {
  const item = btn.closest('.faq-item');
  const isOpen = item.classList.contains('open');

  /* Close all open FAQs */
  document.querySelectorAll('.faq-item.open').forEach(function (el) {
    el.classList.remove('open');
  });

  /* Toggle current */
  if (!isOpen) {
    item.classList.add('open');
  }
}

/* Cookie consent */
(function () {
  const bar = document.getElementById('cookieBar');
  if (!bar) return;
  if (!localStorage.getItem('sbe_cookies_accepted')) {
    bar.classList.add('show');
  }
})();

function acceptCookies() {
  localStorage.setItem('sbe_cookies_accepted', '1');
  const bar = document.getElementById('cookieBar');
  if (bar) {
    bar.style.transition = 'opacity 0.3s';
    bar.style.opacity = '0';
    setTimeout(() => bar.remove(), 300);
  }
}

/* Smooth scroll for anchor links */
document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

/* Auto-dismiss flash messages */
(function () {
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      alert.style.transition = 'opacity 0.5s';
      alert.style.opacity = '0';
      setTimeout(() => alert.remove(), 500);
    }, 5000);
  });
})();

/* Download button feedback */
document.querySelectorAll('.btn-download[href*="/download/"]').forEach(function (btn) {
  btn.addEventListener('click', function () {
    const original = this.innerHTML;
    this.innerHTML = '⏳ Starting Download...';
    this.style.pointerEvents = 'none';
    setTimeout(() => {
      this.innerHTML = original;
      this.style.pointerEvents = '';
    }, 3000);
  });
});
