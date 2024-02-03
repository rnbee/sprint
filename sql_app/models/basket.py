from .shared import *


class Basket(Base):
    __tablename__ = 'basket'

    id_basket = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(length=20), nullable=False)
    status = Column(Boolean, default=False)
    id_user = Column(Integer, ForeignKey('user.id_user'))

    user = relationship('User', back_populates='Baskets')