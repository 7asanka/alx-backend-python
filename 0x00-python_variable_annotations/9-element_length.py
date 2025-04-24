#!/usr/bin/env python3
"""module to modify annotiations"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    each containing the element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence-like
        elements (e.g., str, list, tuple).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples (element, length).
    """
    return [(i, len(i)) for i in lst]
