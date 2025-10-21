from fastapi import FastAPI, HTTPException
from datetime import timedelta
from auth import authenticate_user, create_access_token

app = FastAPI()

@app.post("/login")
def login(username: str, password: str):
    if authenticate_user(username, password):
        access_token_expires = timedelta(minutes=60)
        access_token = create_access_token(
            data={"sub": username}, expires_delta=access_token_expires
        )
        return {"message": "Giriş başarılı", "token": access_token}
    else:
        raise HTTPException(status_code=401, detail="Kullanıcı adı veya şifre hatalı")
