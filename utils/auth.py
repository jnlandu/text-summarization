import os
# from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

#TODO: Add environment variables

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return password + "hashed"

#TODO: use a real database
users_db = {
    "admin": { "username": "admin", "password": hash_password("userpass"), "role": "admin" },
    "user": { "username": "user", "password": hash_password("userpass"), "role": "user" }
}

def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    if user and user['password'] == hash_password(password):
        return user
    return None
