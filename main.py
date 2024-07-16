from fastapi import FastAPI
from users.models import user
from database import SessionLocal, engine 
from sqlalchemy.orm import sessionmaker

# Create the database tables
user.Base.metadata.create_all(bind=engine)
#product.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Nacre Online Store"}
