import pika
import os
import logging

# Configurar el registro de eventos
logging.basicConfig(level=logging.INFO)

# Obtener las credenciales de las variables de entorno
user = os.getenv('RABBITMQ_USER')
password = os.getenv('RABBITMQ_PASS')

# Conectarse a RabbitMQ con las credenciales proporcionadas por las variables de entorno
credentials = pika.PlainCredentials(user, password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Vincular la cola 'prueba' al intercambio 'logs'
channel.queue_bind(exchange='logs', queue='prueba')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    logging.info(f"Mensaje recibido: {body}")

channel.basic_consume(queue='prueba', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
