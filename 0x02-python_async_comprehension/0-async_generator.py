#!/usr/bin/env python3
'''
Write a coroutine called async_generator that takes no arguments.
'''

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''wait 1 second, then yield a random number between 0 and 10'''
    for y in range(10):
        await sleep(1)
        yield 10 * random()
