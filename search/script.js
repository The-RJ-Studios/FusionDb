// let mkc7= document.getElementById('Search').innerText
// console.log(mkc7)
function showSidebar(){
  const sidebar = document.querySelector('.sidebar');
  sidebar.style.display = 'flex'
}
function hideSidebar(){
  const sidebar = document.querySelector('.sidebar');
  sidebar.style.display = 'none'
}
function tope(){
    window.scrollTo(0,0);
  }
  let mm = gsap.matchMedia();
  mm.add("(min-width: 801)",()=>{
    gsap.to(".counter", 0.25, {
      delay: 1.5,
      duration: 2,
      opacity: 0,
      ease: "power4.inOut"
    });
    
    gsap.fromTo(".bar",{opacity:1},  {
      delay: 2,
      opacity: 0 ,
      duration: 2,
      ease: "power1.out",
    
    });
  
  })
  let mobile = gsap.matchMedia();
  mobile.add("(max-width: 800px)",()=>{
  
  gsap.to("#nav", {
    backgroundColor: "#0e100f",
    duration: 1.5,
    height: "80px",
    marginTop: 0,
    borderBottom: "1.5px solid #42433d",
    scrollTrigger: {
      trigger: "#nav",
      scroller: "body",
      // markers:true,
      start: "300px",
      // end: "top -11%",
      scrub: 1
    },
  });
  gsap.fromTo(".nav-elem", { opacity: 0 }, {
    opacity: 1,
    duration: 3,
    delay: 0,
    stagger: 0.1,
    scrub: 1
  
  })
  
  });
  setTimeout(() => {
    var a = document.getElementById("mkc");
    a.style.display = "none";
    var a = document.getElementById("mkc-2");
    a.style.display = "none";
    clearTimeout(setTimeout);
  }, 4000);
