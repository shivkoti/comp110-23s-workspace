"""`list` Utility Functions."""
___author___: "730556602"


def all(my_list: list[int], number: int) -> bool:  
    """Indicates if all numbers in list match indicated number."""
    counter: int = 0
    if len(my_list) == 0:
        return False
    while counter < len(my_list):
        if number != my_list[counter]:
            return False
        counter = counter + 1
        
    return True
       
 
def max(list_0: list[int]) -> int:
    """Returns the largest number in the list."""
    if len(list_0) == 0:
        raise ValueError("max() arg is an empty List")
    max_number = list_0[0]
    counter: int = 0
    while counter < len(list_0):
        if list_0[counter] > max_number:
            max_number = list_0[counter]
        counter = counter + 1
    return max_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """True if lists are equal, False otherwise."""
    x: int = 0
    if len(list_1) != len(list_2):
        return False
    while x < len(list_1) and x < len(list_2):
        if list_1[x] != list_2[x]:
            return False
        x = x + 1
    return True
