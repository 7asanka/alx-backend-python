#!/usr/bin/env python3
"""module for the to_kv function"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is the input string `k`,
    and the second is the square of `v` as a float.

    Args:
        k (str): A string key.
        v (Union[int, float]): A number to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.
    """
    return (k, float(v ** 2))
