from fastapi import APIRouter,Request,Response, status
from webapp.schema import User 
from webapp.database import db
from bson import ObjectId



route = APIRouter(
    prefix="/crud",
    tags=["crud"]
)

# =============== Starting CRUD operations ===================

@route.get("/{unique_id}")
def find_user(unique_id,request: Request,response: Response):
    print("FIND API HITTED")
    query = {"unique_id": unique_id}
    hash_data = [data for data in db.find(query)]
    response.status_code = status.HTTP_200_OK
    data = {}
    for i in hash_data:
        data[str(i["_id"])] = i['data']
        
    return  data


@route.post("/")
def create_user(data:User,request:Request,response: Response):
    print("POST API HITTED")
    db.insert_one(dict(data))
    response.status_code = status.HTTP_201_CREATED
    return response
    

@route.put("/{_id}")
def update_user(_id,data:User,request:Request,response: Response):
    print("PUT API HITTED")
    print(_id)
    db.find_one_and_update(
                            {"_id":ObjectId(_id)},
                            {"$set":dict(data)})
    response.status_code = status.HTTP_201_CREATED
    return response

@route.delete("/{_id}")
def delete(_id,request:Request,response: Response):
    print("DELETE API HITTED")
    db.find_one_and_delete({"_id":ObjectId(_id)})
    response.status_code = status.HTTP_301_MOVED_PERMANENTLY
    return response
