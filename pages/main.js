// let counter = 1



// setInterval(()=>{

//     document.querySelector('.sliderimg.show').classList.remove('show')
//     const img = document.querySelector(`.img-${counter}`)
//     img.classList.add('show')
//     counter++

//     if(counter >3){
//         counter = 1
//     }

// },3000);

function tope() {
  window.scrollTo(0, 0);
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
    start: "740px",
    // end: "top -11%",
    scrub: 1
  },
});

const btn = document.querySelector(".Nav_btn");
btn.onmousemove = function (e) {
  const x = e.pageX - btn.offsetLeft;
  const y = e.pageY - btn.offsetTop;

  btn.style.setProperty("--x", x + "px");
  btn.style.setProperty("--y", y + "px");
}
let tl2 = gsap.timeline({
  // ease: "slow(0.7,0.7,false)",
  stagger: 0.5,
  opacity:0,
  repeat: -1,

});
tl2.to("#myText-2",{text:"Discover Anime, Manga and Movies all in one place",opacity:1, delay: 5,ease: "slow(0.5, 0.8)",  duration: 6,})
tl2.to("#myText-2",{opacity:0, delay: 10, text:"",ease: "slow(0.5, 0.8)",  duration: 2,})
tl2.to("#myText-2",{text:"Trending, Popular, New releases and upcoming", delay: 0,ease: "slow(0.5, 0.8)",opacity:1,  duration: 6,})
tl2.to("#myText-2",{opacity:0, delay: 10, text:"",ease: "slow(0.5, 0.8)",  duration: 2,})
tl2.to("#myText-2",{text:"No need to vist three websites for all three", delay: 0,ease: "slow(0.5, 0.8)",opacity:1,  duration: 6,})
tl2.to("#myText-2",{opacity:0, delay: 10, text:"",ease: "slow(0.5, 0.8)",  duration: 2,})
tl2.to("#myText-2",{text:"Enjoy your visit", delay: 0,ease: "slow(0.5, 0.8)",opacity:1,  duration: 3,})
tl2.to("#myText-2",{opacity:0, delay: 4, text:"",ease: "slow(0.5, 0.8)",  duration: 2,})

gsap.fromTo(".container",{opacity:0}, {
  opacity: 1,
  duration: 2,
  ease: "linear",
  delay: 4,

})
// function startLoader() {
//    let counterElement = document.querySelector(".counter");
//    let currentValue = 0;

//    function updateCounter(){
//     if(currentValue === 100){
//       return;
//     }

//     currentValue += Math.floor(Math.random() * 10) + 1;

//     if (currentValue > 100){
//       currentValue = 100;
//     }

//     counterElement.textContext = currentValue;
//     let delay = Math.floor(Math.random() * 200) + 50; 
//     setTimeout(updateCounter, delay);
//   }

//   // var divToRemove = document.getElementById('mkc-2');
//   // if (divToRemove) {
//   // divToRemove.parentNode.removeChild(divToRemove); 
//   // }
//   // var TdivToRemove = document.getElementById('mkc');
//   // if (TdivToRemove) {
//   // TdivToRemove.parentNode.removeChild(TdivToRemove); 
//   // }
//   updateCounter();
// }

// startLoader();
// let text = document.querySelector(".text");

gsap.to(".counter", 0.25, {
  delay: 3.4,
  opacity: 0,
  ease: "power4.inOut"
});

gsap.fromTo(".bar",{opacity:1},  {
  delay: 3.7,
  opacity: 0 ,
  duration: 4,
  ease: "power1.out",

});
// gsap.to(".bar", 1.5, {
//   delay: 3.5,
//   height: 0,
//   stagger: {
//     amount: 0.5,
//   },
//   ease: "power4.inOut"

// });
setTimeout(() => {
  var a = document.getElementById("mkc");
  a.style.zIndex = -100;
  var a = document.getElementById("mkc-2");
  a.style.zIndex = -100;
  clearTimeout(setTimeout);
}, 4000);

// let tl = gsap.timeline({
//   defaults: {
//     opacity: 0,
//     ease: "slow(0.7,0.7,false)",
//   }
// })

// tl.set(".card",{
//   opacity: 0,

// })
// tl.set(".Type",{
//   opacity: 0,

