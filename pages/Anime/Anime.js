const initSlider = () => {
  const cardlayout = document.querySelector(".card-layout");
  const slideButtons = document.querySelectorAll(".slide-button");
  const maxScrollLeft = cardlayout.scrollWidth - cardlayout.clientWidth;
  slideButtons.forEach(button => {
    button.addEventListener("click", () => {
     
      const direction = button.id ==="prev-slide" ? -1 : 1;
      const scrollAmount = cardlayout.clientWidth * direction;
      cardlayout.scrollBy({left: scrollAmount, behavior: "smooth"});
    });
  });
  const handleSideButtons = () => {
    slideButtons[0].style.display = cardlayout.scrollLeft <= 0 ? "none" : "block";
    slideButtons[1].style.display = cardlayout.scrollLeft >= maxScrollLeft ? "none" : "block";
  }

  cardlayout.addEventListener("scroll",()=>{
    handleSideButtons();
  });

}


window.addEventListener("load", initSlider)