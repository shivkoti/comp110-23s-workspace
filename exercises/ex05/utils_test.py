
__author__: "730556602"

"""Unit tests for only_evens, sub, concat function"""

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens() -> None:
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []

def test_concat() -> None:
    test_list: list[int] = ([], [])
    assert concat(test_list) == []

def test_sub() -> None:
    test_list: (list[int], a: int, b: int) = ([1, 2, 3, 4, 5], 2, 4)
    assert sub(test_list) == [3, 5]
