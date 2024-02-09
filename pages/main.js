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

function tope(){
  window.scrollTo(0,0);
}

const btn = document.querySelector(".Nav_btn");
btn.onmousemove = function(e){
  const x = e.pageX - btn.offsetLeft;
  const y = e.pageY - btn.offsetTop;

  btn.style.setProperty("--x",x + "px");
  btn.style.setProperty("--y",y + "px");
}


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

let sections = gsap.utils.toArray(".popu");

gsap.to(sections,{

    xPercent: -100 * (sections.length-4.5),
    ease: "none",
    scrollTrigger: {
        trigger: ".all-card-pop",
        pin: true,
        start: "50px",
        // end:"100px",
        // markers: true,
        scrub: 1,
        snap: 1 / (sections.length-1),
        end: () => "+=" + 
        document.querySelector(".all-card-pop").offsetWidth

    }
});


let sectionsL = gsap.utils.toArray(".popi");

gsap.to(sectionsL,{

    xPercent: -100 * (sectionsL.length-4.5),
    ease: "slow(0.7,0.7,false)",
    scrollTrigger: {
        trigger: ".all-card-lat",
        pin: true,
        start: "50px",
        // end:"100px",
        // markers: true,
        scrub: 1,
        snap: 1 / (sectionsL.length-1),
        end: () => "+=" + 
        document.querySelector(".all-card-lat").offsetWidth

    }
});
let sectionsR = gsap.utils.toArray(".popo");

gsap.to(sectionsR,{

    xPercent: -100 * (sectionsR.length-4.5),
    ease: "slow(0.7,0.7,false)",
    scrollTrigger: {
        trigger: ".all-card-ran",
        pin: true,
        start: "50px",
        // end:"100px",
        // markers: true,
        scrub: 1,
        snap: 1 / (sectionsR.length-1),
        end: () => "+=" + 
        document.querySelector(".all-card-ran").offsetWidth

    }
});
setTimeout(() => {
  var a = document.getElementById("mkc");
  a.style.zIndex=-100; 
  var a = document.getElementById("mkc-2");
  a.style.zIndex=-100;
  clearTimeout(setTimeout);
}, 4000);
