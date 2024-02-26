import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
      import {
        getDatabase,
        set,
        ref,
      } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";
      import {
        getAuth,
        createUserWithEmailAndPassword,
      } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";

      const firebaseConfig = {
        apiKey: "AIzaSyABQtlWaFpJhoOqPNRYUFS_tFRtQnPKMaQ",
        authDomain: "m2adb2537.firebaseapp.com",
        databaseURL: "https://m2adb2537-default-rtdb.firebaseio.com",
        projectId: "m2adb2537",
        storageBucket: "m2adb2537.appspot.com",
        messagingSenderId: "89155231634",
        appId: "1:89155231634:web:c826df5eb93b18cabb2b4b",
        measurementId: "G-P0KGHPKMCK",
      };

      const app = initializeApp(firebaseConfig);
      const db = getDatabase();
      const auth = getAuth(app);
      const dbref = ref(db);

      let name = document.getElementById("name");
      let EmailInp = document.getElementById("email");
      let PassInp = document.getElementById("pass");
      let registerForm = document.getElementById("sign-up");
      let RegisterUser = (evt) => {
        evt.preventDefault();
        //Creating user using this function
        createUserWithEmailAndPassword(auth, EmailInp.value, PassInp.value)
          .then((credentials) => {
            //Using set function to set data into database
            set(ref(db, "UserAuthList/" + credentials.user.uid), {
              //This Curly braces are objects
              Name: name.value,
            });
            /*get(child(dbref, 'UserAuthList/' + credentials.user.uid)).then((snapshot)=>{
                    if(snapshot.exist){
                        sessionStorage.setItem("user-info", JSON.stringify({
                            name: snapshot.val().Name
                            
                        }))
                        sessionStorage.setcoo("user-creds", JSON.stringify(credentials.user));
                        window.location.href = './Users/User.html';

                    }
                }
                )*/
          })
          .catch((error) => {
            alert(error.code);
            console.log(error.code);
            console.log(error.message);
          });
      };

      registerForm.addEventListener("submit", RegisterUser);