import json
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from pydantic import BaseModel

from sqlalchemy.orm import Session

from schemas import User, UserInDB, BasketProductsCreate
from database import SessionLocal, engine
import crud, publisher


fake_users_db = {
    "johndoe": {
        "user_name": "johndoe",
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "phone_number": "9345234253",
        "hashed_password": "fakehashedsecret",
        "is_active": False,
    },
    "alice": {
        "user_name": "alice",
        "first_name": "Alice",
        "last_name": "Garcie",
        "phone_number": "9385862343",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "is_active": True,
    },
}

# session = Session(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

def fake_hash_password(password: str):
    return 'fakehashed' + password

def get_user(db, user_name: str):
    if user_name in db:
        user_dict = db[user_name]
        return UserInDB(**user_dict)

def fake_decode_token(token):
   user = get_user(fake_users_db, token)
   return user

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={'WWW-Authenticate': 'Bearer'}
        )
    return user

def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.is_activate:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")                                                        
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict =  fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not user.hashed_password == hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {'access_token': user.user_name, 'token_type': 'bearer'}

@app.get("/users/me")
def read_user_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

@app.post("/users/{user_id}")
def add_product_to_user_basket(user_id: int, product_name: str, 
                               product_quantity: int, db: Session = Depends(get_db)):
    
    # validation_products return body {id_prod, product_name, quantity}
    product = crud.validation_products(db=db, product_name=product_name, 
                             product_quantity=product_quantity)     
    if product is None:
        raise HTTPException(status_code=404, detail=f"{product_name} Not Found or quantity is more than...")
    
    # we are need to get basket or create it (if basket doesn't exist)
    # in order to adding product inside it
    id_basket = crud.get_id_basket(db, user_id)   
    basket_products = BasketProductsCreate(**product, id_basket=id_basket, id_user=user_id)
    
    to_json = basket_products.model_dump_json()
    # send product to the queue in order to adding to data base
    publisher.send_message(operation='adding_to_cart', message=to_json)












# order_publisher = OrderPublisher()

# # Base.metadata.create_all(engine)

# # class Order(BaseModel):
# #     product: str 
# #     quantity: int

# # external_data = {
# #     'user_name': 'Matew',
# #     'product': 'chair',
# #     'quantity': 2
# # }
# # 
# # order = Order(**external_data)

# def order_validation(user_name: str, product_name: str, quantity: int) -> bool:
#     user_obj = session.query(user.User).filter(user.User.first_name == user_name).first()
#     if not user_obj:
#         print(f'{user_name} is not registered.')
#         return False
    
#     product_obj = session.query(product.Product).filter(product.Product.product_name == product_name).first()
#     if not product_obj:
#         print(f"{product_name} doesn't exist.")
#         return False
    
#     product_quantity = session.query(product.Product).filter(product.Product.quantity >= quantity).first()
#     if not product_quantity:
#         print(f"count of products must be at most {product.Product.quantity}.")
#         return False
    
#     return True

# @app.get("/get_orders/{user_name}")
# def get_order(user_name: str):
#     # в базу данных отправляется запрос на получение 
#     # данных по конкретному user
#     # и предовставляет полный список товаров находящийся 
#     # в корзине 
#     pass

# @app.post("/orders/{user_name}")
# def create_order(user_name: str, product_name: str, quantity:int):
#     # pdb.set_trace()
#     if not order_validation(user_name, product_name, quantity):
#         print("order failed.")

#     message_body = {
#         'user_name': user_name,
#         'product': product_name,
#         'quantity': quantity
#     }

#     message_body = json.dumps(message_body)
#     order_publisher.send_message_to_queue(body=message_body, routing_key='add_to_db')

