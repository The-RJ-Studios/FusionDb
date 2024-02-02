let counter = 1



setInterval(()=>{

    document.querySelector('.sliderimg.show').classList.remove('show')
    const img = document.querySelector(`.img-${counter}`)
    img.classList.add('show')
    counter++

    if(counter >3){
        counter = 1
    }

},3000)

gsap.to("#nav", {
    backgroundColor: "#5338AC",
    duration: 0.5,
    height: "90px",
    scrollTrigger: {
      trigger: "#nav",
      scroller: "body",
      // markers:true,
      start: "top -10%",
      end: "top -11%",
      scrub: 1,
    },
  });