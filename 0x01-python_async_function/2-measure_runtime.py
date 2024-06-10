#!/usr/bin/env python3
'''
Creates a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay)
'''

from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''returns total_time / n. Your function should return a float.'''
    time_0 = time()
    run(wait_n(n, max_delay))
    time_1 = time()
    total_time = time_1 - time_0
    return total_time / n