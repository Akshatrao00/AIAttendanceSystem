import cv2
import os
import pandas as pd
from datetime import datetime
from deepface import DeepFace

# Get full path to known_faces
known_faces_path = os.path.join(os.getcwd(), "known_faces")

if not os.path.exists(known_faces_path):
    print("❌ Folder 'known_faces' not found.")
    exit()

csv_file = "attendance.csv"
if not os.path.exists(csv_file):
    with open(csv_file, "w") as f:
        f.write("Name,Time\n")

# Attendance mark
def mark_attendance(name):
    df = pd.read_csv(csv_file)
    if name not in df['Name'].values:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(csv_file, "a") as f:
            f.write(f"{name},{now}\n")
        print(f"✅ Marked attendance for: {name} at {now}")

# Start webcam
cap = cv2.VideoCapture(0)
print("📷 Camera started. Press 'q' to quit.")

frame_count = 0
skip_frames = 5  # Process every 5th frame

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to access camera.")
        break

    frame_count += 1
    if frame_count % skip_frames != 0:
        cv2.imshow("AI Attendance System", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    try:
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        results = DeepFace.find(img_path=small_frame, db_path=known_faces_path, enforce_detection=False)

        if isinstance(results, list) and len(results) > 0 and not results[0].empty:
            identity_path = results[0].loc[0, 'identity']
            name = os.path.splitext(os.path.basename(identity_path))[0]
            mark_attendance(name)
            cv2.putText(frame, f"Detected: {name}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    except Exception as e:
        print(f"⚠️ Error: {e}")

    cv2.imshow("AI Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
