class FaceObject:
    def __init__(self, identity, source_x, source_y, source_w, source_h):
        self.identity = identity
        self.source_x = source_x
        self.source_y = source_y
        self.source_w = source_w
        self.source_h = source_h


MODELS = [
  "VGG-Face",    # 0
  "Facenet",     # 1
  "Facenet512",  # 2
  "OpenFace",    # 3
  "DeepFace",    # 4
  "DeepID",      # 5
  "ArcFace",     # 6
  "Dlib",        # 7
  "SFace",       # 8
]

DETECTORS = [
  'opencv',      # 0
  'ssd',         # 1
  'dlib',        # 2
  'mtcnn',       # 3
  'retinaface',  # 4
  'mediapipe'    # 5
]