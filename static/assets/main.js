/* Biggsmash Outreach â€” shared chrome + scroll engine
   data-reveal="up|right|left|zoom"  one-shot reveal when entering view (data-i = stagger index)
   data-slide="right|left"           scroll-linked slide-in (reverses when scrolling back up)
   data-flip                         tile revolves 360Â° on Y as it scrolls into view
   data-spin="turns" [data-scope=page]  rotates with scroll (360Â° per turn)
   data-counter-spin="turns"         counter-rotation so labels stay upright
   data-parallax="speed"             vertical depth offset (negative = slower than page)
   data-drift="px"                   horizontal drift with scroll (marquees)
   data-grow                         scaleX 0â†’1 as the section scrolls through
   data-words                        words light up as you scroll
*/
const $ = (s, r = document) => [...r.querySelectorAll(s)];
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const easeOut = (t) => 1 - Math.pow(1 - t, 3);
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- section dots ---------- */
const secs = $('main > section');
const dots = document.getElementById('dots');
secs.forEach((s, i) => {
  const b = document.createElement('button'); b.setAttribute('aria-label', 'Section ' + (i + 1));
  b.onclick = () => s.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
  dots.appendChild(b);
});

/* ---------- mobile navigation ---------- */
(() => {
  const toggle = document.getElementById('navToggle');
  const menu = document.getElementById('mobileNav');
  const closeBtn = document.getElementById('navClose');
  if (!toggle || !menu) return;

  const open = () => {
    menu.classList.add('open');
    menu.setAttribute('aria-hidden', 'false');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Close menu');
    document.body.classList.add('menu-open');
    if (closeBtn) closeBtn.focus();
  };
  const close = () => {
    menu.classList.remove('open');
    menu.setAttribute('aria-hidden', 'true');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open menu');
    document.body.classList.remove('menu-open');
    if (menu.contains(document.activeElement)) toggle.focus();
  };

  toggle.addEventListener('click', open);
  if (closeBtn) closeBtn.addEventListener('click', close);
  menu.querySelectorAll('a').forEach((a) => a.addEventListener('click', close));
  menu.addEventListener('click', (e) => { if (e.target === menu) close(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
  addEventListener('resize', () => { if (innerWidth > 960) close(); });
})();

/* ---------- one-shot reveals ---------- */
$('[data-i]').forEach((el) => el.style.setProperty('--i', el.dataset.i));
const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.18, rootMargin: '0px 0px -6% 0px' });
$('[data-reveal], .mask').forEach((el) => io.observe(el));
// hero lines play on load
requestAnimationFrame(() => setTimeout(() => $('.hero2 [data-reveal], .hero2 .mask').forEach((el) => el.classList.add('in')), 120));

/* ---------- counters ---------- */
const cio = new IntersectionObserver((es) => es.forEach((e) => {
  if (!e.isIntersecting) return; cio.unobserve(e.target);
  const el = e.target, to = +el.dataset.count, t0 = performance.now(), d = 1400;
  const tick = (t) => { const p = clamp((t - t0) / d); el.textContent = Math.round(to * easeOut(p)); if (p < 1) requestAnimationFrame(tick); };
  requestAnimationFrame(tick);
}), { threshold: 0.6 });
$('[data-count]').forEach((el) => cio.observe(el));

/* ---------- word-by-word statement ---------- */
$('[data-words]').forEach((el) => {
  el.innerHTML = el.textContent.trim().split(/\s+/).map((w) => `<span class="w${/^(360Â°|one|roof\.?)$/i.test(w) ? ' sig' : ''}">${w}</span>`).join(' ');
});

/* ---------- horizontal pinned sections ---------- */
const hs = $('.hscroll');
const sizeH = () => hs.forEach((h) => {
  if (innerWidth <= 960) { h.style.height = ''; return; }
  const tr = h.querySelector('.htrack');
  h.style.height = (tr.scrollWidth - innerWidth + innerHeight * 1.1) + 'px';
});
addEventListener('resize', sizeH); addEventListener('load', sizeH); sizeH();

/* ---------- scroll loop ---------- */
const nav = document.getElementById('nav'), bar = document.getElementById('bar');
const par = $('[data-parallax]'), spin = $('[data-spin]'), cspin = $('[data-counter-spin]'), drift = $('[data-drift]'),
  flips = $('[data-flip]'), slides = $('[data-slide]'), grows = $('[data-grow]'), words = $('[data-words]');
let lastY = 0, ticking = false;

function frame() {
  ticking = false;
  const vh = innerHeight, y = scrollY, doc = document.documentElement.scrollHeight - vh;
  bar.style.transform = `scaleX(${doc > 0 ? y / doc : 0})`;
  nav.classList.toggle('stuck', y > 40);
  nav.classList.toggle('hide', y > lastY && y > 400 && !matchMedia('(hover:none)').matches ? true : (y < lastY ? false : nav.classList.contains('hide')));
  lastY = y;

  // active section dot
  let act = 0; secs.forEach((s, i) => { if (s.getBoundingClientRect().top < vh * 0.5) act = i; });
  [...dots.children].forEach((b, i) => b.classList.toggle('on', i === act));
  if (reduce) return;

  const prog = (el, r) => (vh - r.top) / (vh + r.height);

  par.forEach((el) => { const r = el.getBoundingClientRect(); if (r.bottom < -200 || r.top > vh + 200) return; el.style.transform = `translate3d(0,${(prog(el, r) - 0.5) * -parseFloat(el.dataset.parallax) * vh}px,0)`; });

  spin.forEach((el) => {
    const r = el.getBoundingClientRect(); const turns = parseFloat(el.dataset.spin);
    const p = el.dataset.scope === 'page' ? (doc > 0 ? y / Math.min(doc, vh * 3) : 0) : clamp(prog(el, r));
    el.style.transform = `rotate(${clamp(p, 0, 1) * 360 * turns}deg)`;
  });
  cspin.forEach((el) => {
    const host = el.closest('[data-spin]'); const turns = parseFloat(host.dataset.spin);
    const p = host.dataset.scope === 'page' ? clamp(y / Math.min(doc, vh * 3)) : clamp(prog(host, host.getBoundingClientRect()));
    el.style.transform = `rotate(${-p * 360 * turns}deg)`;
  });

  drift.forEach((el) => { const r = el.parentElement.getBoundingClientRect(); if (r.bottom < 0 || r.top > vh) return; el.style.transform = `translate3d(${(prog(el, r) - 0.5) * parseFloat(el.dataset.drift)}px,0,0)`; });

  flips.forEach((el, i) => {
    const r = el.getBoundingClientRect(); const idx = +(el.dataset.i || 0);
    const e = clamp((vh * 0.95 - r.top - idx * 40) / (vh * 0.55));
    el.style.transform = `rotateY(${(1 - easeOut(e)) * 360}deg) translateY(${(1 - e) * 40}px)`; el.style.opacity = clamp(e * 2.2);
  });

  const compactAnim = innerWidth <= 1024;
  slides.forEach((el) => {
    const r = el.getBoundingClientRect(); const dir = el.dataset.slide === 'left' ? -1 : 1;
    const e = clamp((vh * 0.92 - r.top) / (vh * 0.5));
    el.style.transform = compactAnim
      ? `translate3d(0,${(1 - easeOut(e)) * 40}px,0)`
      : `translate3d(${(1 - easeOut(e)) * 260 * dir}px,0,0)`;
    el.style.opacity = easeOut(e);
  });

  grows.forEach((el) => { const r = el.parentElement.getBoundingClientRect(); el.style.transform = `scaleX(${clamp((vh * 0.8 - r.top) / (r.height + vh * 0.2))})`; });

  words.forEach((el) => {
    const r = el.getBoundingClientRect(); const p = clamp((vh * 0.85 - r.top) / (r.height + vh * 0.35));
    const ws = el.children; const n = Math.round(p * ws.length); for (let i = 0; i < ws.length; i++) ws[i].classList.toggle('on', i < n);
  });

  hs.forEach((h) => {
    if (innerWidth <= 960) return;
    const tr = h.querySelector('.htrack'), r = h.getBoundingClientRect();
    const p = clamp(-r.top / (h.offsetHeight - vh)); tr.style.transform = `translate3d(${-p * (tr.scrollWidth - innerWidth)}px,0,0)`;
    const pr = h.querySelector('.hprog i'); if (pr) pr.style.transform = `scaleX(${p})`;
  });
}
const kick = () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
addEventListener('scroll', kick, { passive: true }); addEventListener('resize', kick); frame();

/* ---------- contact chips ---------- */
$('.chips button').forEach((b) => b.addEventListener('click', (e) => { e.preventDefault(); b.classList.toggle('on'); }));
$('form[data-demo]').forEach((f) => f.addEventListener('submit', (e) => { e.preventDefault(); const b = f.querySelector('.btn'); b.innerHTML = 'Message ready âœ“'; }));


/* ---------- hero slides (photo cross-fade, auto-advance, pills) ---------- */
(() => {
  const root = document.querySelector('.hero2'); if (!root) return;
  const slides = $('.slide', root), pills = $('.slidebtns button', root); let cur = 0, timer = 0;
  const show = (i) => { cur = (i + slides.length) % slides.length; slides.forEach((s, j) => s.classList.toggle('on', j === cur)); pills.forEach((b, j) => b.setAttribute('aria-pressed', String(j === cur))); };
  const play = () => { clearInterval(timer); if (!reduce) timer = setInterval(() => { if (!document.hidden) show(cur + 1); }, 6500); };
  pills.forEach((b, i) => b.addEventListener('click', () => { show(i); play(); }));
  root.addEventListener('mouseenter', () => clearInterval(timer)); root.addEventListener('mouseleave', play);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) play(); });
  play();
})();



