from functools import wraps
from threading import Thread
from time import time
import os

NUM = 100000000


def count(num):
    while num > 0:
        num -= 1


def time_measure(func):
    """
    A decorator that wraps a function, and measures its wall time.
    """
    @wraps(func)
    def internal(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()

        print('{} took {:.2f} seconds'.format(func.__name__, end_time - start_time))
    return internal


@time_measure
def two_calls_sequential():
    count(NUM)
    count(NUM)


@time_measure
def two_parallel_calls():
    t1 = Thread(target=count, args=(NUM,))
    t2 = Thread(target=count, args=(NUM,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


@time_measure
def one_simple_call():
    count(NUM)


def main():
    one_simple_call()
    # two_calls_sequential()
    # two_parallel_calls()


if __name__ == '__main__':
    main()
