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
  delay: 3.5,
  opacity: 0,
  ease: "power4.inOut"
});
gsap.to(".bar",1.5,{
  delay: 3.5,
  height: 0,
  stagger: {
    amount: 0.5,
  },
  ease: "power4.inOut"

});
setTimeout(() => {
  var a = document.getElementById("mkc");
  a.style.zIndex=-100; 
  var a = document.getElementById("mkc-2");
  a.style.zIndex=-100;
  clearTimeout(setTimeout);
}, 5000);

let sections = gsap.utils.toArray(".popu");
gsap.set(".card",{
  opacity: 0,
  
})
gsap.set(".Type",{
  opacity: 0,
  
})
gsap.to(".Type",{
  opacity:1,
  ease: "linear",
  stagger: {
    amount: 8,
    each: 4,
  },
  scrollTrigger: {
    trigger: ".all-card-pop",
    start: "-100px",
    end: "-20px",
    scrub: 1,
    markers: true,
  }
})


gsap.to(".card",{
  opacity:1,
  ease: "linear",
  stagger: {
    amount: 8,
    each: 4,
  },
  scrollTrigger: {
    trigger: ".all-card-pop",
    start: "-50px",
    end: "100px",
    scrub: 1,
    markers: true,
  }
})
gsap.to(sections,{

    xPercent: -100 * (sections.length-6),
    ease: "none",
    scrollTrigger: {
        trigger: ".all-card-pop",
        pin: true,
        start: "50px",
        // end:"100px",
        markers: true,
        scrub: 1,
        snap: 1 / (sections.length-1),
        end: () => "+=" + 
        document.querySelector(".all-card-pop").offsetWidth

    }
});


let sectionsL = gsap.utils.toArray(".popi");

gsap.to(sectionsL,{

    xPercent: -100 * (sectionsL.length-6),
    ease: "slow(0.7,0.7,false)",
    scrollTrigger: {
        trigger: ".all-card-lat",
        pin: true,
        start: "50px",
        // end:"100px",
        markers: true,
        scrub: 1,
        snap: 1 / (sectionsL.length-1),
        end: () => "+=" + 
        document.querySelector(".all-card-lat").offsetWidth

    }
});
let sectionsR = gsap.utils.toArray(".popo");

gsap.to(sectionsR,{

    xPercent: -100 * (sectionsR.length-6),
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
gsap.from(".container video", {
  height: 0,
  width: 0,
  duration: 2,
  ease: "sine.out",
  delay: 5,

})
gsap.from(".header", {
  y: "-100%",
  duration: 2,
  delay: 6.5,
  ease: "bounce",
  scrub: 1

})



gsap.to("#nav", {
  backgroundColor: "#0e100f",
  duration: 1.5,
  height: "80px",
  scrollTrigger: {
    trigger: "#nav",
    scroller: "body",
    // markers:true,
    start: "740px",
    // end: "top -11%",
    scrub: 1
  },
});

