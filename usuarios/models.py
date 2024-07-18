from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import tipos_usuario.models as tipos_usuario

class Usuario(Base): 
    __tablename__  = "usuarios"
    
    nombres = Column(String, index=True)
    apellidos = Column(String, index=True)
    correo = Column(String, index=True)
    contraseña = Column(String, index=True)
    tipo_id = Column(Integer, ForeignKey(tipos_usuario.Tipo_Usuario.id))

    tipo = relationship('Tipo_Usuario', back_populates='usuarios')
    productos = relationship('Product', back_populates='usuarios')
    compras = relationship('Compra', back_populates='cliente')


