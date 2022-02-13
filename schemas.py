from datetime import datetime
from pydantic import BaseModel, EmailStr
from datetime import datetime


class Post(BaseModel):
    title: str
    content: str
    published: bool        #pydantic field assigns the default value True if the field is not 
                                    #present in request body #Optional field, pydantic only checks the 
                                    #  fields if it present in request body, if not rating is null/None

class PostOut(Post):
    created_at: datetime
    id:int
    
    class Config:
        orm_mode = True
    
class UserCreate(BaseModel):
    email:EmailStr
    password: str
    
class UserOut(BaseModel):
    id:int
    email:EmailStr
    
    class Config:
        orm_mode = True
        
class userLogin(BaseModel):
    email:EmailStr
    password: str
    