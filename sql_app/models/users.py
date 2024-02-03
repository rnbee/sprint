from .shared import *


class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    is_activate = Column(Boolean, default=True)
    first_name = Column(String(length=20), nullable=False)
    last_name = Column(String(length=20), nullable=False)
    phone_number = Column(String(length=18), nullable=False)
    registration_date = Column(DateTime(timezone=True), nullable=False)

    baskets = relationship('Basket', back_populates='User')
    