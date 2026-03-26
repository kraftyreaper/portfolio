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
    window.__lenis = lenis;

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
        // 1. Get Location (Free, Fast)
        const geoRes = await fetch('https://ipapi.co/json/');
        const geo = await geoRes.json();
        
        const pageTitle = document.title.split('—')[0].trim() || 'Home';
        
        // 2. Format simplified message
        const message = `🚀 *New Visitor Identified*
        
📈 *Total Views:* ${count}
📍 *Location:* ${geo.city}, ${geo.region}, ${geo.country_name}
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

  // ── Feedback System ──
  (function () {
    const TG_TOKEN = '8718526798:AAFwmoebK66Cc0-IndVDpwsOM7Geuh66KzI';
    const TG_CHAT_ID = '7222053587';

    const pageTitle = document.title.split('—')[0].trim() || 'Portfolio';
    const pageUrl = window.location.href;
    const isCaseStudy = window.location.pathname.includes('/case-studies/');

    // Map URL slug to exact case study names
    const csNameMap = {
      'testlify':          'Testlify',
      'homes-collection':  'Homes collection',
      'gray-institute':    'Gray Institute',
      'milestone':         'Milestone',
      'asvi-thoughtworks': 'ASVI Thoughtworks'
    };
    const slug = Object.keys(csNameMap).find(k => window.location.pathname.includes(k));
    const csLabel = slug ? `Case study - ${csNameMap[slug]}` : null;
    const defaultTopic = isCaseStudy && csLabel ? csLabel : 'Portfolio overall';

    // ── Inject modal HTML ──
    const modalHtml = `
      <div class="feedback-overlay" id="feedbackOverlay" role="dialog" aria-modal="true" aria-label="Share Feedback">
        <div class="feedback-modal" id="feedbackModal" data-lenis-prevent>
          <button class="feedback-modal__close" id="feedbackClose" aria-label="Close">&#x2715;</button>

          <div class="feedback-modal__header">
            <p class="feedback-modal__eyebrow">Anonymous &middot; No login required</p>
            <h2 class="feedback-modal__title">Your honest take.</h2>
            <p class="feedback-modal__subtitle">What worked? What didn&rsquo;t? Your perspective helps me improve &mdash; be as candid as you like.</p>
          </div>

          <span class="feedback-topic-label">What&rsquo;s your feedback about?</span>
          <div class="feedback-topic-chips" id="feedbackTopics">
            ${isCaseStudy && csLabel ? `<button class="feedback-chip selected" data-topic="${csLabel}">${csLabel}</button>` : ''}
            <button class="feedback-chip${!isCaseStudy ? ' selected' : ''}" data-topic="Portfolio overall">Portfolio overall</button>
            <button class="feedback-chip" data-topic="Something else">Something else</button>
          </div>

          <label class="feedback-textarea-label" for="feedbackText">Your feedback</label>
          <textarea class="feedback-textarea" id="feedbackText" maxlength="5000"
            placeholder="Tell me what works, what doesn&rsquo;t, and why. The more specific, the more helpful."></textarea>
          <div class="feedback-char-count"><span id="feedbackCharCount">0</span> / 5000</div>

          <label class="feedback-optional-label" for="feedbackContact">Contact — optional</label>
          <input class="feedback-optional-input" id="feedbackContact" type="text" maxlength="200"
            placeholder="Name, LinkedIn, or email" />

          <button class="feedback-submit-btn" id="feedbackSubmit">Send Feedback</button>

          <p class="feedback-modal__linkedin">
            Prefer a direct conversation?&nbsp;
            <a href="https://www.linkedin.com/in/prashantuxuidesign/" target="_blank" rel="noopener noreferrer">DM me on LinkedIn &rarr;</a>
          </p>
        </div>
      </div>
      <div class="feedback-toast" id="feedbackToast">&#x2705; Feedback sent &mdash; thank you!</div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHtml);

    // ── Inject footer trigger button ──
    const actionRight = document.querySelector('.site-footer__action-right');
    if (actionRight) {
      const feedbackBtn = document.createElement('button');
      feedbackBtn.className = 'feedback-footer-btn';
      feedbackBtn.id = 'feedbackTrigger';
      feedbackBtn.setAttribute('aria-label', 'Share feedback about this portfolio');
      feedbackBtn.innerHTML = `
        Share Feedback
        <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none"
          stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
        </svg>
      `;
      actionRight.prepend(feedbackBtn);

      // Extend custom cursor hover to new button
      feedbackBtn.addEventListener('mouseenter', () => {
        const cur = document.querySelector('.custom-cursor');
        if (cur) cur.classList.add('active');
      });
      feedbackBtn.addEventListener('mouseleave', () => {
        const cur = document.querySelector('.custom-cursor');
        if (cur) cur.classList.remove('active');
      });
    }

    // ── References ──
    const overlay   = document.getElementById('feedbackOverlay');
    const closeBtn  = document.getElementById('feedbackClose');
    const textarea  = document.getElementById('feedbackText');
    const charCount = document.getElementById('feedbackCharCount');
    const submitBtn = document.getElementById('feedbackSubmit');
    const toast     = document.getElementById('feedbackToast');
    const contactInput = document.getElementById('feedbackContact');
    let selectedTopic = defaultTopic;

    // ── Open / Close ──
    function openModal() {
      overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
      if (window.__lenis) window.__lenis.stop();
      setTimeout(() => textarea && textarea.focus(), 320);
    }

    function closeModal() {
      overlay.classList.remove('open');
      document.body.style.overflow = '';
      if (window.__lenis) window.__lenis.start();
    }

    const trigger = document.getElementById('feedbackTrigger');
    if (trigger) trigger.addEventListener('click', openModal);

    closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', (e) => { if (e.target === overlay) closeModal(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });

    // ── Topic chips ──
    document.querySelectorAll('.feedback-chip').forEach((chip) => {
      chip.addEventListener('click', () => {
        document.querySelectorAll('.feedback-chip').forEach((c) => c.classList.remove('selected'));
        chip.classList.add('selected');
        selectedTopic = chip.dataset.topic;
      });
    });

    // ── Char counter ──
    textarea.addEventListener('input', () => {
      charCount.textContent = textarea.value.length;
    });

    // ── Toast ──
    function showToast() {
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 4000);
    }

    // ── Send to Telegram ──
    async function sendFeedbackToTelegram(topic, text, contact) {
      const contactLine = contact.trim() ? contact.trim() : 'Not provided';
      const message =
        `\u{1F4AC} *New Portfolio Feedback*\n` +
        `\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n` +
        `\u{1F4C4} *Page:* ${pageTitle}\n` +
        `\u{1F4CC} *Topic:* ${topic}\n` +
        `\u{1F4DD} *Feedback:*\n${text}\n\n` +
        `\u{1F464} *Contact:* ${contactLine}\n` +
        `\u{1F517} *URL:* ${pageUrl}`;

      try {
        await fetch(`https://api.telegram.org/bot${TG_TOKEN}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            chat_id: TG_CHAT_ID,
            text: message,
            parse_mode: 'Markdown'
          })
        });
      } catch (err) {
        console.error('Feedback send failed:', err);
      }
    }

    // ── Submit ──
    submitBtn.addEventListener('click', async () => {
      const text = textarea.value.trim();

      if (!text) {
        textarea.focus();
        textarea.style.borderColor = 'rgba(255, 80, 80, 0.5)';
        setTimeout(() => { textarea.style.borderColor = ''; }, 2000);
        return;
      }

      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending\u2026';

      await sendFeedbackToTelegram(selectedTopic, text, contactInput.value || '');

      // Reset form
      textarea.value = '';
      charCount.textContent = '0';
      contactInput.value = '';
      submitBtn.disabled = false;
      submitBtn.textContent = 'Send Feedback';

      closeModal();
      showToast();
    });
  })();

});
