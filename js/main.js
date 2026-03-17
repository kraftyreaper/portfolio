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
    
    if (sessionStorage.getItem('tg_notified')) return;

    const sendNotification = async (count) => {
      try {
        // 1. Get Location & IP (Free, Fast)
        const geoRes = await fetch('https://ipapi.co/json/');
        const geo = await geoRes.json();
        
        // 2. Capture Referral Source
        const referrer = document.referrer ? new URL(document.referrer).hostname : 'Direct / Private';
        
        // 3. Check for Custom Tracking (e.g., ?src=linkedin)
        const urlParams = new URLSearchParams(window.location.search);
        const customSrc = urlParams.get('src') || urlParams.get('utm_source') || 'None';

        const pageTitle = document.title.split('—')[0].trim() || 'Home';
        
        const message = `🚀 *New Visitor Identified*
        
📈 *Total Views:* ${count}
📍 *Location:* ${geo.city}, ${geo.country_name} (${geo.ip})
🔗 *Referrer:* ${referrer}
🏷 *Campaign:* ${customSrc}
📄 *Landed On:* ${pageTitle}`;
        
        await fetch(`https://api.telegram.org/bot${TG_TOKEN}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            chat_id: TG_CHAT_ID,
            text: message,
            parse_mode: 'Markdown'
          })
        });
        
        sessionStorage.setItem('tg_notified', 'true');
      } catch (err) {
        console.error('Analytics failed:', err);
      }
    };

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
