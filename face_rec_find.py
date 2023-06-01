import re
import cv2
import threading
from deepface import DeepFace


class FaceObject:
    def __init__(self, identity, source_x, source_y, source_w, source_h):
        self.identity = identity
        self.source_x = source_x
        self.source_y = source_y
        self.source_w = source_w
        self.source_h = source_h


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

faces = []
face_match = False

reference_path = "database"


models = [
  "VGG-Face",
  "Facenet",
  "Facenet512",
  "OpenFace",
  "DeepFace",
  "DeepID",
  "ArcFace",
  "Dlib",
  "SFace",
]

backends = [
  'opencv',
  'ssd',
  'dlib',
  'mtcnn',
  'retinaface',
  'mediapipe'
]


def face_rec(video_frame):
    global faces, face_match
    try:
        face_results = DeepFace.find(video_frame, reference_path, model_name=models[0], detector_backend=backends[0])
        faces = []
        if len(face_results):
            has_face = False
            for face in face_results:
                if len(face):
                    has_face = True
                    face_x = face['source_x'].values[0]
                    face_y = face['source_y'].values[0]
                    face_w = face['source_w'].values[0]
                    face_h = face['source_h'].values[0]
                    identity = re.sub(r"\d+$", "", face['identity'].values[0].split("/")[-1].split(".")[0])
                    faces.append(FaceObject(identity, face_x, face_y, face_w, face_h))
            face_match = has_face
        else:
            faces = []
            face_match = False
    except ValueError:
        faces = []
        face_match = False


while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=face_rec, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            for face_obj in faces:
                x, y, w, h = face_obj.source_x, face_obj.source_y, face_obj.source_w, face_obj.source_h
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.putText(frame, "NOT MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
