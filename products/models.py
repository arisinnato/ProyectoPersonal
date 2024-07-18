from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    image_url = Column(String)
    carts = relationship('Cart', back_populates='product')
    likes = relationship('Like', back_populates='product')
    detailcompra = relationship('PurchaseDetail', back_populates='product')
