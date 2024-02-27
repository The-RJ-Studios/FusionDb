import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyABQtlWaFpJhoOqPNRYUFS_tFRtQnPKMaQ",
    authDomain: "m2adb2537.firebaseapp.com",
    projectId: "m2adb2537",
    storageBucket: "m2adb2537.appspot.com",
    messagingSenderId: "89155231634",
    appId: "1:89155231634:web:c826df5eb93b18cabb2b4b"
  };
  

const app = initializeApp(firebaseConfig);
const auth = getAuth(app)



export { app, auth };
