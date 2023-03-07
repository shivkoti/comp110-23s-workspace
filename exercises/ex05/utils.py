
__author__: "730556602"

def only_evens(xs: list[int]) -> list[int]:
    """Returns even numbers in list"""
    even_numbers: list[int] = []
    for idx in xs:
        if  idx %2 == 0:
            even_numbers.append(idx)
    return even_numbers

def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Concatenates two lists of ints and returns the resulting list."""
    return list1 + list2

def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """Returns a List which is a subset of the given list"""
    new_list: list[int] = []
    if a < 0:
        a = 0
    if b >= len(a_list):
        b = len(a_list) - 1
    if len(a_list) == 0 or a >= len(a_list): 
        return new_list
    for i in range(a, b):
        new_list.append(a_list[i])
    return new_list