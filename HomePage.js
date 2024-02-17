// let counter = 1

// const { default: gsap } = require("gsap");



// setInterval(()=>{

//     document.querySelector('.sliderimg.show').classList.remove('show')
//     const img = document.querySelector(`.img-${counter}`)
//     img.classList.add('show')
//     counter++

//     if(counter >3){
//         counter = 1
//     }

// },3000);
// gsap.to("#myText", {duration: 2, text: "thank you for waiting",preserveSpaces: true, delay: 7.5});

const btn = document.querySelector(".Nav_btn");
btn.onmousemove = function(e){
  const x = e.pageX - btn.offsetLeft;
  const y = e.pageY - btn.offsetTop;

  btn.style.setProperty("--x",x + "px");
  btn.style.setProperty("--y",y + "px");
}
gsap.from(".container", {
    x: "-100%",
    duration: 2,
    ease: "sine.out",
    delay: 5,

})
gsap.from(".header", {
    y: "-100%",
    duration: 2,
    delay: 6,
    ease: "bounce",
    scrub: 1

})
gsap.fromTo(".scrolling-down",{opacity:0,y: 120},{
  opacity:1,
  y: 0,
  duration: 1,
  ease: "linear",
  delay: 6.5,
  
})
// gsap.fromTo(".scrolling-down-symbol",{opacity:0,y: 100},{
//   opacity:1,
//   y: 0,
//   duration: 2,
//   ease: "linear",
//   delay: 7,
// })



gsap.to("#nav", {
    backgroundColor: "#0e100f",
    duration: 1.5,
    height: "80px",
    marginTop: 0,
    // boxShadow: "0px 4px 0px 0px blue",
    borderBottom: "10px solid #42433d",
    scrollTrigger: {
      trigger: "#nav",
      scroller: "body",
      // markers:true,
      start: "740px",
      // end: "top -11%",
      scrub: 1
    },
  });

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

gsap.to(".counter",{
  duration: 0.25,
  delay: 3.5,
  opacity: 0,
});
gsap.to(".bar",1.5,{
  delay: 3.5,
  height: 0,
  stagger: {
    amount: 0.5,
  },
  ease: "power4.inOut",

});
// let lastKnownScrollPosition = 0;
// function gand(){

//   document.addEventListener("scroll", (event) => {
    
//     lastKnownScrollPosition = window.scrollY;
//     // console.log(lastKnownScrollPosition);
    
//     if(lastKnownScrollPosition>=100){
//       window.scrollTo(0, 0);
//     }
//   }
//   )
// }
// document.removeEventListener("scroll",gand);





// setTimeout(()=>{
//   document.addEventListener("scroll", (event) => {

//     lastKnownScrollPosition = window.scrollY;
//     // console.log(lastKnownScrollPosition);

//     if(lastKnownScrollPosition>=100){
//       window.scrollTo(0, 0);
//     }
//   }
//   )
  
// },0)

setTimeout(() => {
  var a = document.getElementById("mkc");
  a.style.zIndex=-100; 
  var a = document.getElementById("mkc-2");
  a.style.zIndex=-100;
  clearTimeout(setTimeout);
}, 5000);

function tope(){
  window.scrollTo(0,0);
}
// start page timeline
// let tl2 = gsap.timeline({
//   // ease: "slow(0.7,0.7,false)",
//   stagger: 0.01,
//   duration: 6,
//   repeat: 2,

// });
// tl2.to("#myText-2",{text:"Discover Anime, Manga and Movies all in one place", delay: 7,ease: "slow(0.5, 0.8)",})
// tl2.to("#myText-2",{text:"Trending, Popular, New releases and upcoming", delay: 7,ease: "slow(0.5, 0.8)",})
// tl2.to("#myText-2",{text:"No need to vist three websites for all three", delay: 7,ease: "slow(0.5, 0.8)",})
// tl2.to("#myText-2",{text:"Enjoy your visit", delay: 7,ease: "slow(0.5, 0.8)",})

let tl2 = gsap.timeline({
  // ease: "slow(0.7,0.7,false)",
  stagger: 0.5,
  opacity:0,
  repeat: -1,

});
tl2.to("#myText-2",{text:"Discover Anime, Manga and Movies all in one place",opacity:1, delay: 7,ease: "slow(0.5, 0.8)",  duration: 6,})
tl2.to("#myText-2",{opacity:0, delay: 10, text:"",ease: "slow(0.5, 0.8)",  duration: 2,})
tl2.to("#myText-2",{text:"Trending, Popular, New releases and upcoming", delay: 0,ease: "slow(0.5, 0.8)",opacity:1,  duration: 6,})
tl2.to("#myText-2",{opacity:0, delay: 10, text:"",ease: "slow(0.5, 0.8)",  duration: 2,})
tl2.to("#myText-2",{text:"No need to vist three websites for all three", delay: 0,ease: "slow(0.5, 0.8)",opacity:1,  duration: 6,})
tl2.to("#myText-2",{opacity:0, delay: 10, text:"",ease: "slow(0.5, 0.8)",  duration: 2,})
tl2.to("#myText-2",{text:"Enjoy your visit", delay: 0,ease: "slow(0.5, 0.8)",opacity:1,  duration: 3,})
tl2.to("#myText-2",{opacity:0, delay: 4, text:"",ease: "slow(0.5, 0.8)",  duration: 2,})


// about us timeline
// TweenLite.defaultEase = Linear.easeNone;
let tl= gsap.timeline({scrollTrigger: {
  trigger: ".ani-words",
  start: "-600px",
  end: "-270px",
  scrub: 1,
  delay: 4,
  stagger: 0.01,
  // markers: true,
  ease: "slow(0.7,0.7,false)",
},});

tl.to("#mkc-3",4, {text:"LATEST & POPULAR"})
tl.to(".p1",4, {text:" M2ADB is a webite made in a way that"})
tl.fromTo(".ab-img", {opacity:0,scale:0},{ opacity: 1 , scale: 1 , duration: 5 , })
tl.to(".p2", 4, {text:"people can discover Popular, Upcoming & Latest"})
tl.to(".p3", 4, {text:"Anime, Manga and Movies"})
tl.to(".p4", 4, {text:"all three in"})
tl.to(".p5", 4, {text:"one single place, and does not have the need to visit another "})
tl.to(".p6", 4, {text:"website for each."})
// setTimeout(function () {
//   window.scrollTo(0, 0);
// },2);

// document.getElementById("page1").style.zIndex = 100000;

// snap all of the properties in the comma-delimited list ("x,y" in this case) to the closest whole number:
// gsap.to(".elem", {
//   x: 100,
//   y: 250,
//   snap: "x,y",
// });

// // snap to an increment:
// gsap.to(".elem-2", {
//   x: 1000,
//   snap: {
//     x: 20, // x snaps to the closest increment of 20 (0, 20, 40, 60, etc.)
//   },
// });

// // snap to the closest value in an array:
// gsap.to(".elem-3", {
//   x: 1000,
//   snap: {
//     x: [0, 50, 150, 500], // x snaps to the closest value in this array
//   },
// });