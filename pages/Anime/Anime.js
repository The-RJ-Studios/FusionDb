


// for popular 

const initSlider = () => {
  window.scrollTo(0, 0);
  const cardlayout = document.querySelector(".card-layout");
  const slideButtons = document.querySelectorAll(".slide-button");
  const maxScrollLeft = cardlayout.scrollWidth - cardlayout.clientWidth;
  slideButtons.forEach(button => {
    button.addEventListener("click", () => {
     
      const direction = button.id === "prev-slide" ? -1 : 1;
      const scrollAmount = cardlayout.clientWidth * direction;
      cardlayout.scrollBy({left: scrollAmount, behavior: "smooth"});
    });
  });
  const handleSideButtons = () => {
    
    slideButtons[0].style.display = cardlayout.scrollLeft <= 0 ? "none" : "block";
    slideButtons[1].style.display = cardlayout.scrollLeft >= 100 ? "none" : "block";
  }
  

  cardlayout.addEventListener("scroll",()=>{
    handleSideButtons();
  });

}


window.addEventListener("load", initSlider)

// for latest

const initSliderLat = () => {
  const cardlayoutL = document.querySelector(".card-layout-latest");
  const slideButtonsL = document.querySelectorAll(".slide-button-2");
  const maxScrollLeftL = cardlayoutL.scrollWidth - cardlayoutL.clientWidth;
  slideButtonsL.forEach(button => {
    button.addEventListener("click", () => {
     
      const directionL = button.id ==="prev-slide-2" ? -1 : 1;
      const scrollAmountL = cardlayoutL.clientWidth * directionL;
      cardlayoutL.scrollBy({left: scrollAmountL, behavior: "smooth"});
    });
  });
  const handleSideButtons = () => {
    slideButtons[0].style.display = cardlayout.scrollLeft <= 0 ? "none" : "block";
    slideButtons[1].style.display = cardlayout.scrollLeft >= 100 ? "none" : "block";
  }

  cardlayoutL.addEventListener("scroll",()=>{
    handleSideButtons();
  });

}


window.addEventListener("load", initSliderLat)


// random

const initSliderRan = () => {
  const cardlayoutR = document.querySelector(".card-layout-Random");
  const slideButtonsR = document.querySelectorAll(".slide-button-3");
  const maxScrollLeftR= cardlayoutR.scrollWidth - cardlayoutR.clientWidth;
  slideButtonsR.forEach(button => {
    button.addEventListener("click", () => {
     
      const directionR = button.id ==="prev-slide-3" ? -1 : 1;
      const scrollAmountR = cardlayoutR.clientWidth * directionR;
      cardlayoutR.scrollBy({left: scrollAmountR, behavior: "smooth"});
    });
  });
  const handleSideButtons = () => {
    slideButtonsR[0].style.display = cardlayout.scrollLeft <= 0 ? "none" : "block";
    slideButtonsR[1].style.display = cardlayout.scrollLeft >= 100 ? "none" : "block";
  }

  cardlayoutR.addEventListener("scroll",()=>{
    handleSideButtons();
  });

}


window.addEventListener("load", initSliderRan)
// function tope(){
//   window.scrollTo(0,0);
// }

// let sections = gsap.utils.toArray(".popu");

// gsap.to(sections,{

//     xPercent: -100 * (sections.length-4.5),
//     ease: "slow(0.7,0.7,false)",
//     scrollTrigger: {
//         trigger: ".all-card-pop",
//         pin: true,
//         // start: "top",
//         // end:"100px",
//         markers: true,
//         scrub: 1,
//         snap: 1 / (sections.length-4.5),
//         end: () => "+=" + 
//         document.querySelector(".all-card-pop").offsetWidth

//     }
// });


// let sectionsL = gsap.utils.toArray(".popi");

// gsap.to(sectionsL,{

//     xPercent: -100 * (sectionsL.length-4.5),
//     ease: "slow(0.7,0.7,false)",
//     scrollTrigger: {
//         trigger: ".all-card-lat",
//         pin: true,
//         // start: "top",
//         // end:"100px",
//         markers: true,
//         scrub: 1,
//         snap: 1 / (sectionsL.length-4.5),
//         end: () => "+=" + 
//         document.querySelector(".all-card-lat").offsetWidth

//     }
// });
// let sectionsR = gsap.utils.toArray(".popo");

// gsap.to(sectionsR,{

//     xPercent: -100 * (sectionsR.length-4.5),
//     ease: "slow(0.7,0.7,false)",
//     scrollTrigger: {
//         trigger: ".all-card-ran",
//         pin: true,
//         // start: "top",
//         // end:"100px",
//         markers: true,
//         scrub: 1,
//         snap: 1 / (sectionsR.length-4.5),
//         end: () => "+=" + 
//         document.querySelector(".all-card-ran").offsetWidth

//     }
// });

// gsap.to(".counter",0.25,{
//     delay: 1.5,
//     opacity: 0,
//   });
//   gsap.to(".bar",1.5,{
//     delay: 1.5,
//     height: 0,
//     stagger: {
//       amount: 0.5,
//     },
//     ease: "power4.inOut",
  
//   });
//   gsap.from("#h1",1.5,{
//     delay: 1.5, 
//     y: 700,
//     stagger: {
//       amount: 0.5,
//     },
//     ease : "power4.inOut",
//   });
//   setTimeout(() => {
//     var a = document.getElementById("mkc");
//     a.style.zIndex=-100; 
//     var a = document.getElementById("mkc-2");
//     a.style.zIndex=-100;
//     clearTimeout(setTimeout);
//   }, 5000);