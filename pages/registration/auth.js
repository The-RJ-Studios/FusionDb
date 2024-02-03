import { initializeApp} from 'firebse/app';
import {
    getAuth,
    connectAuthEmulator,
    signInWithEmailAndPassword
}from 'firebase/auth';

const firebaseApp = initializeApp({
    apiKey:"AIzaSyABQtlWaFpJhoOqPNRYUFS_tFRtQnPKMaQ",
    authDomain: "m2adb2537.firebaseapp.com",
    databaseURL: "https://<DATABASE_NAME>.firebaseio.com",
    storageBucket: "<BUCKET>.appspot.com",
    messagingSenderId: "89155231634-b0au71hch2itm5gnh5kf0mdqlm1tnjh3.apps.googleusercontent.com",
})
const auth = getAuth(firebasseApp);
connectAuthEmulator(auth,"http://localhost:5500");

const loginEmailPass = async()=>{
    const loginEmail = getElementById("email").value
    const loginPass = getElementById("pass").value

    const userCredential = await signInWithEmailAndPassword(auth, loginEmail, loginPass);
    console.log(userCredential.user)

}