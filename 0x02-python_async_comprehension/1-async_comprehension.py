#!/usr/bin/env python3
'''collect 10 random numbers using an async comprehensing over async_generator'''

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Return 10 random numbers in async_generator. '''
    return [value async for value in async_generator()]
