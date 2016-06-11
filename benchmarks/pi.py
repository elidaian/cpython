from functools import wraps
from threading import Thread
from time import time
import os

NUM = 40000000

def pi(iterations):
    res = 0.0
    for k in range(iterations):
        if (k % 2) == 0:
            res += 4.0 / (2.0 * k + 1.0)
        else:
            res -= 4.0 / (2.0 * k + 1.0)
    return res


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
    pi(NUM)
    pi(NUM)


@time_measure
def two_parallel_calls():
    t1 = Thread(target=pi, args=(NUM,))
    t2 = Thread(target=pi, args=(NUM,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


@time_measure
def one_simple_call():
    pi(NUM)


def main():
    one_simple_call()
    # two_calls_sequential()
    # two_parallel_calls()


if __name__ == '__main__':
    main()
