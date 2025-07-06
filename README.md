# AIAttendanceSystem
Tech Stack  - Python - OpenCV - `face_recognition` (dlib-based) - NumPy, Pandas - CSV for data storage (can be upgraded to MySQL/SQLite)
Bhai, second project ke liye **AI-Based Attendance System** ek दम 🔥 idea hai — real-world use case, CV ke लिए perfect, aur future-ready bhi.



```markdown
# 👁️‍🗨️ AI-Based Attendance System

A Smart Face Recognition Attendance System built with Python, OpenCV, and Face Recognition library. Automates attendance marking by detecting and identifying faces from a live camera feed.

---

## 🎯 Key Features

- 🧠 Real-time face detection and recognition
- 🧾 Attendance automatically marked with name and timestamp
- 💾 Stores data in CSV/Excel file
- 📷 Webcam or IP camera supported
- 🔒 Prevents duplicate attendance for same person

---

## 🧰 Tech Stack

- Python
- OpenCV
- `face_recognition` (dlib-based)
- NumPy, Pandas
- CSV for data storage (can be upgraded to MySQL/SQLite)

---

## 📁 Folder Structure

```

AI-Attendance-System/
│
├── main.py                   # Entry point
├── train\_images/             # Folder of student images (for training)
├── face\_recognition.py       # Face encoding and matching logic
├── attendance.py             # Handles attendance recording
├── utils.py                  # Helper functions
├── attendance.csv            # Output file with attendance logs
├── requirements.txt          # All dependencies
└── README.md                 # This file

````

---

## 🚀 How It Works

1. Place face images in `train_images/` folder (file name = person name).
2. Run the app.
3. System starts webcam, detects faces, and matches with known ones.
4. If matched → logs name and timestamp in `attendance.csv`.

---

## 🛠️ Installation

1. Clone the repo:
```bash
git clone https://github.com/YourUsername/AI-Attendance-System.git
cd AI-Attendance-System
````

2. Install required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run The App

```bash
python main.py
```

Make sure your webcam is working. Adjust the threshold in face comparison if needed.

---

## 📊 Sample Output (CSV)

| Name   | Time        | Date       |
| ------ | ----------- | ---------- |
| Akshat | 10:03:12 AM | 2025-07-06 |
| Hitika | 10:04:01 AM | 2025-07-06 |

---

## 🧠 Future Improvements

* GUI dashboard using Tkinter or PyQt
* Save face encodings in database
* Email alerts for proxy detection
* Live IP camera support
* Firebase/MySQL integration

---

## 🙌 Credits

Developed by \[Your Name]
Using `face_recognition` library by Adam Geitgey

---

## 🌟 Support

If you found this useful, give it a ⭐️ on GitHub and share!

````

---

### 📥 What You Should Do Now:

1. Paste this as `README.md` in your **AI Attendance System** folder  
2. Run these Git commands:

```bash
git add README.md
git commit -m "Added README for AI Attendance System"
git push
````

---

