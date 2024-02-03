from .shared import *


class Distributor(Base):
    __tablename__ = 'distributor'

    id_distributor = Column(Integer, primary_key=True, autoincrement=True)
    adress = Column(String(length=30), nullable=False)
    email = Column(String(length=30), nullable=False)
    title = Column(String(length=30), nullable=False)
    phone_number = Column(String(length=18), nullable=False)
    id_shop = Column(Integer, ForeignKey('shop.id_shop'))
    id_warehouse = Column(Integer, ForeignKey('warehouse.id_warehouse'))

    warehouses = relationship('Warehouse', back_populates='disttributor')
    shops = relationship('Shop', back_populates='distributor')
    product = relationship('Product', back_populates='distributor')