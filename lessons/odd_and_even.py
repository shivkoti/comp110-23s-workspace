"""Odd and Even Pratice for Quiz"""

def odd_and_even(old_list = list[int]) -> list[int]:
    """Return a new list containing the elements of the input list that are odd and have an even index"""
    new_list = []
    i = 0
    while i < len(old_list):
        if i %2 == 0 and old_list[i] %2 == 1:
                new_list.append(old_list[i])
        i += 2
    return new_list

     
        


