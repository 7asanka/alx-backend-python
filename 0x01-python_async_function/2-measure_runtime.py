#!/usr/bin/env python3
""" task 2 module """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measures the total execution time for wait_n(n, max_delay) """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
