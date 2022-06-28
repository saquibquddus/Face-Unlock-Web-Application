from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
import uvicorn
from webapp.router import crud
import os



app  = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"], 
    allow_headers=["*"],
    max_age=2 
    )

app.include_router(crud.route)



if __name__ == '__main__':
    port=8000
    uvicorn.run(app,host="0.0.0.0",port=port)