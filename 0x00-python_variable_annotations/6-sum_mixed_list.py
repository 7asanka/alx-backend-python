#!/usr/bin/env python3
"""module for the sum_mixed_list function"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of int and float values.

    Returns:
        float: The sum of all elements in the list as a float.
    """
    return float(sum(mxd_lst))
