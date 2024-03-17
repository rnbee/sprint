from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .basket import Basket

from .shared import *


class BasketProducts(Base): #NEW
    __tablename__ = 'basket_products'

    id_basket_products = Column(Integer, primary_key=True, autoincrement=True)
    # id_basket = Column(Integer, ForeignKey('basket.id_basket'))
    id_product = Column(Integer, ForeignKey('product.id_product'))
    quantity = Column(Integer, default=0, nullable=False)
    product_name = Column(String, nullable=False)

    # owner = relationship("Basket", uselist=True)
    