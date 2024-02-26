import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
      import {
        getDatabase,
        get,
        ref,
        child,
      } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";
      import {
        getAuth,
        signInWithEmailAndPassword,
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
      let signInForm = document.getElementById("sign-in");
      function setCookie(name, value, exp_days) {
        var d = new Date();
        d.setTime(d.getTime() + exp_days * 24 * 60 * 60 * 1000);
        var expires = "expires=" + d.toGMTString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
      }

      let SignUser = (evt) => {
        evt.preventDefault();
        // The below funtion checks if user's authenticated or not aand if yes it goes inside the then function
        signInWithEmailAndPassword(auth, EmailInp.value, PassInp.value)
          .then((credentials) => {
            get(child(dbref, "UserAuthList/" + credentials.user.uid)).then(
              (snapshot) => {
                if (snapshot.exist) {
                  sessionStorage
                    .setItem(
                      "user-info",
                      JSON.stringify({
                        name: snapshot.val().Name,
                      })
                    )
                    .sessionStorage.setItem(
                      "user-creds",
                      JSON.stringify(credentials.user)
                    );
                  window.location.href = "/index.html";
                }
              }
            );
            console.log(credentials);
            console.log(credentials.user.uid);
          })
          .catch((error) => {
            alert(error.code);
            console.log(error.code);
            console.log(error.message);
          });
      };
      signInForm.addEventListener("submit", SignUser);
      signInForm.addEventListener("submit", (evt) => setCookie("user-info", name.value, 1));