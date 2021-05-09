import pyrebase

# connection establishment
firebaseConfig = {
    'apiKey': "AIzaSyBF-5wv5cyFVe2KmHPhY3fMx0ZlPvj403Y",
    'authDomain': "internship-4292c.firebaseapp.com",
    'databaseURL': 'https://internship-4292c-default-rtdb.firebaseio.com/',
    'projectId': "internship-4292c",
    'storageBucket': "internship-4292c.appspot.com",
    'messagingSenderId': "484348816343",
    'appId': "1:484348816343:web:ac5083a4b0f669451bf992",
    'measurementId': "G-0K3TYDT7PS"
}
# initilizing the server

firebase = pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
#Fetch the data

data=db.child('Personal_Details').get()
for each_data in data.each():
    name=each_data.val()['Name']
    age = each_data.val()['Age']
    contact = each_data.val()['Contact']
    email = each_data.val()['Email']
    phone = each_data.val()['Phone']




