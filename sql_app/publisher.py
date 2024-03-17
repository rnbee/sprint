import pika

def send_message(operation, message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.exchange_declare(exchange='direct', exchange_type='direct')
    
    channel.basic_publish(exchange='direct', routing_key=operation, body=message)
    print(f" [x] Sent {operation}:{message}")
    connection.close()
