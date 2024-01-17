import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from google.cloud import storage as gcs_storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancefinal-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003117":
        {
            "name": "Dhruvi Jani",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003119":
        {
            "name": "Prumika Maiyani",
            "major": "Btech IT",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003121":
        {
            "name": "Aman Dalawat",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003122":
        {
            "name": "Jai Desai",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003124":
        {
            "name": "Prince Raj",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003128":
        {
            "name": "Arya Dixit",
            "major": "Btech IT",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003304":
        {
            "name": "Dixit Sarvani",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003460":
        {
            "name": "Mohit Raiyani",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003605":
        {
            "name": "Kunnal Jain",
            "major": "Btech IT",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003651":
        {
            "name": "Nandish Shah",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003723":
        {
            "name": "Amrendra Singh",
            "major": "Btech IT",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003736":
        {
            "name": "Harshil Kanpariya",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003737":
        {
            "name": "Manav Ramani",
            "major": "Btech IT",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003746":
        {
            "name": "Keval Jobanputra",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003794":
        {
            "name": "Jainam Savla",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003795":
        {
            "name": "Yuvrajsinh Vaghela",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003799":
        {
            "name": "Mazhar Ansari",
            "major": "Btech IT",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "U42000003874":
        {
            "name": "Arshad Sheikh",
            "major": "Btech CSE",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)