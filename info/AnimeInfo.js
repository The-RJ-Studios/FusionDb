


// await pyodide.loadPackage("micropip");
// const micropip = pyodide.pyimport("micropip");
// await micropip.install('snowballstemmer');
// pyodide.runPython(`
//   import snowballstemmer
//   stemmer = snowballstemmer.stemmer('english')
//   print(stemmer.stemWords('go goes going gone'.split()))
// `);
// var languagePluginUrl = 'https://cdn.jsdelivr.net/pyodide/dev/full/';
// pyodide = await loadPyodide({ indexURL : languagePluginUrl });
// let python_code = `
// import js
// `
// (async () => { // enable await
//   await pyodide.loadPackagesFromImports(python_code)
//   let result = await pyodide.runPythonAsync(python_code)
//   console.log(result.toJs())
// })() // call the function immediately

// let python_code = `import js`
// async function main(){
//     // await loadPyodide({
//     //   indexURL : "https://cdn.jsdelivr.net/pyodide/dev/full/"
//     // });
//     await pyodide.loadPackage(
//         "https://files.pythonhosted.org/packages/84/0f/44a5b3455ecb48e7610386b44b838dd6356eb17d11dfe4d344b6a54d99e0/URLSearchParams-1.2-py3-none-any.whl",
//       );
// //     await pyodide.loadPackagesFromImports(python_code)
// //   let result = await pyodide.runPythonAsync(python_code)
// //   console.log(result.toJs())
//     // console.log(pyodide.runPython(`
//     //     import sys
//     //     sys.version
//     // `));
//     console.log(pyodide.runPython(`print(1 + 2)`));
//   }
// main();
// await pyodide.loadPackage("beautifulsoup4");
// await pyodide.runPythonAsync(`
//   from pyodide.http import pyfetch
//   response = await pyfetch("https://files.pythonhosted.org/packages/64/af/b5014d1387a3db9b2fff21ca766d38f6616e3bd6576216bb64fec9d1a6d8/javascript-1!1.1.2.tar.gz")
//   await response.unpack_archive()
// `)

// gsap.to(".counter", 0.25, {
//     delay: 3.5,
//     opacity: 0,
// });
// gsap.to(".bar", 1.5, {
//     delay: 3.5,
//     height: 0,
//     stagger: {
//         amount: 0.5,
//     },
//     ease: "power4.inOut",

// });
// setTimeout(() => {
//     var a = document.getElementById("mkc");
//     a.style.zIndex = -1000;
//     var a = document.getElementById("mkc-2");
//     a.style.zIndex = -1000;
//     clearTimeout(setTimeout);
// }, 5000);




/// REMEMEBER TO ENABLE LATER
// function tope() {
//     window.scrollTo(0, 0);
// }

// const btn = document.querySelector(".Nav_btn");
// btn.onmousemove = function (e) {
//     const x = e.pageX - btn.offsetLeft;
//     const y = e.pageY - btn.offsetTop;

//     btn.style.setProperty("--x", x + "px");
//     btn.style.setProperty("--y", y + "px");
// }