/* ---------- intro: play logo video, then fly the logo into the header ---------- */
(() => {
  const intro = document.getElementById('intro'); if (!intro) return;
  const stage = intro.querySelector('.intro-stage'), vid = intro.querySelector('video'), skip = intro.querySelector('.intro-skip');
  const html = document.documentElement; let done = false;
  // logo bounding box inside the video's final frame, as fractions of the frame
  const B = { x: 0.0975, y: 0.2753, w: 0.7987, h: 0.4413 };
  scrollTo(0, 0);
  const finish = () => {
    if (done) return; done = true; clearTimeout(guard);
    intro.remove(); html.classList.remove('intro-on');
    // replay the hero entrance now that it is visible
    const hero = $('.hero2 [data-reveal], .hero2 .mask'); hero.forEach((el) => el.classList.remove('in'));
    requestAnimationFrame(() => setTimeout(() => hero.forEach((el) => el.classList.add('in')), 60));
    kick();
  };
  const fly = () => {
    if (done || intro.classList.contains('fly')) return;
    vid.pause();
    if (document.activeElement === skip) skip.blur();
    intro.setAttribute('inert', '');
    const target = document.querySelector('header.nav .logo'); if (!target) return finish();
    const t = target.getBoundingClientRect(), r = stage.getBoundingClientRect();
    const cs = getComputedStyle(target), padX = parseFloat(cs.paddingLeft) || 0, padY = parseFloat(cs.paddingTop) || 0, rad = parseFloat(cs.borderTopLeftRadius) || 0;
    const W = r.width, H = r.height;
    const s = (t.width - 2 * padX) / (B.w * W);                       // scale so the logo matches the header logo
    const cx = B.x * W + (B.w * W) / 2, cy = B.y * H + (B.h * H) / 2;  // logo centre inside the stage
    const tx = t.left + t.width / 2 - (r.left + cx), ty = t.top + t.height / 2 - (r.top + cy);
    stage.style.transformOrigin = `${cx}px ${cy}px`;
    const L = B.x * W - padX / s, R = W - (B.x + B.w) * W - padX / s, T = B.y * H - padY / s, Bt = H - (B.y + B.h) * H - padY / s;
    stage.style.clipPath = 'inset(0px 0px 0px 0px round 0px)';
    stage.getBoundingClientRect();                                      // commit the start state
    intro.classList.add('fly');
    stage.style.transform = `translate(${tx}px,${ty}px) scale(${s})`;
    stage.style.clipPath = `inset(${T}px ${R}px ${Bt}px ${L}px round ${rad / s}px)`;
    stage.addEventListener('transitionend', (e) => { if (e.propertyName === 'transform') finish(); });
    setTimeout(finish, 1500);
  };
  const guard = setTimeout(fly, 12000);
  vid.addEventListener('ended', () => setTimeout(fly, 350));
  vid.addEventListener('error', finish);
  skip.addEventListener('click', fly);
  const go = vid.play(); if (go) go.catch(finish);
})();
