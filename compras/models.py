from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Purchase(Base):
    __tablename__ = 'purchases'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    total = Column(Float, nullable=False)
    user = relationship('User', back_populates='purchases')
    purchase_details = relationship('PurchaseDetail', back_populates='purchase')
