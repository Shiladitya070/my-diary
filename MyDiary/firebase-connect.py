import pyrebase;


firebaseConfig = {
  "apiKey": "AIzaSyALfAB9udR3jjUSDh_VYo6W1Fqh-sQ9Xk4",
  "authDomain": "soicalmonkey.firebaseapp.com",
  "databaseURL": "https://soicalmonkey.firebaseio.com",
  "projectId": "soicalmonkey",
  "storageBucket": "soicalmonkey.appspot.com",
  "messagingSenderId": "271386049431",
  "appId": "1:271386049431:web:89becd8ac6a3f9ae7de2d2",
  "measurementId": "G-5BKGTT3RX6"
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()