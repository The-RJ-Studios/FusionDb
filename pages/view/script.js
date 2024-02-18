const btn = document.querySelector(".Nav_btn");
btn.onmousemove = function(e){
  const x = e.pageX - btn.offsetLeft;
  const y = e.pageY - btn.offsetTop;

  btn.style.setProperty("--x",x + "px");
  btn.style.setProperty("--y",y + "px");
}

gsap.to(".counter",0.25,{
    delay: 3,
    opacity: 0,
  });
  gsap.to(".bar",1.5,{
    delay: 3,
    height: 0,
    stagger: {
      amount: 0.5,
    },
    ease: "power4.inOut",
  
  });
setTimeout(() => {
    var a = document.getElementById("mkc");
    a.style.zIndex=-100; 
    a.scrollTop = 0;
    var a = document.getElementById("mkc-2");
    a.style.zIndex=-100;
    clearTimeout(setTimeout);
  },4000);
  
  function tope(){
    window.scrollTo(0,0);
  }
  gsap.to("#nav", {
    backgroundColor: "#0e100f",
    duration: 1.5,
    height: "80px",
    marginTop: 0,
    // boxShadow: "0px 4px 0px 0px blue",
    borderBottom: "1.5px solid #42433d",
    scrollTrigger: {
      trigger: "#nav",
      scroller: "body",
      // markers:true,
      start: "60px",
      // end: "top -11%",
      scrub: 1
    },
  });