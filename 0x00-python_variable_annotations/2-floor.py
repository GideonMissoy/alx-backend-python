#!/usr/bin/env python3
''' type-annotated function floor which takes a float n'''


def floor(n: float) -> int:
    '''returns the floor of the float'''
    return int(n) if n >= 0 else int(n) - 1