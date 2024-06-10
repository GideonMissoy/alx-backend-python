#!/usr/bin/env python3
'''
Writes an asynchronous coroutine that takes in an integer argument (max_delay,
 with a default value of 10) that waits for a random delay between 0 and max_delay
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits till max_delay seconds then return length of delay'''
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay