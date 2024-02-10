// function start(){
//     document.getElementById("boitext").style.zIndex = "-1000";
// }
gsap.to(".counter", 0.25, {
    delay: 3.5,
    opacity: 0,
    ease: "power4.inOut"
});
gsap.to(".bar", 1.5, {
    delay: 3.5,
    height: 0,
    stagger: {
        amount: 0.5,
    },
    ease: "power4.inOut"

});
setTimeout(() => {
    var a = document.getElementById("mkc");
    a.style.zIndex = -100;
    var a = document.getElementById("mkc-2");
    a.style.zIndex = -100;
    clearTimeout(setTimeout);
}, 5000);
function edit() {
    let gopaara = document.getElementById("boitext");
    gopaara.style.opacity = "1";
}
function myFunction(event) {
    let para;
    let ogPara;
    para = document.getElementById("boitext").value;
    document.getElementById("boigar").innerHTML = para;


    if (para == "") {
        return;
    }
    else {
        document.getElementById("boigar").innerHTML = para;
        event.preventDefault()
    }


}