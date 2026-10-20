/* 한국화학안전협회 메인 — 모션그래픽 (첫 화면 필름 + 업무 스크롤 스토리) */
(function(){
  'use strict';
  var mq = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : null;
  var REDUCE = !!(mq && mq.matches);
  var root = document.documentElement;

  /* 헤더 높이 → sticky 기준선 */
  var hd = document.querySelector('.hd');
  function setHd(){ if(hd) root.style.setProperty('--hd-h', hd.offsetHeight + 'px'); }
  setHd(); window.addEventListener('resize', setHd);

  /* 카메라: [translateX, translateY, scale] (SVG 좌표) */
  var CAM = {"wide":[-6.3,-9.5,1],"risk":[68.6,-111.8,1.28],"psm":[-184.4,-53.1,1.32],"scan":[-16.9,-11.7,1.02],
    "merge":[-130.4,-15.8,1.12],"permit":[-126.5,-50,1.22],"build":[-75.7,55.2,1.3],"edu":[-112.6,-123.4,1.18],
    "eduai":[-47.2,-59.7,1.08],"ai":[-29.3,-5.3,1.06],"shield":[14.2,39.6,0.92]};
  /* 첫 화면 필름용 — 자막 영역만큼 위로 올린 구도 */
  var FCAM = {"wide":[24.3,-15.6,0.9],"risk":[74.1,-137.8,1.25],"scan":[8,-22.8,0.94],"permit":[-91.6,-43,1.12],
    "eduai":[-16.9,-96.7,1.02],"edu":[-102.1,-159.9,1.15],"ai":[-4.4,-8.7,0.98],"shield":[32.8,36,0.86]};
  function cam(svg, key, set){
    var g = svg && svg.querySelector('.cam'); var M = set || CAM; var c = M[key] || M.wide;
    if(g) g.style.transform = 'translate(' + c[0] + 'px,' + c[1] + 'px) scale(' + c[2] + ')';
  }

  function onVisible(el, cb){
    if(!('IntersectionObserver' in window)){ cb(true); return; }
    new IntersectionObserver(function(es){ es.forEach(function(e){ cb(e.isIntersecting); }); }, {threshold:0.05}).observe(el);
  }

  /* ---------------- 1. 분자망 배경 (첫 화면 · AI 섹션) ---------------- */
  function net(cv, line, dot){
    if(!cv || !cv.getContext) return;
    var ctx = cv.getContext('2d'), pts = [], W = 0, H = 0, on = true, raf = 0;
    var draw = function(){
      ctx.clearRect(0,0,W,H);
      var D = Math.min(150, W/6.5), D2 = D*D;
      for(var i=0;i<pts.length;i++){
        var a = pts[i];
        for(var j=i+1;j<pts.length;j++){
          var b = pts[j], dx = a.x-b.x, dy = a.y-b.y, d2 = dx*dx+dy*dy;
          if(d2 < D2){ ctx.strokeStyle = 'rgba(' + line + ',' + (0.16*(1-d2/D2)).toFixed(3) + ')'; ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke(); }
        }
      }
      ctx.fillStyle = dot;
      for(var k=0;k<pts.length;k++){ var p = pts[k]; ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,6.283); ctx.fill(); }
    };
    var resize = function(){
      var r = cv.getBoundingClientRect(), dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr,0,0,dpr,0,0);
      var n = Math.round(Math.min(64, Math.max(26, W * H / 16000)));
      pts = []; for(var i=0;i<n;i++) pts.push({x:Math.random()*W, y:Math.random()*H, vx:(Math.random()-.5)*.22, vy:(Math.random()-.5)*.22, r:Math.random()*1.6+.8});
      draw();
    };
    var tick = function(){
      for(var i=0;i<pts.length;i++){ var p = pts[i]; p.x += p.vx; p.y += p.vy;
        if(p.x<-20) p.x = W+20; if(p.x>W+20) p.x = -20; if(p.y<-20) p.y = H+20; if(p.y>H+20) p.y = -20; }
      draw(); raf = requestAnimationFrame(tick);
    };
    resize();
    var rt; window.addEventListener('resize', function(){ clearTimeout(rt); rt = setTimeout(resize, 150); });
    if(!REDUCE){
      onVisible(cv, function(v){ on = v; cancelAnimationFrame(raf); if(v && !document.hidden) raf = requestAnimationFrame(tick); });
      document.addEventListener('visibilitychange', function(){ cancelAnimationFrame(raf); if(!document.hidden && on) raf = requestAnimationFrame(tick); });
    }
  }
  net(document.querySelector('.mkv__net'), '143,224,242', 'rgba(166,232,247,.55)');
  net(document.querySelector('.aix__net'), '133,232,186', 'rgba(133,232,186,.5)');

  /* ---------------- 2. 첫 화면 모션 필름 ---------------- */
  var film = document.getElementById('film');
  if(film){
    var fsvg = film.querySelector('.world');
    var SC = [
      {s:'intro',      c:'wide',   tag:'사업장',      t:'화학물질을 취급하는 사업장',           d:'제조 · 사용 · 판매 · 운반',                 ms:5600, draw:true},
      {s:'risk',       c:'risk',   tag:'위험',        t:'사고는 사업장 밖까지 번질 수 있습니다', d:'그래서 미리 계획하고 대비해야 합니다',       ms:4600},
      {s:'scan',       c:'scan',   tag:'진단',        t:'잠재된 유해·위험 요인을 진단합니다',    d:'법정 진단장비 19종 보유',                     ms:4600},
      {s:'permit psm', c:'permit', tag:'계획·인허가', t:'법정 서류와 인허가를 지원합니다',       d:'예방관리계획서 · PSM · 통합환경 허가',        ms:4600},
      {s:'edu',        c:'edu',    tag:'교육',        t:'현장의 사람을 교육합니다',              d:'유해화학물질 안전교육 · 산업안전보건 교육',   ms:4600},
      {s:'ai',         c:'ai',     tag:'AI 전환',     t:'규제 대응 업무의 AI 전환을 지원합니다',  d:'AI특화 공동훈련센터 · 협약 기업 전액 무료',   ms:5000},
      {s:'shield',     c:'shield', tag:'함께',        t:'한국화학안전협회가 함께 하겠습니다',    d:'환경부 · 노동부 지정 전문기관',               ms:6000}
    ];
    var no = film.querySelector('.film__no'), tag = film.querySelector('.film__tag');
    var ft = film.querySelector('.film__t'), fd = film.querySelector('.film__d');
    var bars = [].slice.call(film.querySelectorAll('.film__ch i'));
    var btns = [].slice.call(film.querySelectorAll('.film__ch button'));
    var pp = film.querySelector('.film__pp');
    var idx = 0, el = 0, last = null, userPaused = false, inView = true;

    var words = function(node, text){
      node.innerHTML = '';
      text.split(' ').forEach(function(w, i){
        if(i) node.appendChild(document.createTextNode(' '));
        var o = document.createElement('span'); o.className = 'w';
        var n = document.createElement('span'); n.textContent = w; n.style.animationDelay = (i*55) + 'ms';
        o.appendChild(n); node.appendChild(o);
      });
    };
    var apply = function(){
      var s = SC[idx];
      film.setAttribute('data-scene', idx);
      fsvg.setAttribute('data-s', s.s);
      cam(fsvg, s.c, FCAM);
      no.textContent = ('0' + (idx+1)).slice(-2); tag.textContent = s.tag;
      words(ft, s.t); fd.textContent = s.d;
      fd.classList.remove('in'); void fd.offsetWidth; fd.classList.add('in');
      btns.forEach(function(b, j){ b.setAttribute('aria-current', j === idx ? 'step' : 'false'); });
      if(s.draw && !REDUCE){ fsvg.classList.remove('is-drawing'); void fsvg.getBoundingClientRect(); fsvg.classList.add('is-drawing'); }
    };
    var go = function(i){ idx = (i + SC.length) % SC.length; el = 0; apply(); paint(); };
    var paint = function(){
      for(var j=0;j<bars.length;j++){
        var v = j < idx ? 1 : (j > idx ? 0 : (REDUCE ? 1 : Math.min(1, el / SC[idx].ms)));
        bars[j].style.transform = 'scaleX(' + v + ')';
      }
    };
    var running = function(){ return !REDUCE && !userPaused && inView && !document.hidden; };
    var loop = function(ts){
      if(last === null) last = ts;
      var dt = Math.min(100, ts - last); last = ts;
      if(running()){ el += dt; if(el >= SC[idx].ms) go(idx + 1); paint(); }
      requestAnimationFrame(loop);
    };
    var idle = function(){ film.classList.toggle('is-idle', !running()); };

    btns.forEach(function(b, j){ b.addEventListener('click', function(){ go(j); }); });
    if(pp){
      pp.addEventListener('click', function(){
        userPaused = !userPaused;
        pp.setAttribute('aria-pressed', userPaused ? 'true' : 'false');
        pp.setAttribute('aria-label', userPaused ? '모션 재생' : '모션 일시정지');
        film.classList.toggle('is-paused', userPaused); idle();
      });
    }
    onVisible(film, function(v){ inView = v; idle(); });
    document.addEventListener('visibilitychange', idle);

    if(REDUCE){ idx = SC.length - 1; apply(); paint(); if(pp) pp.hidden = true; }
    else { apply(); paint(); requestAnimationFrame(loop); }
  }

  /* ---------------- 3. 업무 스크롤 스토리 ---------------- */
  var stage = document.getElementById('stage');
  var steps = [].slice.call(document.querySelectorAll('.story__steps > .step'));
  if(stage && steps.length){
    var ssvg = stage.querySelector('.world');
    var sno = stage.querySelector('.stage__no b'), slaw = stage.querySelector('.stage__law');
    var dots = [].slice.call(stage.querySelectorAll('.stage__dots button'));
    var wrapSt = stage.parentElement;
    var dq = window.matchMedia('(min-width: 960px)');
    var cur = -1, ticking = false, total = steps.length - 1;
    var CAMS = {risk:'risk', psm:'psm', scan:'scan', merge:'merge', permit:'permit', build:'build', edu:'edu', ai:'ai', shield:'shield'};

    var set = function(i){
      if(i === cur) return; cur = i;
      var st = steps[i], s = st.getAttribute('data-s');
      ssvg.setAttribute('data-s', s); cam(ssvg, CAMS[s] || 'wide');
      stage.setAttribute('data-step', i);
      sno.textContent = i < total ? ('0' + (i+1)).slice(-2) : '—';
      slaw.textContent = st.getAttribute('data-law');
      slaw.classList.remove('in'); void slaw.offsetWidth; slaw.classList.add('in');
      steps.forEach(function(x, j){ x.classList.toggle('is-on', j === i); });
      dots.forEach(function(d, j){ d.setAttribute('aria-current', j === i ? 'step' : 'false'); });
    };
    var line = function(){
      var vh = window.innerHeight;
      if(dq.matches) return vh * 0.52;
      var b = (hd ? hd.offsetHeight : 58) + wrapSt.offsetHeight;   /* 고정됐을 때의 무대 하단 */
      return b + (vh - b) * 0.34;
    };
    var pick = function(){
      ticking = false;
      var L = line(), k = 0;
      for(var i=0;i<steps.length;i++){ if(steps[i].getBoundingClientRect().top < L) k = i; }
      set(k);
    };
    window.addEventListener('scroll', function(){ if(!ticking){ ticking = true; requestAnimationFrame(pick); } }, {passive:true});
    window.addEventListener('resize', pick);
    dots.forEach(function(d, j){
      d.addEventListener('click', function(){
        var r = steps[j].getBoundingClientRect();
        var y = dq.matches ? window.scrollY + r.top - line() + Math.min(r.height/2, 160)
                           : window.scrollY + r.top - ((hd ? hd.offsetHeight : 58) + wrapSt.offsetHeight) + 2;
        window.scrollTo({top: y, behavior: REDUCE ? 'auto' : 'smooth'});
      });
    });
    var setSh = function(){ root.style.setProperty('--stage-h', (dq.matches ? 0 : wrapSt.offsetHeight) + 'px'); };
    setSh(); window.addEventListener('resize', setSh);
    onVisible(stage, function(v){ stage.classList.toggle('is-idle', !v); });
    pick();
  }

  /* ---------------- 4. AI 교육센터 — 4단계 순환 ---------------- */
  var flow = document.getElementById('axflow');
  var aix = document.getElementById('aix');
  if(flow && aix){
    var st = [].slice.call(flow.querySelectorAll('.axs'));
    var rail = flow.querySelector('.axflow__rail i');
    var ai = 0, aT = 0, aOn = false;
    var setA = function(i){
      ai = i;
      st.forEach(function(x, j){ x.classList.toggle('is-on', j === i); x.classList.toggle('is-done', j < i);
        x.querySelector('.axs__btn').setAttribute('aria-pressed', j === i ? 'true' : 'false'); });
      if(rail) rail.style.transform = 'scaleX(' + ((i + 0.5) / st.length) + ')';
    };
    var next = function(){ setA((ai + 1) % st.length); };
    var run = function(){ clearInterval(aT); if(!REDUCE && aOn && !document.hidden) aT = setInterval(next, 2800); };
    st.forEach(function(x, j){
      x.querySelector('.axs__btn').addEventListener('click', function(){ setA(j); run(); });
      x.addEventListener('mouseenter', function(){ if(window.matchMedia('(hover:hover)').matches){ setA(j); run(); } });
    });
    setA(0);
    onVisible(aix, function(v){
      aOn = v; if(v) aix.classList.add('is-in');
      aix.classList.toggle('is-idle', !v); run();
    });
    document.addEventListener('visibilitychange', run);
  }
})();
