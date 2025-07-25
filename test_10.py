import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

image = cv2.imread("me_2_2.jpg")
results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

for face in results.multi_face_landmarks:
    for i, point in enumerate(face.landmark):
        print(f"Point {i}: ({point.x}, {point.y}, {point.z})")
