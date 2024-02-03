from .shared import *


class Category(Base):
    __tablename__ = 'category'

    id_category = Column(Integer, primary_key=True, autoincrement=True)
    name_category = Column(String, nullable=False)

    products = relationship('Product', back_populates='category')
