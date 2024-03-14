import json
from datetime import datetime
from model import Contact
from faker import Faker
import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='Web8 exchange', exchange_type='direct')
channel.queue_declare(queue='web_8_queue', durable=True)
channel.queue_bind(exchange='Web8 exchange', queue='web_8_queue')
fake = Faker()


def create_tasks(nums: int):
    for i in range(nums):
        task = Contact(fullname=fake.name(), email=fake.email()).save()

        channel.basic_publish(
            exchange='Web8 exchange',
            routing_key='web_8_queue',
            body=str(task.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )

    connection.close()


if __name__ == "__main__":
    create_tasks(3)
