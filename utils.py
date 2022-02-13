from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def get_hash(user_password: str):
    return pwd_context.hash(user_password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)