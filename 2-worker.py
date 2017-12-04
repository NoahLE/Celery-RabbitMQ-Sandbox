import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

print(" [*] Waiting for messages. To exit press Ctrl + C")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # A useful command for checking queues if ack is forgotten:
    # rabbitmqctl.bat list_queues name messages_ready messages_unacknowledged


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='hello')

channel.start_consuming()
