import cv2
from deepface import DeepFace


class FaceObject:
    def __init__(self, identity, source_x, source_y, source_w, source_h):
        self.identity = identity
        self.source_x = source_x
        self.source_y = source_y
        self.source_w = source_w
        self.source_h = source_h


# 加载摄像头
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

faces = []
face_match = False

reference_path = "database"

backends = [
  'opencv',
  'ssd',
  'dlib',
  'mtcnn',
  'retinaface',
  'mediapipe'
]


def face_det(video_frame):
    global faces, face_match
    try:
        faces = []
        face_objs = DeepFace.extract_faces(video_frame, detector_backend=backends[4])
        print(face_objs)
        if len(face_objs):
            face_match = True
            for face in face_objs:
                face_x = face['facial_area']['x']
                face_y = face['facial_area']['y']
                face_w = face['facial_area']['w']
                face_h = face['facial_area']['h']
                faces.append(FaceObject('', face_x, face_y, face_w, face_h))
        else:
            faces = []
            face_match = False
    except ValueError:
        faces = []
        face_match = False


while True:
    # 读取摄像头帧
    ret, frame = cap.read()

    if ret:
        face_det(frame)
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
