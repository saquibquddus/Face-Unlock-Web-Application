
from pymongo import MongoClient
import pymongo
import ssl

try:
    # client = MongoClient("mongodb://sandeepjena:Siku8339@cluster0-shard-00-00.tetcj.mongodb.net:27017,cluster0-shard-00-01.tetcj.mongodb.net:27017,cluster0-shard-00-02.tetcj.mongodb.net:27017/?ssl=true&replicaSet=atlas-tzvisj-shard-0&authSource=admin&retryWrites=true&w=majority")
    
    # client = pymongo.MongoClient("mongodb+srv://mohan:faceunlock@faceunlock.jb92s.mongodb.net/?retryWrites=true&w=majority")

    # client = MongoClient("localhost",27017)
    # client=MongoClient("mongodb+srv://mksaquib:mksaquib@cluster0.tetcj.mongodb.net/?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

    client = MongoClient("mongodb+srv://saquib1:saquib1@cluster0.f4teh.mongodb.net/?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)

except pymongo.errors.ConfigurationError as e :
    raise e
except pymongo.errors.ConnectionFailure as f:
    raise f
    
store = client.storehash
db = store['All_User_Data']