from datetime import timedelta
from jose import JWTError, jwt
from datetime import datetime, timedelta

#Secret key
#Algorithm
#Expiration time

SECRET_KEY = "329850y4cb57-34657vb3=0142865-vb75675vb47560v7564"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)