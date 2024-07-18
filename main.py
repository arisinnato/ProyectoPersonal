from fastapi import FastAPI
from database import engine, Base
from usuarios import router as user_router
from tipos_usuario import router as tipo_usuario_router

app = FastAPI()

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(tipo_usuario_router.router, prefix="/tipo_usuario", tags=["tipo_usuario"])
