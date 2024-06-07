#!/usr/bin/env python3
'''
Augment the following code with the correct duck-typed annotations:
'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''The types of the elements of the input are not know'''
    if lst:
        return lst[0]
    else:
        return None