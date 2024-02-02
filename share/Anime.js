gsap.to("#nav", {
    backgroundColor: "#5338AC",
    duration: 0.5,
    height: "70px",
    scrollTrigger: {
      trigger: "#nav",
      scroller: "body",
      // markers:true,
      start: "top -10%",
      end: "top -11%",
      scrub: 1,
    },
  });