__author__: "730556602"
"""Challenge question"""


def zip(list_a: list[str], list_b: list[int]) -> dict[str, int]:
    """list_a = keys, list_b = values"""
    dictionary: dict[str, int] = {}
    if len(list_a) != len(list_b):
     return dictionary 
    if len(list_a) == 0 or len(list_b) == 0:
       return dictionary
    for idx in range(len(list_a)):
        dictionary[list_a[idx]] = list_b[idx]
    return dictionary
