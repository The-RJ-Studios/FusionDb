// function start(){
//     document.getElementById("boitext").style.zIndex = "-1000";
// }
function edit(){
    let gopaara = document.getElementById("boitext");
gopaara.style.opacity = "1";
}
function myFunction(event) {
    let para;
    let ogPara;
    para = document.getElementById("boitext").value;
    document.getElementById("boigar").innerHTML = para;


    if(para==""){
        return;
    }
    else{
        document.getElementById("boigar").innerHTML = para;
        event.preventDefault()
    }


  }