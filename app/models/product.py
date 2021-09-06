from sqlalchemy import Column, Integer, String, Float, DateTime, text
from sqlalchemy.sql import func
import datetime

from app.database.base_class import Base


class Product(Base):
    # TODO: Use uuid, add createdAt, updatedAt
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    # TODO: Using server updated time (from SqlAlchemy) not working
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    # updated_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.datetime.now)