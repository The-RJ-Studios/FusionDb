<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body onload="tope()">
    <h1 id="mkc" class="counter">
      <!-- <img src="/pics/icons8-loading-circle.gif" alt=""> -->
      <input id="demo" value="0" />
    </h1>
    <div id="mkc-2" class="overlay">
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
      <div class="bar"></div>
    </div>

    <div id="page1">
      <!-- nav section -->
      <div id="nav" class="header">
        <img class="nav-elem" src="/pics/Logo.png" alt="" />
        <h4 class="nav-elem"><a href="/index.html">Home</a></h4>
        <h4 class="nav-elem"><a href="/pages/manga/index.html">Manga</a></h4>
        <h4 class="nav-elem"><a href="/pages/movies/index.html">Movies</a></h4>
        <form id="form">
          <input class="nav-elem" type="text" placeholder="Type to search" id="Search" />
        </form>
        <div id="nav2">
          <a class="nav-elem" href="/pages/registration/register.html">
            <button class="Nav_btn" class="nav-elem"><span>Register</span></button>
            <!-- <i class="fa-solid fa-circle-user"></i> -->
          </a>
        </div>
    </div>

    <div class="page-content">
      <div class="container">
        <div class="result">
          <div class="media-card">
           <a href="" class="cover">

          <img src="/pics/Ghoul.jpg" alt="" class="image loaded">

           </a> 
           <a href="" class="title">

           Title of an anime long title

           </a>
          </div>
      </div>
    </div>
    </div>
  </div>
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"
      integrity="sha512-7eHRwcbYkK4d9g/6tD/mhkf++eoTHwpNM9woBxtPUBWm67zeAfFC+HrdoE2GanKeocly/VxeLvIqwvCdk7qScg=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"
      integrity="sha512-onMTRKJBKz8M1TnqqDuGBlowlH0ohFzMXYRNebz+yOcc5TQr/zAKsthzhuv0hiyUKEiQEQXEynnXCvNTOk50dg=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
    <script src="/search/script.js"></script>
    <script src="/pages/anime.min.js"></script>
    <script>
      anime({
        targets: "#demo",
        value: [0, 100],
        easing: "linear",
        round: 1,
        duration: 3000,
      });
    </script>
  </body>
</html>