import re
import cv2
import threading
from deepface import DeepFace
from face_base import MODELS, DETECTORS, FaceObject

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

faces = []
face_match = False

reference_path = "database"
reference_img_path = "database/mars/mars1.jpg"
reference_img = cv2.imread(reference_img_path)


def face_rec_find(video_frame):
    global faces, face_match
    try:
        face_results = DeepFace.find(video_frame, reference_path, model_name=MODELS[0], detector_backend=DETECTORS[0])
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


def face_rec_verify(video_frame):
    global faces, face_match
    try:
        result = DeepFace.verify(video_frame, reference_img, model_name=MODELS[0], detector_backend=DETECTORS[0])
        faces = []
        if result['verified']:
            face_match = True
            face_x = result['facial_areas']['img1']['x']
            face_y = result['facial_areas']['img1']['y']
            face_w = result['facial_areas']['img1']['w']
            face_h = result['facial_areas']['img1']['h']
            identity = re.sub(r"\d+$", "", reference_img_path.split("/")[-1].split(".")[0])
            faces.append(FaceObject(identity, face_x, face_y, face_w, face_h))
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
                threading.Thread(target=face_rec_verify, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            for face_obj in faces:
                x, y, w, h = face_obj.source_x, face_obj.source_y, face_obj.source_w, face_obj.source_h
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, face_obj.identity, (x, y + h + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
        else:
            cv2.putText(frame, "NOT MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
