const btn = document.querySelector(".Nav_btn");
btn.onmousemove = function(e){
  const x = e.pageX - btn.offsetLeft;
  const y = e.pageY - btn.offsetTop;

  btn.style.setProperty("--x",x + "px");
  btn.style.setProperty("--y",y + "px");
}
gsap.to(".counter",0.25,{
    delay: 2.5,
    opacity: 0,
  });
  gsap.to(".bar",1.5,{
    delay: 2,
    height: 0,
    stagger: {
      amount: 0.5,
    },
    ease: "power4.inOut",
  
  });
setTimeout(() => {
    var a = document.getElementById("mkc");
    a.style.zIndex=-10000; 
    a.scrollTop = 0;
    var a = document.getElementById("mkc-2");
    a.style.zIndex=-10000;
    clearTimeout(setTimeout);
  },4000);
  
  function tope(){
    window.scrollTo(0,0);
  }