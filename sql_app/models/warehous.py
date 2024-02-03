from .shared import *


class Warehouse(Base):
    __tablename__ = 'warehouse'

    id_warehouse = Column(Integer, primary_key=True, autoincrement=True)
    id_distributor = Column(Integer, ForeignKey('distributor.id_distributor'))
    location = Column(String(length=50), nullable=False)
    amount = Column(Integer, nullable=False)

    distributor = relationship('Distributor', back_populates='warehouses')
    product = relationship('Product', back_populates='warehouses')