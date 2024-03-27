import multiprocessing
import threading
import time
from codecs import encode


def process_a_func(queue, conn):
    while True:
        if not queue.empty():
            msg = queue.get().lower()
            conn.send(msg)
            time.sleep(5)


def process_b_func(conn_from_a, conn_to_main):
    while True:
        msg = conn_from_a.recv()
        encoded_msg = encode(msg, "rot_13")
        conn_to_main.send(encoded_msg)


def user_input_handler(queue):
    while True:
        msg = input()
        if msg.lower() == "exit":
            break
        print(f"{time.strftime('%H:%M:%S')}: Главный процесс (ввод): {msg}")
        queue.put(msg)
        time.sleep(0.5)


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    parent_conn_to_b, child_conn_to_b = multiprocessing.Pipe()
    parent_conn_from_b, child_conn_from_b = multiprocessing.Pipe()

    process_a = multiprocessing.Process(target=process_a_func, args=(queue, child_conn_to_b))
    process_b = multiprocessing.Process(target=process_b_func, args=(parent_conn_to_b, child_conn_from_b))

    process_a.start()
    process_b.start()

    input_thread = threading.Thread(target=user_input_handler, args=(queue,))
    input_thread.start()

    try:
        while input_thread.is_alive():
            if parent_conn_from_b.poll():
                encoded_msg = parent_conn_from_b.recv()
                print(f"{time.strftime('%H:%M:%S')}: Главный процесс (вывод ROT13): {encoded_msg}")
            time.sleep(0.1)
    finally:
        process_a.terminate()
        process_b.terminate()
