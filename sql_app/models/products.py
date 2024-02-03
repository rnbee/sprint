from .shared import *


class Product(Base):
    __tablename__ = 'product'

    id_product = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, default=0)
    title = Column(String(length=50), nullable=False)
    id_distributor = Column(Integer, ForeignKey('distributor.id_distributor'))
    id_category = Column(Integer, ForeignKey('category.id_category'))
    price = Column(Numeric(precision=10, scale=2), index=True)
    img = Column(LargeBinary, nullable=True)

    category = relationship('Category', back_populates='products')
    distributors = relationship('Distributor', back_populates='product')