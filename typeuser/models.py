from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class TypeUser(Base):
    __tablename__ = 'typeuser'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    
    users = relationship('User', secondary='typeuser', back_populates='type_user')
