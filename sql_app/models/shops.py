from .shared import *


class Shop(Base):
    __tablename__ = 'shop'

    id_shop = Column(Integer, primary_key=True, autoincrement=True)
    shop_name = Column(String(length=20), nullable=False)

    distributors = relationship('Distributor', back_populates='shops') 
