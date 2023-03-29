"""Dictionary Functions."""

__author__ = "730555602"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Given dict_1, return new dictionary that inverts the keys and values."""
    new_dict: dict[str, str] = {}
    for key in dict_1:
        if dict_1[key] in new_dict:
            raise KeyError("This is wrong.")
        new_dict[dict_1[key]] = key
    return new_dict    

    
def favorite_color(dict_1: dict[str, str]) -> str:
    """Returns the color that appears most in the dictionary."""
    colors: dict[str, int] = {}
    max_color = ""
    max_color_count = 0
    for key in dict_1:
        if dict_1[key] in colors:
            colors[dict_1[key]] += 1
        else:
            colors[dict_1[key]] = 1
    for key in colors:
        if colors[key] > max_color_count:
            max_color = key
            max_color_count = colors[key]
    return max_color


def count(list_1: list[str]) -> dict[str, int]:
    """Counts number of items and list and returns them in dictionary."""
    new_dict = {}
    for elem in list_1:
        if elem not in new_dict:
            new_dict[elem] = 1
        elif elem in new_dict:
            new_dict[elem] += 1
    return new_dict