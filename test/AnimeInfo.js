response.addHeader("Access-Control-Allow-Origin", "*");
languagePluginUrl = 'https://cdn.jsdelivr.net/pyodide/dev/full/';
pyodide = await loadPyodide({ indexURL : languagePluginUrl });
let python_code = `
import js
`
(async () => { // enable await
  await pyodide.loadPackagesFromImports(python_code)
  let result = await pyodide.runPythonAsync(python_code)
  console.log(result.toJs())
})() // call the function immediately
fetch("get.php").then(response =>{
  return response.json();
}).then(console.log("Header sent"));

await pyodide.loadPackage("beautifulsoup4");
await pyodide.runPythonAsync(`
  from pyodide.http import pyfetch
  response = await pyfetch("https://files.pythonhosted.org/packages/64/af/b5014d1387a3db9b2fff21ca766d38f6616e3bd6576216bb64fec9d1a6d8/javascript-1!1.1.2.tar.gz")
  await response.unpack_archive()
`)
function loader(){
  fetch("get.php").then(response =>{
    return response.json();
}).then(console.log("Header sent"));
}
function myFunction() 
{
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");
  
    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
}
