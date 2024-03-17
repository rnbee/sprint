from typing import TYPE_CHECKING
from .basket_products import BasketProducts

if TYPE_CHECKING:
    from .user import User

from models.shared import *


class Basket(Base):
    __tablename__ = 'basket'

    id_basket = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, default='empty')
    id_user = Column(Integer, ForeignKey('user.id_user'))
    total_quantity = Column(Integer, default=0) # NEW
    total_amount = Column(Integer, default=0) # NEW
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now()) # NEW
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.now()) # NEW
    id_basket_products = Column(Integer, ForeignKey('basket_products.id_basket_products')) # NEW

    # owner = relationship("User", back_populates="baskets") # NEW
    # basket_products = relationship("BasketProducts")
