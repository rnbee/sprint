from .shared import *


class Basket(Base):
    __tablename__ = 'basket'

    id_basket = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Boolean, default=False)
    id_user = Column(Integer, ForeignKey('user.id_user'))

    user = relationship('User', back_populates='baskets')
    products = relationship('Product', back_populates='baskets')