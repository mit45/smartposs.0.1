from fastapi import FastAPI, HTTPException
from auth import authenticate_user

app = FastAPI()

@app.post("/login")
def login(username: str, password: str):
    if authenticate_user(username, password):
        return {"message": "Giriş başarılı", "token": "örnek_token_123"}
    else:
        raise HTTPException(status_code=401, detail="Kullanıcı adı veya şifre hatalı")
