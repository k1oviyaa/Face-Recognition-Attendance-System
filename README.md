Face Recognition Attendance System
Overview

This project is a Python-based Face Recognition Attendance System. It captures faces via webcam, extracts facial features, marks attendance automatically, and displays it on a web interface using Flask.

It is designed to help automate attendance in classrooms or offices using facial recognition technology.

Features

Capture faces using webcam

Extract and store facial features

Real-time attendance marking

Web interface to view attendance records

Uses SQLite for storing attendance data

Technologies Used

Python

OpenCV → for capturing and processing images

dlib → for facial recognition

Flask → web interface

SQLite → database to store attendance

Tkinter → optional GUI for face capture
Installation

Clone the repository:

git clone https://github.com/your-username/Face-Recognition-Attendance-System.git
cd Face-Recognition-Based-Attendance-System
pip install -r requirements.txt
How to Run

Run the full system:

python run_all.py

Follow the prompts:

Capture faces

Extract features

Mark attendance

Web interface opens automatically at: http://127.0.0.1:5000

Optional: You can run each script separately:

get_faces_from_camera_tkinter.py → capture faces

features_extraction_to_csv.py → extract features

attendance_taker.py → mark attendance

app.py → launch web interface
