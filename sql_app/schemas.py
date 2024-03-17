from datetime import datetime

from pydantic import BaseModel

class User(BaseModel):
    user_name: str
    is_activate: bool = False
    email: str
    first_name: str
    last_name: str
    phone_number: str

class UserInDB(User):
    hashed_password: str

# models for basket products table 
class BasketProductsBase(BaseModel):
    quantity: int
    product_name: str 

class BasketProductsCreate(BasketProductsBase):
    id_product: int
    price: int
    id_basket: int | None
    id_user: int

class BasketProducts(BasketProductsBase):
    id_basket_products: int
    id_product: int

    class Config:
        from_attributes = True


# models for basket table 
class BasketBase(BaseModel):
    total_amount: int
    total_quantity: int
    status: str

class BasketCreate(BasketBase):
    pass

class Basket(BasketBase):
    id_basket: int
    created_at: datetime
    updated_at: datetime
    products: list[BasketProducts] = []

    class Config:
        from_attributes = True


# models for user
class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: int

class User(UserBase):
    phone_number: str
    registration_date: datetime
    is_acitve: bool
    baskets: list[Basket] = []

    class Config:
        from_attributes = True


# models for product
class ProductBase(BaseModel):
    product_name: str

class ProductAdd(ProductBase):
    id_product: int
    quantity: int
    price: int


class Product(ProductBase):
    quantity: int
    id_product: int
    price: int
    description: str
    id_distributor: int
    id_category: int

    class Config:
        from_attributes = True

