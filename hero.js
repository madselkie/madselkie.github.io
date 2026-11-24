(function(){
  var v = document.getElementById('hero');
  if (!v) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  function stop(){ try { v.pause(); v.removeAttribute('autoplay'); } catch(e){} }
  if (reduce.matches) { stop(); }
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function(es){
      es.forEach(function(e){
        if (reduce.matches) return;
        if (e.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function(){}); }
        else { v.pause(); }
      });
    }, { threshold: 0.15 }).observe(v);
  }
  reduce.addEventListener && reduce.addEventListener('change', function(e){ if (e.matches) stop(); });
})();