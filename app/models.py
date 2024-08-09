from sqlalchemy import Column, Float, Integer, String, Date
from .database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    category = Column(String, index=True)
    type = Column(String, index=True)
