/* =================================================================
   PRASHANT AHIRE — PORTFOLIO 2026
   Main JavaScript — Interactions & Scroll Reveals
   ================================================================= */

document.addEventListener('DOMContentLoaded', () => {

  // ── Page Fade In ──
  document.body.style.opacity = '0';
  document.body.style.transition = 'opacity 0.6s ease';
  requestAnimationFrame(() => {
    document.body.style.opacity = '1';
  });

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

  // ── Scroll Reveal ──
  const revealElements = document.querySelectorAll('.reveal, .stagger-reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // ── Header Background on Scroll ──
  const header = document.getElementById('header');

  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.style.background = 'rgba(13, 13, 13, 0.9)';
        header.style.backdropFilter = 'blur(10px)';
        header.classList.add('header--scrolled');
      } else {
        header.style.background = 'transparent';
        header.style.backdropFilter = 'none';
        header.classList.remove('header--scrolled');
      }
    }, { passive: true });
  }

  // ── Magnetic Buttons/Links ──
  const magneticElements = document.querySelectorAll('.header__link, .site-footer__link, .case-tabs__btn');

  magneticElements.forEach(el => {
    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;

      el.style.transform = `translate(${x * 0.3}px, ${y * 0.5}px)`;
    });

    el.addEventListener('mouseleave', () => {
      el.style.transform = 'translate(0, 0)';
    });
  });

  // ── Smooth scroll for scroll indicator ──
  const scrollX = document.querySelector('.hero__scroll-x');
  const scrollArrow = document.querySelector('.hero__scroll-arrow');
  const caseStudies = document.getElementById('case-studies');

  function scrollToProjects() {
    if (caseStudies) {
      caseStudies.scrollIntoView({ behavior: 'smooth' });
    }
  }

  if (scrollX) scrollX.addEventListener('click', scrollToProjects);
  if (scrollArrow) scrollArrow.addEventListener('click', scrollToProjects);

  // ── Card Hover Effects ──
  const cards = document.querySelectorAll('.case-card');

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = (y - centerY) / centerY * -3;
      const rotateY = (x - centerX) / centerX * 3;

      card.style.transform = `translateY(-8px) perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'translateY(0) perspective(1000px) rotateX(0deg) rotateY(0deg)';
    });
  });

  // ── Tabs Logic ──
  const tabButtons = document.querySelectorAll('.case-tabs__btn');
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.getAttribute('data-tab');
      const tabsGroup = btn.closest('.case-section');

      // Remove active from all buttons and panes in this group
      tabsGroup.querySelectorAll('.case-tabs__btn').forEach(b => b.classList.remove('active'));
      tabsGroup.querySelectorAll('.case-tabs__pane').forEach(p => p.classList.remove('active'));

      // Add active to current button and target pane
      btn.classList.add('active');
      const targetPane = tabsGroup.querySelector(tabId);
      if (targetPane) targetPane.classList.add('active');
    });
  });

  // ── Carousel ── (Kept logic but ensured it interacts well)
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

});
