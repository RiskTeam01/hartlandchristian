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

    // Slide images are held in data-src: a display:none slide downloads every
    // image up front otherwise, regardless of loading="lazy". Give a slide its
    // images as it is shown, and fetch its neighbours once the browser is idle
    // so the next click is instant without slowing the first paint.
    function load(n) {
      slides[n].querySelectorAll('img[data-src]').forEach(function (img) {
        img.src = img.getAttribute('data-src');
        img.removeAttribute('data-src');
      });
    }
    function warm(i, neighbours) {
      load(i);
      if (!neighbours) return;
      load((i + 1) % slides.length);
      load((i - 1 + slides.length) % slides.length);
    }
    var interacted = false;
    var _go = go;
    go = function (i) { _go(i); warm(index, interacted); interacted = true; };

    root.setAttribute('data-ready', 'true');
    go(0);

    var idle = window.requestIdleCallback || function (fn) { return setTimeout(fn, 2000); };
    idle(function () { warm(index, true); });
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

  /* -------------------------------------------------------- handbook search
     Indexes each section's text once on load, then matches either the whole
     phrase or every word typed. Results name the section, count the hits and
     show the surrounding sentence, and jump to that section when clicked. */
  /* Families search for the words they use at home; the handbook uses its own
     vocabulary. This maps the former onto the latter — "dress code" finds
     Personal Appearance, "snow day" finds cancellations. Each key is matched
     against the query, and its terms are searched as alternatives. Add freely:
     keys may be single words or phrases. */
  var HB_SYNONYMS = {
    'dress code': ['personal appearance', 'clothing', 'modest'],
    'uniform': ['personal appearance', 'clothing'],
    'what to wear': ['personal appearance', 'clothing'],
    'attire': ['personal appearance', 'clothing'],
    'clothes': ['clothing', 'personal appearance'],
    'jewelry': ['earrings', 'piercing'],
    'makeup': ['make-up', 'nail polish'],
    'tattoo': ['tattoo', 'body art'],
    'haircut': ['haircuts', 'hair'],
    'shoes': ['dress shoes', 'sneakers', 'sandals'],

    'late': ['tardy', 'late fee'],
    'lateness': ['tardy'],
    'absent': ['absence', 'excused'],
    'missing school': ['absence', 'excused', 'attendance'],
    'vacation': ['absence', 'excused'],
    'sick': ['ill students', 'illness'],
    'fever': ['ill students', 'fever'],

    'phone': ['cell phones', 'telephone'],
    'cellphone': ['cell phones'],
    'mobile': ['cell phones'],
    'technology': ['electronic devices', 'computer science'],
    'laptop': ['electronic devices'],
    'tablet': ['electronic devices'],
    'ipad': ['electronic devices'],

    'punishment': ['demerit', 'detention', 'discipline'],
    'trouble': ['demerit', 'detention', 'discipline'],
    'bullying': ['hands off', 'fighting', 'conduct'],
    'expelled': ['expulsion'],
    'suspended': ['suspension'],

    'cost': ['tuition', 'fee'],
    'price': ['tuition', 'fee'],
    'money': ['tuition', 'fee', 'payment'],
    'pay': ['payment', 'tuition', 'billing'],
    'billing': ['billing cycle', 'statements'],
    'financial aid': ['discount', 'financial'],
    'scholarship': ['discount', 'financial'],

    'snow day': ['cancellation', 'closings'],
    'closing': ['cancellation', 'closings'],
    'weather': ['cancellation', 'cold weather'],

    'food': ['lunch', 'snack'],
    'cafeteria': ['lunch', 'lunch tables'],
    'eating': ['lunch', 'snack'],

    'sports': ['volleyball', 'basketball', 'athletics'],
    'teams': ['volleyball', 'basketball', 'sports teams'],
    'basketball': ['basketball', 'conquerors sports'],
    'volleyball': ['volleyball', 'conquerors sports'],

    'grades': ['report cards', 'quarter', 'score'],
    'grading': ['report cards', 'score', 'scoring'],
    'report card': ['report cards', 'quarter'],
    'gpa': ['credits', 'report cards'],
    'exam': ['pace test', 'self-test', 'checkup'],
    'quiz': ['checkup', 'self-test'],
    'testing': ['diagnostic testing', 'pace test'],

    'diploma': ['diploma', 'graduation', 'credits'],
    'apply': ['application', 'admissions'],
    'application': ['application', 'admissions'],
    'sign up': ['application', 'admissions'],
    'register': ['registration', 'admissions'],
    'new student': ['transfer students', 'registration', 'probationary'],
    'transferring': ['transfer students'],

    'teacher': ['supervisor', 'monitor'],
    'faculty': ['supervisor', 'monitor', 'administrator'],
    'principal': ['administrator'],
    'staff': ['supervisor', 'monitor', 'administrator'],

    'curriculum': ['curriculum', 'a.c.e.', 'paces'],
    'classes': ['courses', 'curriculum'],
    'subjects': ['courses', 'curriculum'],
    'homework': ['homework'],

    'complaint': ['grievance', 'complaints'],
    'concern': ['grievance', 'reconciliation'],
    'problem': ['grievance', 'conflicts'],

    'parking': ['parking lot', 'vehicles'],
    'driving': ['vehicles', 'transportation'],
    'car': ['vehicles', 'transportation'],
    'bus': ['transportation'],

    'volunteer': ['volunteers', 'snack shop', 'boosters'],
    'fundraising': ['boosters'],
    'field trip': ['field trips'],
    'chapel': ['chapel', 'devotions'],
    'worship': ['devotions', 'chapel'],
    'prayer': ['prayer', 'devotions'],
    'schedule': ['order of the day', 'recess'],
    'hours': ['order of the day'],
    'withdraw': ['withdraw', 'dismissal'],
    'records': ['transcripts', 'medical records'],
    'immunization': ['medical records'],
    'health': ['medical records', 'health']
  };

  function initHandbookSearch() {
    var wrap = document.querySelector('[data-hb-search]');
    if (!wrap) return;
    var sections = Array.prototype.slice.call(document.querySelectorAll('.hb-section'));
    if (!sections.length) return;

    var input = wrap.querySelector('#hb-q');
    var results = wrap.querySelector('#hb-results');
    var count = wrap.querySelector('#hb-search-count');
    var clear = wrap.querySelector('.hb-search__clear');

    // Build the index: collapse whitespace so snippets read cleanly.
    var index = sections.map(function (sec) {
      var h = sec.querySelector('h2');
      var text = (sec.textContent || '').replace(/\s+/g, ' ').trim();
      return {
        id: sec.id,
        title: h ? h.textContent.trim() : sec.id,
        text: text,
        lower: text.toLowerCase()
      };
    });

    wrap.hidden = false;   // only usable with scripting, so reveal it here

    function esc(s) {
      return s.replace(/[&<>"']/g, function (c) {
        return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
      });
    }

    // Words too common to be worth counting on their own — otherwise a query
    // like "what to wear" scores every "to" in the section.
    var STOP = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'can', 'do', 'does',
      'for', 'from', 'how', 'i', 'in', 'is', 'it', 'my', 'of', 'on', 'or', 'our', 'the',
      'to', 'was', 'we', 'what', 'when', 'where', 'which', 'who', 'will', 'with', 'you', 'your'];

    // Where does this entry match, and how often?
    function findHits(entry, phrase, words) {
      var hits = [];
      hits.phrase = false;
      var i = entry.lower.indexOf(phrase);
      while (i !== -1 && hits.length < 200) {
        hits.push([i, i + phrase.length]);
        i = entry.lower.indexOf(phrase, i + phrase.length);
      }
      if (hits.length) { hits.phrase = true; return hits; }
      // no whole-phrase match: require every meaningful word to appear somewhere
      var useful = words.filter(function (w) { return STOP.indexOf(w) === -1 && w.length > 2; });
      if (!useful.length) useful = words;
      var all = useful.every(function (w) { return entry.lower.indexOf(w) !== -1; });
      if (!all) return [];
      useful.forEach(function (w) {
        var j = entry.lower.indexOf(w);
        while (j !== -1 && hits.length < 200) {
          hits.push([j, j + w.length]);
          j = entry.lower.indexOf(w, j + w.length);
        }
      });
      hits.sort(function (a, b) { return a[0] - b[0]; });
      return hits;
    }

    // Which handbook terms should we also look for, given what was typed?
    function synonymTerms(phrase, words) {
      var out = [];
      Object.keys(HB_SYNONYMS).forEach(function (key) {
        var asked = phrase.indexOf(key) !== -1 || words.indexOf(key) !== -1;
        if (!asked) return;
        HB_SYNONYMS[key].forEach(function (t) {
          // skip anything the literal search would already have found
          if (phrase.indexOf(t) !== -1 || out.indexOf(t) !== -1) return;
          out.push(t);
        });
      });
      return out;
    }

    function snippet(entry, hit) {
      var pad = 70;
      var from = Math.max(0, hit[0] - pad);
      var to = Math.min(entry.text.length, hit[1] + pad);
      // don't cut mid-word
      if (from > 0) { var sp = entry.text.indexOf(' ', from); if (sp > -1 && sp < hit[0]) from = sp + 1; }
      if (to < entry.text.length) { var sp2 = entry.text.lastIndexOf(' ', to); if (sp2 > hit[1]) to = sp2; }
      return (from > 0 ? '&hellip;' : '') +
        esc(entry.text.slice(from, hit[0])) +
        '<mark>' + esc(entry.text.slice(hit[0], hit[1])) + '</mark>' +
        esc(entry.text.slice(hit[1], to)) +
        (to < entry.text.length ? '&hellip;' : '');
    }

    function render(q) {
      var phrase = q.trim().toLowerCase().replace(/\s+/g, ' ');
      if (phrase.length < 2) {
        results.hidden = true;
        results.innerHTML = '';
        count.textContent = '';
        input.setAttribute('aria-expanded', 'false');
        clear.hidden = !q;
        return;
      }
      var words = phrase.split(' ').filter(Boolean);
      var matches = [];
      index.forEach(function (entry) {
        var hits = findHits(entry, phrase, words);
        if (hits.length) matches.push({ entry: entry, hits: hits });
      });
      matches.sort(function (a, b) {
        if (a.hits.phrase !== b.hits.phrase) return a.hits.phrase ? -1 : 1;
        return b.hits.length - a.hits.length;
      });

      // Second pass on the handbook's own wording for what was typed.
      var terms = synonymTerms(phrase, words);
      var already = matches.map(function (m) { return m.entry.id; });
      var related = [];
      terms.forEach(function (t) {
        index.forEach(function (entry) {
          if (already.indexOf(entry.id) !== -1) return;
          var at = entry.lower.indexOf(t);
          if (at === -1) return;
          already.push(entry.id);
          related.push({ entry: entry, hit: [at, at + t.length], term: t });
        });
      });

      clear.hidden = false;
      if (!matches.length && !related.length) {
        results.innerHTML = '<li class="hb-results__empty">No sections match &ldquo;' + esc(q.trim()) + '&rdquo;.</li>';
        results.hidden = false;
        count.textContent = 'No matches.';
        input.setAttribute('aria-expanded', 'true');
        return;
      }

      var html = matches.map(function (m) {
        return '<li><a href="#' + m.entry.id + '" data-hb-jump="' + m.entry.id + '">' +
          '<span class="hb-results__title">' + esc(m.entry.title) +
          '<span class="hb-results__n">' + m.hits.length + '</span></span>' +
          '<span class="hb-results__snip">' + snippet(m.entry, m.hits[0]) + '</span>' +
          '</a></li>';
      }).join('');

      if (related.length) {
        html += '<li class="hb-results__group">' +
          (matches.length ? 'Related' : 'The handbook calls this') + '</li>' +
          related.map(function (r) {
            return '<li><a href="#' + r.entry.id + '" data-hb-jump="' + r.entry.id + '">' +
              '<span class="hb-results__title">' + esc(r.entry.title) +
              '<span class="hb-results__n hb-results__n--soft">' + esc(r.term) + '</span></span>' +
              '<span class="hb-results__snip">' + snippet(r.entry, r.hit) + '</span>' +
              '</a></li>';
          }).join('');
      }
      results.innerHTML = html;

      var total = matches.reduce(function (n, m) { return n + m.hits.length; }, 0);
      if (matches.length && related.length) {
        count.textContent = total + ' match' + (total === 1 ? '' : 'es') + ' in ' +
          matches.length + ' section' + (matches.length === 1 ? '' : 's') + ', plus ' +
          related.length + ' related.';
      } else if (matches.length) {
        count.textContent = total + ' match' + (total === 1 ? '' : 'es') + ' in ' +
          matches.length + ' section' + (matches.length === 1 ? '' : 's') + '.';
      } else {
        count.textContent = 'No exact match — showing ' + related.length +
          ' related section' + (related.length === 1 ? '' : 's') + '.';
      }
      results.hidden = false;
      input.setAttribute('aria-expanded', 'true');
    }

    var timer;
    input.addEventListener('input', function () {
      clearTimeout(timer);
      var v = input.value;
      timer = setTimeout(function () { render(v); }, 120);
    });

    clear.addEventListener('click', function () {
      input.value = '';
      render('');
      input.focus();
    });

    input.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { input.value = ''; render(''); }
      if (e.key === 'Enter') {
        e.preventDefault();
        var first = results.querySelector('a');
        if (first) first.click();
      }
    });

    // Flash the section briefly so it is obvious where you landed.
    results.addEventListener('click', function (e) {
      var a = e.target.closest('a[data-hb-jump]');
      if (!a) return;
      var sec = document.getElementById(a.getAttribute('data-hb-jump'));
      if (!sec) return;
      sec.classList.remove('is-target');
      void sec.offsetWidth;
      sec.classList.add('is-target');
      setTimeout(function () { sec.classList.remove('is-target'); }, 1600);
    });
  }

  /* ------------------------------------------------------------------ boot */
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    initNav();
    initBackLink();
    initHandbookSearch();
    document.querySelectorAll('.carousel').forEach(initCarousel);
    document.querySelectorAll('[data-accordion-toggle]').forEach(initAccordion);
  });
})();
