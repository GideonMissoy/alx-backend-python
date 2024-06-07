#!/usr/bin/env python3
'''
type-annotated function sum_list which takes a list input_list of floats
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns their sum as a float.'''
    return sum(input_list)