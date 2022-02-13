import utils
from fastapi import HTTPException
from fastapi import Depends, FastAPI, Response, status
from pydantic import BaseModel
from database import engine,get_db
import models
from sqlalchemy.orm import Session
import schemas
from routers import auth,post,user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)

 
@app.get("/")
async def root():
    return {"message": "Hello World"}