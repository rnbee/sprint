import sys, json, pdb

import pika 
from sqlalchemy.exc import IntegrityError

from database import SessionLocal
from models import basket_products
import schemas, crud


db = SessionLocal() # закроется содидение или оно останется открытым?

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='direct', exchange_type='direct')

result = channel.queue_declare('', exclusive=True) # из-за параметра exclusive мы не сможем запустить копию этого скрипта, так ли это?
queue_name = result.method.queue
print(queue_name)
operation = sys.argv[1]
if not operation:
    sys.stderr.write("Usage: %s [operation]\n" % sys.argv[0])
    sys.exit(1)

channel.queue_bind(queue=queue_name, exchange='direct', routing_key=operation)

print(" [x] Wating for product. To exit press CTRL+C")

def add_product(ch, method, prst, body):

    body = json.loads(body.decode('utf-8'))
    id_basket = body.pop('id_basket')
    id_user = body.pop('id_user')
    price = body.pop('price')
    
    try:    
        db_basket_products = crud.add_product_to_cart(db, basket_products.BasketProducts(**body))

        if id_basket is None:
            crud.create_basket(db, id_user, db_basket_products.id_basket_products)
    
    except IntegrityError as e:
        print(f"{e} error has occured") 
    
    finally:
        ch.basik_ack(delivery_tag=method.delivery_tag)
        


channel.basic_consume(queue=queue_name, on_message_callback=add_product, auto_ack=False)

channel.start_consuming()