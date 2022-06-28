from cryptography.fernet import Fernet
import pandas as pd
import os
import pickle
from dotenv import load_dotenv

class Encrypt:
    def __init__(self):
        load_dotenv()
        self.secrets_path = os.path.join('STREAMLIT','Metadata','secrets.pkl')
        # self.file_key = bytes(os.getenv('SECRET_KEY'),'utf-8')
        # self.file_cipher = self._get_cipher(self.file_key)
        # self.file_cipher = pd.read_pickle("useless.pkl")

    def _get_key(self):
        key = Fernet.generate_key()
        return key
    def _get_cipher(self,key):
        cipher = Fernet(key)
        return cipher

    def first_time_key_generator(self,unique_id):
        if not os.path.exists(self.secrets_path):
            key = self._get_key() # create a byte key
            key = key.decode()  # bytes to string
            data = {unique_id: key}
            with open(self.secrets_path, 'wb') as f:
                pickle.dump(data, f)
        #     self.encrypt_file(self.secrets_path)
        # self.decrypt_file(self.secrets_path)

    
    def fetch_key_per_user(self,unique_id,type=None):
        df = pd.read_pickle(self.secrets_path)
        if unique_id in df.keys():
            s_key = df[unique_id]
            s_key = bytes(s_key,'utf-8')
            return s_key
        elif type != None:
            raise Exception(f"Unique id {unique_id} is not present")
        else:
            s_key = self._get_key().decode()
            df[unique_id] = s_key
            with open(self.secrets_path, 'wb') as f:
                pickle.dump(df, f)
            # self.encrypt_file(self.secrets_path)
            return bytes(s_key,'utf-8')


    def encrypt_data(self,unique_id=None,userdata=None,key=None):
        self.first_time_key_generator(unique_id)
        key = self.fetch_key_per_user(unique_id)
        print(f"key used for encrypting is {key} ")
        cipher = self._get_cipher(key)
        result = []
        if isinstance(userdata,list):
            for ele in userdata:
                ele = bytes(ele,encoding='utf-8')
                result.append(cipher.encrypt(ele).decode())
            return result
        else:
            result = cipher.encrypt(userdata)
            return result

    def decrypt_data(self,unique_id,userdata):
        # self.decrypt_file(self.secrets_path)
        key = self.fetch_key_per_user(unique_id,"decrypt")
        print(f"key used for decrypting is {key} ")
        cipher = self._get_cipher(key)
        result = []
        if isinstance(userdata,list):
            for ele in userdata:
                ele = bytes(ele,encoding='utf-8')
                ele = cipher.decrypt(ele)
                result.append(ele.decode())
            return result
        else:
            result = bytes(ele,encoding='utf-8')
            result = cipher.decrypt(userdata)
            result = result.decode()
            return result


    # def encrypt_file(self,filepath):
    #     cipher = self._get_cipher(self.file_key)
    #     with open(filepath,"rb") as file:   #normal pickle
    #         file_data = file.read()
    #         result = cipher.encrypt(file_data)
    #     with open(filepath,"wb") as file:
    #         file.write(result)

    # def decrypt_file(self,filepath):
    #     cipher = self._get_cipher(self.file_key)
    #     with open(filepath,"rb") as file:
    #         file_data = file.read()
    #         result = cipher.decrypt(file_data)
    #     with open(filepath,"wb") as file:
    #         file.write(result)
