/* Swapnil Kumar — site behaviour */
(function () {
  'use strict';

  /* --- mobile nav --- */
  var toggle = document.querySelector('.nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    document.querySelectorAll('.nav-links a').forEach(function (a) {
      a.addEventListener('click', function () {
        document.body.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* --- scroll reveal --- */
  var targets = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && targets.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        var delay = parseInt(el.getAttribute('data-reveal-delay') || '0', 10);
        setTimeout(function () { el.classList.add('is-in'); }, delay);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    targets.forEach(function (t) { io.observe(t); });
  } else {
    targets.forEach(function (t) { t.classList.add('is-in'); });
  }

  /* --- animated stat counters --- */
  var figures = document.querySelectorAll('[data-count]');
  function animate(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var dur = 1100;
    var start = null;
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window && figures.length) {
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        animate(e.target);
        io2.unobserve(e.target);
      });
    }, { threshold: 0.5 });
    figures.forEach(function (f) { io2.observe(f); });
  } else {
    figures.forEach(function (f) { f.textContent = f.getAttribute('data-count') + (f.getAttribute('data-suffix') || ''); });
  }

  /* --- contact form (front-end only) --- */
  var form = document.querySelector('.form');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var status = form.querySelector('.form-status');
      var data = new FormData(form);
      var subject = encodeURIComponent('Website enquiry from ' + (data.get('name') || 'a visitor'));
      var body = encodeURIComponent(
        'Name: ' + (data.get('name') || '') + '\n' +
        'Email: ' + (data.get('email') || '') + '\n' +
        'Organisation: ' + (data.get('organisation') || '') + '\n\n' +
        (data.get('message') || '')
      );
      if (status) status.textContent = 'Opening your email client…';
      window.location.href = 'mailto:swapnil.kumar22@alumni.imperial.ac.uk?subject=' + subject + '&body=' + body;
    });
  }

  /* --- footer year --- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
