from fastapi import FastAPI
from database import engine
from tipos_usuario import router as tipos_usuario
from usuarios import router as usuarios
app = FastAPI()


