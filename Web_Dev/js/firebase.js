const firebaseConfig = {
    apiKey: "AIzaSyDknpGYaLH-sUL9KUfUL0AzEQCd7aIOOgw",
    authDomain: "personalblog-fe4da.firebaseapp.com",
    projectId: "personalblog-fe4da",
    storageBucket: "personalblog-fe4da.appspot.com",
    messagingSenderId: "724551053296",
    appId: "1:724551053296:web:6fd1ef28adea70d9947735",
    measurementId: "G-89D0WW8ZVW"
  };
  
  // Initialize Firebase
firebase.initializeApp(firebaseConfig);
let db = firebase.firestore;