(function(){
  /* 모바일 메뉴 */
  var b=document.getElementById('burger'), d=document.getElementById('drawer');
  if(b&&d){
    b.addEventListener('click',function(){
      var open=d.classList.toggle('open');
      b.setAttribute('aria-expanded',open?'true':'false');
      b.setAttribute('aria-label',open?'메뉴 닫기':'메뉴 열기');
    });
  }

  /* 헤더 스크롤 그림자 */
  var hd=document.querySelector('.hd');
  if(hd){
    var onScroll=function(){ hd.classList.toggle('is-scrolled', window.scrollY>6); };
    onScroll();
    window.addEventListener('scroll',onScroll,{passive:true});
  }

  /* 스크롤 리빌 — 마크업 수정 없이 JS로 대상 지정 */
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!reduce && 'IntersectionObserver' in window){
    var SEL='.sec__head, .entry, .grid>div, .quick a, .links a, .place, .acc, .tl li, .steps li,'
          + '.news a, .desig li, .free, .stats div, .callout, .badges div, .gate, .btnrow, .prose, .dl, .bul, .tblwrap';
    var els=[].slice.call(document.querySelectorAll(SEL));
    // 첫 화면(히어로/KV) 안쪽 요소는 즉시 노출
    els=els.filter(function(el){ return !el.closest('.kv, .hero, details'); });
    els.forEach(function(el){ el.setAttribute('data-rv',''); });
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(!e.isIntersecting) return;
        var el=e.target;
        // 형제 순서에 따라 살짝 지연 (최대 180ms)
        var sibs=el.parentElement?[].slice.call(el.parentElement.children).indexOf(el):0;
        el.style.transitionDelay=Math.min(sibs,3)*60+'ms';
        el.classList.add('in');
        io.unobserve(el);
      });
    },{rootMargin:'0px 0px -8% 0px',threshold:0.08});
    els.forEach(function(el){ io.observe(el); });
    // 실패 대비 — 2.2초 뒤 남은 요소는 모두 노출
    setTimeout(function(){
      document.querySelectorAll('[data-rv]:not(.in)').forEach(function(el){ el.classList.add('in'); });
    },2200);
    // 아코디언 열릴 때 안쪽 요소가 숨어있지 않도록
    document.querySelectorAll('details').forEach(function(d){
      d.addEventListener('toggle',function(){
        d.querySelectorAll('[data-rv]:not(.in)').forEach(function(el){ el.classList.add('in'); });
      });
    });
  }
})();
