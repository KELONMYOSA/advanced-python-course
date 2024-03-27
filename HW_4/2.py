import logging
import math
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def integrate_part(f, a, b, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, executor, n_jobs=1, n_iter=10000000):
    step = (b - a) / n_jobs
    futures = []

    with executor(max_workers=n_jobs) as e:
        for i in range(n_jobs):
            part_a = a + i * step
            part_b = a + (i + 1) * step
            futures.append(e.submit(integrate_part, f, part_a, part_b, n_iter=n_iter // n_jobs))
            logging.info(f"Задача {i + 1} запущена: от {part_a} до {part_b}")

    return sum([future.result() for future in futures])


if __name__ == "__main__":
    logging.basicConfig(filename="artifacts/2.txt", level=logging.INFO, format="%(asctime)s %(message)s")

    cpu_num = 8
    times_thread = []
    times_process = []

    for i, executor in enumerate((ThreadPoolExecutor, ProcessPoolExecutor)):
        for n_jobs in range(1, cpu_num * 2 + 1):
            if i == 0:
                logging.info(f"--- Старт - ThreadPoolExecutor: cpu_num = {n_jobs} ---")
            else:
                logging.info(f"--- Старт - ProcessPoolExecutor: cpu_num = {n_jobs} ---")

            start_time = time.time()
            result = integrate(math.cos, 0, math.pi / 2, executor, n_jobs=n_jobs)
            end_time = time.time()

            if i == 0:
                logging.info(
                    f"--- Финиш - ThreadPoolExecutor: cpu_num = {n_jobs}, время: {end_time - start_time:.3f} секунд ---"
                )
            else:
                logging.info(
                    f"--- Финиш - ProcessPoolExecutor: cpu_num = {n_jobs}, "
                    f"время: {end_time - start_time:.3f} секунд ---"
                )

            logging.info(f"Результат: {result}")
