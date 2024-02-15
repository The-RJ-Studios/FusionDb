import gsap from "gsap-trial";

/* The following plugins are Club GSAP perks */
import { ScrollSmoother } from "gsap-trial/ScrollSmoother";
import { MorphSVGPlugin } from "gsap-trial/MorphSVGPlugin";


gsap.registerPlugin(ScrollSmoother,MorphSVGPlugin);

let smoother = ScrollSmoother.create({
    wrapper: "#smooth-wrapper",
    content: "#smooth-content",
})
