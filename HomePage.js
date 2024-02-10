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


const btn = document.querySelector(".Nav_btn");
btn.onmousemove = function(e){
  const x = e.pageX - btn.offsetLeft;
  const y = e.pageY - btn.offsetTop;

  btn.style.setProperty("--x",x + "px");
  btn.style.setProperty("--y",y + "px");
}


gsap.to("#nav", {
    backgroundColor: "transparent",
    duration: 0.5,
    height: "80px",
    scrollTrigger: {
      trigger: "#nav",
      scroller: "body",
      // markers:true,
      start: "top -10%",
      end: "top -11%",
      scrub: 1,
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
  delay: 4,
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
gsap.from("#vid",2.5,{
  delay: 1.5, 
  x: 700,
  stagger: {
    amount: 0.5,
  },
  ease : "power4.inOut",
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
}, 4000);

function tope(){
  window.scrollTo(0,0);
}
setTimeout(function () {
  window.scrollTo(0, 0);
},2);

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