// })
// tl.to(".Type",{
//   opacity:1,
//   ease: "linear",
//   stagger: {
//     amount: 8,
//     each: 4,
//   },
//   scrollTrigger: {
//     trigger: ".all-card-pop",
//     start: "-100px",
//     end: "-20px",
//     scrub: 1,
//     markers: true,
//   }
// })
// for popular section
// tl.fromTo(".type-1", { opacity: 0 }, {
//   opacity: 1,
//   ease: "slow(0.7,0.7,false)",
//   stagger: 1,
//   scrollTrigger: {
//     trigger: ".all-card",
//     start: "-295px",
//     // end: "-20px",
//     scrub: 1,
//     // markers: true,
//   }
// })
// tl.fromTo(".popu", { opacity: 0 }, {
//   opacity: 1,
//   duration: 3,
//   delay: 1,
//   ease: "slow(0.7,0.7,false)",
//   paused: true,
//   stagger: 1,
//   scrollTrigger: {
//     trigger: ".all-card-pop",
//     start: "-280px",
//     end: "70px",
//     scrub: 1,
//     // markers: true,
//   }
// })
// // for latest section
// tl.fromTo(".type-2", { opacity: 0 }, {
//   opacity: 1,
//   ease: "slow(0.7,0.7,false)",
//   stagger: 1,
//   scrollTrigger: {
//     trigger: ".all-card-lat",
//     start: "1000px",
//     // end: "-20px",
//     scrub: 1,
//     // markers: true,
//   }
// })
// tl.fromTo(".popi", { opacity: 0 }, {
//   opacity: 1,
//   duration: 3,
//   delay: 1,
//   ease: "slow(0.7,0.7,false)",
//   paused: true,
//   stagger: 1,
//   scrollTrigger: {
//     trigger: ".all-card-lat",
//     start: "1010px",
//     end: "1300px",
//     scrub: 1,
//     // markers: true,
//   }
// })
// // for ran section
// tl.fromTo(".type-3", { opacity: 0 }, {
//   opacity: 1,
//   ease: "slow(0.7,0.7,false)",
//   stagger: 1,
//   scrollTrigger: {
//     trigger: ".all-card-ran",
//     start: "2400px",
//     // end: "2450px",
//     scrub: 1,
//     markers: true,
//   }
// })
// tl.fromTo(".popo", { opacity: 0 }, {
//   opacity: 1,
//   duration: 3,
//   delay: 1,
//   ease: "slow(0.7,0.7,false)",
//   paused: true,
//   stagger: 1,
//   scrollTrigger: {
//     trigger: ".all-card-ran",
//     start: "2410px",
//     end: "2600px",
//     scrub: 1,
//     // markers: true,
//   }
// })
//horizontal scrolling
let sections = gsap.utils.toArray(".popu");

gsap.to(sections, {

  xPercent: -150 * (sections.length - 7),
  // ease: "linear",
  ease: "power2.out",
  scrollTrigger: {
    trigger: ".all-card-pop",
    pin: true,
    start: "50px",
    // end:"70px",
    markers: true,
    scrub: 1,
    snap: 2 / (sections.length - 2),
    end: () => 
      document.querySelector(".all-card-pop").offsetWidth

  }
});


let sectionsL = gsap.utils.toArray(".popi");

gsap.to(sectionsL, {

  xPercent: -150 * (sectionsL.length - 7),
  ease: "slow(0.7,0.7,false)",
  scrollTrigger: {
    trigger: ".all-card-lat",
    pin: true,
    start: "50px",
    // end:"100px",
    // markers: true,
    scrub: 1,
    snap: 2 / (sectionsL.length - 2),
    end: () => 
      document.querySelector(".all-card-lat").offsetWidth

  }
});
let sectionsR = gsap.utils.toArray(".popo");

gsap.to(sectionsR, {

  xPercent: -150 * (sectionsR.length - 7),
  ease: "slow(0.7,0.7,false)",
  scrollTrigger: {
    trigger: ".all-card-ran",
    pin: true,

    start: "50px",
    // end:"100px",
    // markers: true,
    scrub: 1,
    snap: 2 / (sectionsR.length - 2),
    end: () => 
      document.querySelector(".all-card-ran").offsetWidth

  }
});
// gsap.fromTo(".ani-vid",{scale: 0}, {
// scale: 1,
//   duration: 2,
//   // ease: "sine.out",
//   delay: 5,

// })
gsap.fromTo(".man-vid", { opacity: 0 }, {
  duration: 2,
  ease: "sine.out",
  opacity: 1,
  rotation: 360,
  delay: 5,

})
// gsap.from(".header", {
//   y: "-100%",
//   duration: 2,
//   delay: 4,
//   ease: "linear",
//   scrub: 1

// })
gsap.fromTo(".nav-elem", { opacity: 0 }, {
  opacity: 1,
  duration: 4,
  delay: 4.5,
  stagger: 0.1,
  scrub: 1

})




