import concurrent.futures
import time
import os

NUM = 200
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


def compare_function(*func, funct = "", num = NUM, count = COUNT):
    best_time = 9999999999
    best_func = func[0]
    for fun in func:
        time_start = time.time()
        fun(funct, num, count)
        time_prog = time.time() - time_start
        if time_prog < best_time:
            best_time = time_prog
            best_func = fun
        print('----------------------')
        print(time_prog)
    print(best_func, best_time)

    # if time_process > time_thread:
    #     print("ThreadPoolExecutor is better")
    # else:
    #     print("ProcessPoolExecutor is better")
    # min_time = 0
    # min_time_func = args[0]
    # time_start = time.time()
    # for i in args:
    #     print("ff")
    # time_finish = time.time() - time_start
    # print(time_finish)



if __name__ == '__main__':
    compare_function(without_concurrent_futures,
                     thread_pool_executor,
                     process_pool_executor,funct=factorial, num=NUM, count=COUNT)
