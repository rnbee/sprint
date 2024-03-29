from .shared import *


class Product(Base):
    __tablename__ = 'product'

    id_product = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(length=50), nullable=False)
    price = Column(Numeric(precision=10, scale=2), index=True)
    # img = Column(LargeBinary, nullable=True)
    description = Column(String(length=50), nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
    # id_distributor = Column(Integer, ForeignKey('distributor.id_distributor'))
    # id_category = Column(Integer, ForeignKey('category.id_category'))

