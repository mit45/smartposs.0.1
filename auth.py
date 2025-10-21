import json
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "super_secret_key_123"  # Gerçek sistemde .env dosyasına yazılacak
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def authenticate_user(username, password):
    with open("users.json", "r", encoding="utf-8") as f:
        users = json.load(f)

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
