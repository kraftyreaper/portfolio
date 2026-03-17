/* =================================================================
   PRASHANT AHIRE — PORTFOLIO 2026
   Main JavaScript — interactions & Scroll Reveals
   ================================================================= */

document.addEventListener('DOMContentLoaded', () => {

  // ── Scroll Progress Bar ──
  const progressBar = document.createElement('div');
  progressBar.className = 'progress-bar';
  document.body.appendChild(progressBar);

  window.addEventListener('scroll', () => {
    const windowScroll = document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (windowScroll / height) * 100;
    progressBar.style.width = scrolled + '%';
  }, { passive: true });

  // ── Optimized Scroll Reveal ──
  const revealElements = document.querySelectorAll('.reveal, .stagger-reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1, // Sooner appearance
    rootMargin: '0px 0px -40px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // ── Header Appearance ──
  const header = document.getElementById('header');

  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.style.background = 'rgba(13, 13, 13, 0.9)';
        header.style.backdropFilter = 'blur(10px)';
      } else {
        header.style.background = 'transparent';
        header.style.backdropFilter = 'none';
      }
    }, { passive: true });
  }

  // ── Card Hover Spotlight ──
  const cards = document.querySelectorAll('.case-card');

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
    });
  });

  // ── Tabs Logic ──
  const tabButtons = document.querySelectorAll('.case-tabs__btn');
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.getAttribute('data-tab');
      const tabsGroup = btn.closest('.case-section');

      tabsGroup.querySelectorAll('.case-tabs__btn').forEach(b => b.classList.remove('active'));
      tabsGroup.querySelectorAll('.case-tabs__pane').forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPane = tabsGroup.querySelector(tabId);
      if (targetPane) targetPane.classList.add('active');
    });
  });

  // ── Carousel Logic ──
  const carousels = document.querySelectorAll('.case-carousel');
  carousels.forEach(carousel => {
    const track = carousel.querySelector('.case-carousel__track');
    const slides = carousel.querySelectorAll('.case-carousel__slide');
    const btnPrev = carousel.querySelector('.case-carousel__btn--prev');
    const btnNext = carousel.querySelector('.case-carousel__btn--next');

    if (!track || slides.length === 0) return;

    let currentIndex = 0;

    function updateCarousel() {
      track.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    if (btnPrev) {
      btnPrev.addEventListener('click', () => {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : slides.length - 1;
        updateCarousel();
      });
    }

    if (btnNext) {
      btnNext.addEventListener('click', () => {
        currentIndex = (currentIndex < slides.length - 1) ? currentIndex + 1 : 0;
        updateCarousel();
      });
    }
  });

  // ── Lenis Smooth Scroll ──
  if (typeof Lenis !== 'undefined') {
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: 'vertical',
      smoothWheel: true,
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
  }

  // ── Custom Cursor ──
  const cursor = document.createElement('div');
  cursor.className = 'custom-cursor';
  document.body.appendChild(cursor);

  window.addEventListener('mousemove', (e) => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
  });

  document.querySelectorAll('a, button, .case-card').forEach(el => {
    el.addEventListener('mouseenter', () => cursor.classList.add('active'));
    el.addEventListener('mouseleave', () => cursor.classList.remove('active'));
  });

  // ── Magnetic Buttons ──
  const magnets = document.querySelectorAll('.header__link, .site-footer__link');
  magnets.forEach((magnet) => {
    magnet.addEventListener('mousemove', (e) => {
      const bound = magnet.getBoundingClientRect();
      const x = (e.clientX - bound.left) - bound.width / 2;
      const y = (e.clientY - bound.top) - bound.height / 2;
      magnet.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
    });

    magnet.addEventListener('mouseleave', () => {
      magnet.style.transform = `translate(0px, 0px)`;
    });
  });

  // ── Telegram Visitor Notification ──
  (function() {
    const TG_TOKEN = '8718526798:AAFwmoebK66Cc0-IndVDpwsOM7Geuh66KzI';
    const TG_CHAT_ID = '7222053587';
    const LEGACY_OFFSET = 627; // Baseline from GitHub Insights
    
    // Check if we've already notified for this session
    if (sessionStorage.getItem('tg_notified')) {
      // Even if already notified, let's keep the footer updated with the offset
      const checkFooter = setInterval(() => {
        const countEl = document.getElementById('busuanzi_value_site_pv');
        if (countEl && countEl.innerText !== '—') {
          clearInterval(checkFooter);
          const totalCount = parseInt(countEl.innerText) + LEGACY_OFFSET;
          countEl.innerText = totalCount.toLocaleString();
        }
      }, 500);
      return;
    }

    // Function to send message
    const sendNotification = (count) => {
      const totalCount = parseInt(count) + LEGACY_OFFSET;
      const pageTitle = document.title.split('—')[0].trim() || 'Home';
      const message = `🚀 *New Visitor Identified*\n\n📈 *Total Views:* ${totalCount}\n🔗 *Source:* ${pageTitle}\n📍 *URL:* ${window.location.href}`;
      
      fetch(`https://api.telegram.org/bot${TG_TOKEN}/sendMessage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chat_id: TG_CHAT_ID,
          text: message,
          parse_mode: 'Markdown'
        })
      }).then(() => {
        sessionStorage.setItem('tg_notified', 'true');
        // Update the visible footer count with the offset
        const countEl = document.getElementById('busuanzi_value_site_pv');
        if (countEl) countEl.innerText = totalCount.toLocaleString();
      }).catch(err => console.error('TG Notification failed:', err));
    };

    // Wait for Busuanzi to populate the count
    let attempts = 0;
    const checkBusuanzi = setInterval(() => {
      const countEl = document.getElementById('busuanzi_value_site_pv');
      const count = countEl ? countEl.innerText : null;
      
      if (count && count !== '—') {
        clearInterval(checkBusuanzi);
        sendNotification(count);
      }
      
      if (++attempts > 20) clearInterval(checkBusuanzi);
    }, 500);
  })();

});
