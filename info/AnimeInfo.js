// languagePluginUrl = 'https://cdn.jsdelivr.net/pyodide/dev/full/';
// pyodide = await loadPyodide({ indexURL : languagePluginUrl });
// let python_code = `
// import js
// `
// (async () => { // enable await
//   await pyodide.loadPackagesFromImports(python_code)
//   let result = await pyodide.runPythonAsync(python_code)
//   console.log(result.toJs())
// })() // call the function immediately


// await pyodide.loadPackage("beautifulsoup4");
// await pyodide.runPythonAsync(`
//   from pyodide.http import pyfetch
//   response = await pyfetch("https://files.pythonhosted.org/packages/64/af/b5014d1387a3db9b2fff21ca766d38f6616e3bd6576216bb64fec9d1a6d8/javascript-1!1.1.2.tar.gz")
//   await response.unpack_archive()
// `)

gsap.to(".counter", 0.25, {
    delay: 3.5,
    opacity: 0,
});
gsap.to(".bar", 1.5, {
    delay: 3.5,
    height: 0,
    stagger: {
        amount: 0.5,
    },
    ease: "power4.inOut",

});
setTimeout(() => {
    var a = document.getElementById("mkc");
    a.style.zIndex = -1000;
    var a = document.getElementById("mkc-2");
    a.style.zIndex = -1000;
    clearTimeout(setTimeout);
}, 5000);

function tope() {
    window.scrollTo(0, 0);
}

const btn = document.querySelector(".Nav_btn");
btn.onmousemove = function (e) {
    const x = e.pageX - btn.offsetLeft;
    const y = e.pageY - btn.offsetTop;

    btn.style.setProperty("--x", x + "px");
    btn.style.setProperty("--y", y + "px");
}


