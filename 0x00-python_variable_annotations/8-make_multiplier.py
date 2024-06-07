#!/usr/bin/env python3
'''
type-annotated function make_multiplier that takes a float multiplier
'''

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function that multiplies a float by multiplier'''
    return lambda y: y * multiplier