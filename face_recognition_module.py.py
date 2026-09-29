import cv2
import face_recognition
import os
import numpy as np

# Load known face encodings and names
known_face_encodings = []
known_face_names = []

def load_known_faces(known_faces_dir="known_faces"):
    for filename in os.listdir(known_faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = face_recognition.load_image_file(f"{known_faces_dir}/{filename}")
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(os.path.splitext(filename)[0])

def recognize_user(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        return name
    return None

if __name__ == "__main__":
    load_known_faces()
    video_capture = cv2.VideoCapture(0)
    print("Starting Smart Mirror Camera Feed...")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        user = recognize_user(frame)
        if user:
            print(f"Welcome back, {user}!")
            # Trigger custom profile layout or API events here

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()