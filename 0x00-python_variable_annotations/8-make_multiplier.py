#!/usr/bin/env python3
"""module for the make_multiplier function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies
        its input by `multiplier`.
    """
    def multiplier_fn(x: float) -> float:
        return x * multiplier

    return multiplier_fn
