import subprocess, os

python_exe = os.sys.executable  # current Python

subprocess.run([python_exe, "get_faces_from_camera_tkinter.py"])
subprocess.run([python_exe, "features_extraction_to_csv.py"])
subprocess.run([python_exe, "attendance_taker.py"])

# Run Flask app in the same console
subprocess.run([python_exe, "app.py"])