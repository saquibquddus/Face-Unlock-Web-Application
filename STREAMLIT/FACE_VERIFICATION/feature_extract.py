import face_recognition
class FaceExtractor:
    def __init__(self):
        # self.kEncodings = []
        pass

    def face_extractor(self, image, boxes):
        kEncodings = []
        encodings = face_recognition.face_encodings(image, boxes)
        for encoding in encodings:
            kEncodings.append(encoding)
        return kEncodings
