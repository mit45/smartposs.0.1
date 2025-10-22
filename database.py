from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL bağlantı adresi
# Buradaki bilgileri kendi sistemine göre değiştir:
# user=postgres, password=1234, host=localhost, port=5432, database=smartpos
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/smartpos"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Veritabanı oturumunu (session) almak için
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
