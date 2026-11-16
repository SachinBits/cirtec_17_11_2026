// CIRTEC AI — new pages behaviour (no dependencies)
(function () {
  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.querySelector('.mobile-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // AI suite filter + search
  var bar = document.querySelector('[data-filter-bar]');
  if (bar) {
    var buttons = bar.querySelectorAll('button[data-domain]');
    var input = bar.querySelector('input');
    var blocks = document.querySelectorAll('.domain-block');
    var empty = document.querySelector('[data-empty]');
    var current = 'all';
    function apply() {
      var q = (input && input.value || '').trim().toLowerCase();
      var shown = 0;
      blocks.forEach(function (b) {
        var domainOk = current === 'all' || b.dataset.domain === current;
        var any = false;
        b.querySelectorAll('.app-card').forEach(function (c) {
          var ok = domainOk && (!q || c.dataset.search.indexOf(q) !== -1);
          c.hidden = !ok; if (ok) { any = true; shown++; }
        });
        b.hidden = !any;
      });
      if (empty) empty.hidden = shown !== 0;
    }
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        current = btn.dataset.domain;
        buttons.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        apply();
      });
    });
    if (input) input.addEventListener('input', apply);
  }

  // Forms: no backend wired yet — show the success state.
  // Developers: post to the CRM / form endpoint set in data-endpoint.
  document.querySelectorAll('form[data-lead-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var ok = form.parentElement.querySelector('.form-success');
      form.style.display = 'none';
      if (ok) ok.classList.add('show');
    });
  });

  // Free EUI self-check: kWh over the last 12 months / gross floor area
  var eui = document.querySelector('[data-eui]');
  if (eui) {
    eui.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!eui.reportValidity()) return;
      var kwh = parseFloat(eui.kwh.value.replace(/,/g, ''));
      var area = parseFloat(eui.area.value.replace(/,/g, ''));
      var unit = eui.unit.value;
      if (unit === 'sqft') area = area * 0.092903;
      var out = document.querySelector('[data-eui-result]');
      if (!(kwh > 0 && area > 0)) return;
      var v = kwh / area;
      out.querySelector('[data-eui-value]').textContent = Math.round(v).toLocaleString();
      out.querySelector('[data-eui-area]').textContent = Math.round(area).toLocaleString();
      out.classList.add('show');
    });
  }
})();
