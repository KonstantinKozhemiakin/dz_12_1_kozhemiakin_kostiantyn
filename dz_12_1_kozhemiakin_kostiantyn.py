import concurrent.futures
import time
import os

NUM = 20
COUNT = 5


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def without_concurrent_futures(*func, count=1):
    for i in range(count):
        print(*func)


def thread_pool_executor(func, num, count=1):
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        for i in range(count):
            futures.append(executor.submit(func, num))
    for f in futures:
        print(f.result())


def process_pool_executor(func, num, count=1):
    futures = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        for i in range(count):
            futures.append(executor.submit(func, num))
    for f in futures:
        print(f.result())


def compare_function(*args):
    min_time = 0
    min_time_func = args[0]
    print(args)
    time_start = time.time()
    for i in args:
        print("ff")
    time_finish = time.time() - time_start
    print(time_finish)


if __name__ == '__main__':
    compare_function(without_concurrent_futures(factorial(NUM), count=COUNT),
                     thread_pool_executor(factorial, NUM, COUNT),
                     process_pool_executor(factorial, NUM, COUNT))
