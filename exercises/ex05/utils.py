
__author__: "730556602"

def only_evens(xs: list[int]) -> list[int]:
    """Returns even numbers in list"""
    for idx in xs:
        if  idx %2 == 0:
            xs.append(idx)
        else:
            return xs.append([])
    return xs  

def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Concatenates two lists of ints and returns the resulting list."""
    return list1 + list2

def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """Returns a List which is a subset of the given list"""
    if a < 0:
        a = 0
    if b >= len(a_list):
        b = len(a_list)  
    if len(a_list) == 0 or a >= len(a_list): 
        return a_list()
    for list in range(a_list[0], len(a_list)):
        return [a_list[a], a_list[b]]