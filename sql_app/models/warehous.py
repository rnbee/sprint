from .shared import *


class Warehouse(Base):
    __tablename__ = 'warehouse'

    id_warehouse = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String(length=50), nullable=False)

    distributor = relationship('Distributor', back_populates='warehouses')