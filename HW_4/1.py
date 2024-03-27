import multiprocessing
import threading
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def run_sync(n):
    start_time = time.time()
    for _ in range(10):
        fibonacci(n)
    return time.time() - start_time


def run_threading(n):
    threads = []
    start_time = time.time()
    for _ in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return time.time() - start_time


def run_multiprocessing(n):
    processes = []
    start_time = time.time()
    for _ in range(10):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    return time.time() - start_time


if __name__ == "__main__":
    n = 35

    time_sync = run_sync(n)
    time_threading = run_threading(n)
    time_multiprocessing = run_multiprocessing(n)

    results_text = (
        f"Синхронный запуск: {time_sync:.2f} секунд\n"
        f"Запуск с использованием потоков (threading): {time_threading:.2f} секунд\n"
        f"Запуск с использованием процессов (multiprocessing): {time_multiprocessing:.2f} секунд"
    )

    with open("artifacts/1.txt", "w") as file:
        file.write(results_text)
