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


const btn = document.querySelector(".Nav_btn");
btn.onmouseover = function(e){
  const x = e.pageX - btn.offsetLeft;
  const y = e.pageY - btn.offsetTop;

  btn.computedStyleMap.setProperty("--x", x + "px");
  btn.computedStyleMap.setProperty("--y", y + "px");
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

gsap.to(".counter",0.25,{
  delay: 1.5,
  opacity: 0,
});
gsap.to(".bar",1.5,{
  delay: 1.5,
  height: 0,
  stagger: {
    amount: 0.5,
  },
  ease: "power4.inOut",

});
gsap.from("#mkc",1.5,{
  delay: 1.5, 
  y: 700,
  stagger: {
    amount: 0.5,
  },
  ease : "power4.inOut",
});
setTimeout(() => {
  var a = document.getElementById("mkc");
  a.style.zIndex=-100; 
  var a = document.getElementById("mkc-2");
  a.style.zIndex=-100;
  clearTimeout(setTimeout);
}, 3000);
