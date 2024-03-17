from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .basket import Basket

from .shared import *

class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, unique=True, nullable=False) # NEW
    email = Column(String, unique=True, nullable=False)
    is_activate = Column(Boolean, default=False)
    first_name = Column(String(length=20), nullable=False)
    last_name = Column(String(length=20), nullable=False)
    phone_number = Column(String(length=18), nullable=False)
    hashed_password = Column(String) # NEW
    registration_date = Column(DateTime(timezone=True), nullable=False, default=datetime.now())

    # baskets = relationship("Basket", back_populates="owner")   # NEW