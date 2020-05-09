import pyrebase

config = {
    "apiKey": "AIzaSyATfSL4XgBp8JuLLohS6w0_8EkdZq4Sqrw",
    "authDomain": "site-b6d35.firebaseapp.com",
    "databaseURL": "https://site-b6d35.firebaseio.com",
    "projectId": "site-b6d35",
    "storageBucket": "site-b6d35.appspot.com",
    "messagingSenderId": "256405613769",
    "appId": "1:256405613769:web:b2a3057c73d0b041a83118",
    "measurementId": "G-Q0BE9FG0Z7"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "images/smurai.jpg"
path_local = "manga.jpg"
storage.child(path_on_cloud).put(path_local)
