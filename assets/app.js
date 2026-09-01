(function(){
  var b=document.getElementById('burger'), d=document.getElementById('drawer');
  if(b&&d){
    b.addEventListener('click',function(){
      var open=d.classList.toggle('open');
      b.setAttribute('aria-expanded',open?'true':'false');
      b.setAttribute('aria-label',open?'메뉴 닫기':'메뉴 열기');
    });
  }
})();
