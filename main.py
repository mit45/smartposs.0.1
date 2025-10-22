from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from auth import authenticate_user, create_access_token, verify_token
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import User
from schemas import UserCreate, UserResponse
import bcrypt

app = FastAPI()

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if authenticate_user(username, password):
        access_token_expires = timedelta(minutes=60)
        access_token = create_access_token(
            data={"sub": username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Kullanıcı adı veya şifre hatalı")


# 🔒 Giriş yapılmadan erişilemeyen endpoint
@app.get("/products")
def get_products(username: str = Depends(verify_token)):
    return {"message": f"Hoş geldin {username}!", "products": ["Kalem", "Defter", "Silgi"]}

# 🧱 Veritabanını oluştur
Base.metadata.create_all(bind=engine)

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Kullanıcı adı zaten var mı?
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Bu kullanıcı adı zaten kayıtlı.")

    # Şifreyi hashle
    hashed_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    # Yeni kullanıcı oluştur
    new_user = User(username=user.username, password=hashed_pw.decode('utf-8'), role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user