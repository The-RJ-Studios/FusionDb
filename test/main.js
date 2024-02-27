async function main() {
    let pyodide = await loadPyodide();
    await pyodide.loadPackage("micropip");
    const micropip= pyodide.pyimport("micropip");
    await micropip.install("pulp");
    let pythonCode = await((await fetch("main.py")).text());
    // Pyodide is now ready to use...
    console.log(pyodide.runPython(pythonCode));
};
main();