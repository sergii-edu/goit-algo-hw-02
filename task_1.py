from time import sleep
from queue import Queue
from random import getrandbits

queue = Queue()

request_n = 0


def random_event():
    return bool(getrandbits(1))


def generate_request():
    global request_n
    if random_event():
        request_n += 1
        print(f"Створено нову заявку №{request_n}")
        queue.put(request_n)


def process_request():
    if not queue.empty():
        if random_event():
            print(f"Заявку №{queue.get()} оброблено успішно")
        else:
            print(f"Обробляємо заявку №{queue.queue[0]}...")
    else:
        print("-- Черга пуста --")


while True:
    sleep(1)
    generate_request()
    process_request()
