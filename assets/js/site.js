/* Hartland Christian School — progressive enhancement.
   Everything below is additive: with JS off the nav is a plain list,
   carousels show every slide stacked, and the accordion stays open. */
(function () {
  'use strict';

  /* ------------------------------------------------------------ mobile nav */
  function initNav() {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.getElementById('site-nav');
    var close = document.querySelector('.nav-close');
    if (!toggle || !nav) return;

    function setOpen(open) {
      nav.setAttribute('data-open', open ? 'true' : 'false');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
      if (open) {
        var first = nav.querySelector('a');
        if (first) first.focus();
      } else {
        toggle.focus();
      }
    }

    toggle.addEventListener('click', function () {
      setOpen(nav.getAttribute('data-open') !== 'true');
    });
    if (close) close.addEventListener('click', function () { setOpen(false); });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.getAttribute('data-open') === 'true') setOpen(false);
    });
    // Reset when resizing back up to the desktop bar.
    window.addEventListener('resize', function () {
      if (window.innerWidth > 900 && nav.getAttribute('data-open') === 'true') {
        nav.setAttribute('data-open', 'false');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
  }

  /* ------------------------------------------------------------- carousels */
  function initCarousel(root) {
    var track = root.querySelector('.carousel__track');
    var slides = Array.prototype.slice.call(root.querySelectorAll('.carousel__slide'));
    if (!track || slides.length < 2) return;

    var fade = root.getAttribute('data-fade') === 'true';
    var index = 0;
    var dotsWrap = root.querySelector('.carousel__dots');
    var dots = [];

    if (dotsWrap) {
      slides.forEach(function (slide, i) {
        var b = document.createElement('button');
        b.type = 'button';
        b.setAttribute('role', 'tab');
        b.setAttribute('aria-label', 'Show slide ' + (i + 1) + ' of ' + slides.length);
        b.addEventListener('click', function () { go(i); });
        dotsWrap.appendChild(b);
        dots.push(b);
      });
      dotsWrap.setAttribute('role', 'tablist');
    }

    function go(i) {
      index = (i + slides.length) % slides.length;
      if (fade) {
        slides.forEach(function (s, n) {
          s.setAttribute('data-active', n === index ? 'true' : 'false');
        });
      } else {
        track.style.transform = 'translateX(' + (-100 * index) + '%)';
      }
      slides.forEach(function (s, n) {
        s.setAttribute('aria-hidden', n === index ? 'false' : 'true');
        // keep offscreen slides out of the tab order
        s.querySelectorAll('a, button, iframe').forEach(function (el) {
          if (n === index) el.removeAttribute('tabindex');
          else el.setAttribute('tabindex', '-1');
        });
      });
      dots.forEach(function (d, n) {
        d.setAttribute('aria-selected', n === index ? 'true' : 'false');
      });
    }

    var prev = root.querySelector('.carousel__btn--prev');
    var next = root.querySelector('.carousel__btn--next');
    if (prev) prev.addEventListener('click', function () { go(index - 1); });
    if (next) next.addEventListener('click', function () { go(index + 1); });

    root.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { go(index - 1); }
      else if (e.key === 'ArrowRight') { go(index + 1); }
    });

    // touch swipe
    var x0 = null;
    root.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    root.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 45) go(index + (dx < 0 ? 1 : -1));
      x0 = null;
    }, { passive: true });

    root.setAttribute('data-ready', 'true');
    go(0);
  }

  /* ------------------------------------------------------------- accordion */
  function initAccordion(btn) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;
    // Collapse only once JS is available, so no-JS readers still get the text.
    btn.setAttribute('aria-expanded', 'false');
    panel.setAttribute('data-open', 'false');
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      panel.setAttribute('data-open', open ? 'false' : 'true');
    });
  }

  /* ----------------------------------------------------------- message form
     The original posted to Showit's contact-form service. That endpoint goes
     away with Showit, so rather than silently swallowing a parent's message
     this hands off to the school's mailbox and then shows the same thank-you
     state the original did. Replace with a real form handler when one exists. */
  function initForm() {
    var form = document.getElementById('tuition-form');
    if (!form) return;
    var field = document.getElementById('tuition-message');
    var status = document.getElementById('tuition-form-status');
    var thanks = document.getElementById('tuition-form-thanks');

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = (field.value || '').trim();
      if (!msg) {
        status.textContent = 'Please enter a message before sending.';
        field.focus();
        return;
      }
      status.textContent = '';
      window.location.href = 'mailto:hartlandchristianschool@outlook.com'
        + '?subject=' + encodeURIComponent('Tuition enquiry from the website')
        + '&body=' + encodeURIComponent(msg);
      form.hidden = true;
      thanks.hidden = false;
    });
  }

  /* ---------------------------------------------------------- back link
     The handbook is linked from both /contact and /about, so point the back
     link at whichever one the reader actually came from. Falls back to the
     href already in the markup when there is no usable referrer. */
  function initBackLink() {
    var link = document.getElementById('hb-back');
    if (!link || !document.referrer) return;
    var from;
    try { from = new URL(document.referrer); } catch (e) { return; }
    if (from.origin !== window.location.origin) return;

    var known = { '/about': 'about', '/contact': 'contact', '/admissions': 'admissions' };
    var path = from.pathname.replace(/\/index\.html$/, '').replace(/\/$/, '') || '/';
    if (!known[path]) return;
    link.setAttribute('href', path);
    var label = link.querySelector('.back-link__label');
    if (label) label.textContent = 'back to ' + known[path];
  }

  /* ------------------------------------------------------------------ boot */
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    initNav();
    initForm();
    initBackLink();
    document.querySelectorAll('.carousel').forEach(initCarousel);
    document.querySelectorAll('[data-accordion-toggle]').forEach(initAccordion);
  });
})();
