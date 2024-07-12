from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class PurchaseDetail(Base):
    __tablename__ = 'purchase_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    purchase_id = Column(Integer, ForeignKey('purchases.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    purchase = relationship('Purchase', back_populates='purchase_details')
    product = relationship('Product', back_populates='purchase_details')
