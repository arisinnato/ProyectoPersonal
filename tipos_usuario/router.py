from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import Respuesta
from database import SessionLocal, engine
import tipos_usuario.models as models 
import tipos_usuario.schemas as schemas
import tipos_usuario.service as service

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""@router.get('', response_model=list[schemas.Tipo_Usuario])
def listar_tipos_usuarios(db: Session = Depends(get_db)):
    return service.listar_tipos_usuarios(db=db)

@router.post('', response_model=Respuesta[schemas.Tipo_Usuario])
def crear_un_tipo_de_usuario(tipo_usuario: schemas.Tipo_UsuarioCrear, db: Session = Depends(get_db)):
    return service.crear_un_tipo_de_usuario(db=db, tipo_usuario=tipo_usuario)

@router.get('/{id}', response_model=schemas.Tipo_Usuario)
def buscar_un_tipo_de_usuario(id : int, db: Session = Depends(get_db)): 
    return service.buscar_un_tipo_de_usuario(db=db, id=id)

@router.delete('/{id}', response_model=schemas.Tipo_Usuario)
def eliminar_un_tipo_de_usuario(id : int, db: Session = Depends(get_db)): 
    return service.eliminar_un_tipo_de_usuario(db=db, id=id)"""

@router.get('', response_model=list[schemas.Tipo_Usuario])
def listar_tipos_usuarios(db: Session = Depends(get_db)):
    return service.listar_tipos_usuarios(db=db)

@router.post('', response_model=Respuesta[schemas.Tipo_Usuario])
def crear_un_tipo_de_usuario(tipo_usuario: schemas.el_Tipo_de_Usuario_ha_Crear, db: Session = Depends(get_db)):
    return service.crear_un_tipo_de_usuario(db=db, tipo_usuario=tipo_usuario)

@router.get('/{id}', response_model=schemas.Tipo_Usuario)
def buscar_un_tipo_de_usuario(id : int, db: Session = Depends(get_db)): 
    return service.buscar_un_tipo_de_usuario(db=db, id=id)

@router.delete('/{id}', response_model=schemas.Tipo_Usuario)
def eliminar_un_tipo_de_usuario(id : int, db: Session = Depends(get_db)): 
    return service.eliminar_un_tipo_de_usuario(db=db, id=id)