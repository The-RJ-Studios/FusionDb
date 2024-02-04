// for popular 

const initSlider = () => {
    const cardlayout = document.querySelector(".card-layout");
    const slideButtons = document.querySelectorAll(".slide-button");
    const maxScrollLeft = cardlayout.scrollWidth - cardlayout.clientWidth;
    slideButtons.forEach(button => {
        button.addEventListener("click", () => {

            const direction = button.id === "prev-slide" ? -1 : 1;
            const scrollAmount = cardlayout.clientWidth * direction;
            cardlayout.scrollBy({ left: scrollAmount, behavior: "smooth" });
        });
    });
    const handleSideButtons = () => {
        slideButtons[0].style.display = cardlayout.scrollLeft <= 0 ? "none" : "block";
        slideButtons[1].style.display = cardlayout.scrollLeft >= maxScrollLeft ? "none" : "block";
    }

    cardlayout.addEventListener("scroll", () => {
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

            const directionL = button.id === "prev-slide-2" ? -1 : 1;
            const scrollAmountL = cardlayoutL.clientWidth * directionL;
            cardlayoutL.scrollBy({ left: scrollAmountL, behavior: "smooth" });
        });
    });
    const handleSideButtons = () => {
        slideButtonsL[0].style.display = cardlayoutL.scrollLeft <= 0 ? "none" : "block";
        slideButtonsL[1].style.display = cardlayoutL.scrollLeft >= maxScrollLeftL ? "none" : "block";
    }

    cardlayoutL.addEventListener("scroll", () => {
        handleSideButtons();
    });

}


window.addEventListener("load", initSliderLat)


// random

const initSliderRan = () => {
    const cardlayoutR = document.querySelector(".card-layout-Random");
    const slideButtonsR = document.querySelectorAll(".slide-button-3");
    const maxScrollLeftR = cardlayoutR.scrollWidth - cardlayoutR.clientWidth;
    slideButtonsR.forEach(button => {
        button.addEventListener("click", () => {

            const directionR = button.id === "prev-slide-3" ? -1 : 1;
            const scrollAmountR = cardlayoutR.clientWidth * directionR;
            cardlayoutR.scrollBy({ left: scrollAmountR, behavior: "smooth" });
        });
    });
    const handleSideButtons = () => {
        slideButtonsR[0].style.display = cardlayoutR.scrollLeft <= 0 ? "none" : "block";
        slideButtonsR[1].style.display = cardlayoutR.scrollLeft >= maxScrollLeftR ? "none" : "block";
    }

    cardlayoutR.addEventListener("scroll", () => {
        handleSideButtons();
    });

}


window.addEventListener("load", initSliderRan)