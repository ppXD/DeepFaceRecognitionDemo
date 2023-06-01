import cv2
import threading
from deepface import DeepFace

# 加载摄像头
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

face_match = False
face_coords = None

reference_img = cv2.imread("database/mars/mars1.jpg")

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


def check_face(video_frame):
    global face_match, face_coords
    try:
        result = DeepFace.verify(video_frame, reference_img, model_name=models[0])
        print(result)
        if result['verified']:
            face_match = True
            face_coords = result['facial_areas']['img1']
        else:
            face_match = False
    except ValueError:
        face_match = False


while True:
    # 读取摄像头帧
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(), )).start()
            except ValueError:
                pass
        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            x, y, w, h = face_coords['x'], face_coords['y'], face_coords['w'], face_coords['h']
            # 在图像中绘制人脸矩形框
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.putText(frame, "NOT MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('video', frame)

    # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
