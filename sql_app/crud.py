import json 

from sqlalchemy.orm import Session

from models import basket, product, \
    user as user_mdb, basket_products

import schemas


def get_user(db: Session, id_user: int):
    return db.query(user_mdb.User).\
        filter(user_mdb.User.id_user == id_user).\
            first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_mdb.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + 'notrellyhashed'
    db_user = user_mdb.User(email=user.email, hashed_password = fake_hashed_password,
                            first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def add_product_to_cart(db: Session, product: product.Product) -> basket_products.BasketProducts:
    db_basket_products = product
    db.add(db_basket_products)
    db.commit()
    db.refresh(db_basket_products)

def validation_products(db: Session, product_name: str,
                        product_quantity: int) -> schemas.ProductAdd | None:
    
    product_data = db.query(product.Product).\
        filter(product.Product.product_name == product_name, 
               product.Product.quantity >= product_quantity).first()
    
    if product_data is None: 
        return None

    return {"id_product": product_data.id_product,
            "product_name": product_data.product_name,
            "quantity": product_data.quantity,
            "price": product_data.price
            } 

def create_basket(db: Session, user_id: int, 
                  bakset_poroducts_id: int) -> basket.Basket:
      
    db.add(basket.Basket(id_user=user_id, 
                         id_basket_products=bakset_poroducts_id))
    db.commit()


def get_id_basket(db: Session, user_id: int) -> int | None: 
    db_basket = db.query(basket.Basket).\
        filter(basket.Basket.id_user == user_id, basket.Basket.status == 'empty').first()
    
    if db_basket is None:
        return None

    return db_basket.id_basket

