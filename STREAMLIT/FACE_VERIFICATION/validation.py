import cv2
from FACE_VERIFICATION.face_detector import FaceDetector
from FACE_VERIFICATION.feature_extract import FaceExtractor
import os
import pandas as pd
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from utils.encrypt import Encrypt



obj1 = FaceDetector()
obj2 = FaceExtractor()
obj3 = Encrypt()

class Verify:
    def __init__(self):
        self.metadata_dir = os.path.join('STREAMLIT',"Metadata")
        filename = "Embedding.pkl"
        self.embed_path = os.path.join(self.metadata_dir, filename)

    def verify(self,frame_count,WINDOW):
        count = 0
        cap = cv2.VideoCapture(0)
        while True:
            _,frame = cap.read()
            image, boxes =  obj1.face_detector(frame,WINDOW)
            if boxes is None:
                continue
            current_embed = obj2.face_extractor(image, boxes) 
            current_encodings = np.array(current_embed[0])       
            embed = self.file_chk()
            if embed:
                just_embed_keys = list(embed.keys())
                for ele in just_embed_keys:
                    for i in range(len(embed[ele])):
                        full_encodings = np.array(embed[ele][i]) ## Full encodings for one person
                        current_encodings = current_encodings.reshape(1,-1)
                        full_encodings = full_encodings.reshape(1,-1)
                        score  = cosine_similarity(current_encodings, full_encodings)
                        if score[0][0] * 100 > 93:
                            status = {"msg":"Verified","unique_id":ele}
                            return status
                        else:
                            status = {"msg":"Not Verified"}
                return status
            else:
                return {"msg":"Not Verified"}
            count+=1    
            if count >= frame_count:
                break

    def generate_embeds(self,frame_count=2,WINDOW=None):
        count = 0
        final_current_embeddings = []
        cap = cv2.VideoCapture(0)
        while True:
            _,frame = cap.read()
            image, boxes =  obj1.face_detector(frame,WINDOW)
            if boxes is None:
                continue
            current_embed = obj2.face_extractor(image, boxes)
            final_current_embeddings.append(current_embed[0])
            count+=1    
            if count >= frame_count:
                break
        embed = self.file_chk()
        if embed:
            len_id = len(embed)
            unique_id = len_id + 1
            embed[unique_id] = final_current_embeddings

        else:
            os.makedirs(self.metadata_dir,exist_ok=True)
            embed = {}
            embed[1] = final_current_embeddings

        with open(self.embed_path, 'wb') as f:
                pickle.dump(embed, f)
        # obj3.encrypt_file(self.embed_path)
        return "success"
           

    def file_chk(self):
        file_present = os.path.exists(self.embed_path)
        if file_present:
            # obj3.decrypt_file(self.embed_path)
            embed = pd.read_pickle(self.embed_path)
            return embed
        else:
            return False