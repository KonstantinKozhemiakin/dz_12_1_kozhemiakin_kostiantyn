import concurrent.futures
import time
import os

NUM = 600
COUNT = 5


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def without_concurrent_futures(func, num, count=1):
    for i in range(count):
        print(func(num))


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


def compare_function(*func, funct="", num=NUM, count=COUNT):
    best_time = time.time()
    best_func = func[0]
    for fun in func:
        time_start = time.time()
        fun(funct, num, count)
        time_prog = time.time() - time_start
        if time_prog < best_time:
            best_time = time_prog
            best_func = fun
        print(time_prog)
        print('----------------------')
    print(f"The fastest function is: {best_func.__name__}, with time: {best_time}")


if __name__ == '__main__':
    compare_function(without_concurrent_futures,
                     thread_pool_executor,
                     process_pool_executor, funct=factorial, num=NUM, count=COUNT)
