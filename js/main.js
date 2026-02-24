/* =================================================================
   PRASHANT AHIRE — PORTFOLIO 2026
   Main JavaScript — Interactions & Scroll Reveals
   ================================================================= */

document.addEventListener('DOMContentLoaded', () => {

  // ── Mobile Menu Toggle ──
  const menuToggle = document.getElementById('menuToggle');
  const nav = document.getElementById('nav');

  if (menuToggle && nav) {
    menuToggle.addEventListener('click', () => {
      menuToggle.classList.toggle('active');
      nav.classList.toggle('active');
    });

    // Close menu when clicking a nav link
    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        menuToggle.classList.remove('active');
        nav.classList.remove('active');
      });
    });
  }

  // ── Scroll Reveal ──
  const revealElements = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -60px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // ── Header Background on Scroll ──
  const header = document.getElementById('header');

  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 80) {
        header.style.background = 'rgba(13, 13, 13, 0.95)';
      } else {
        header.style.background = 'rgba(13, 13, 13, 0.85)';
      }
    }, { passive: true });
  }

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

  // ── Card hover tilt (subtle) ──
  const cards = document.querySelectorAll('.case-card');

  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = (y - centerY) / centerY * -2;
      const rotateY = (x - centerX) / centerX * 2;

      card.style.transform = `translateY(-4px) perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'translateY(0) perspective(1000px) rotateX(0deg) rotateY(0deg)';
    });
  });

});
