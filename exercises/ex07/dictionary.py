"""Dictionary Functions."""

__author__ = "730555602"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Given dict_1, return new dictionary that inverts the keys and values."""
    new_list: dict[str, str] = {}
    for key in dict_1:
        new_list[dict_1[key]] = key
    return new_list    

    
def favorite_color(dict_1: dict[str, str]) -> str:
    """Returns the color that appears most in the dictionary."""
    colors: dict[str, int] = {}
    max_color = []
    max_color_count = 0
    for key in dict_1:
        if dict_1[key] in colors:
            colors[dict_1[key]] += 1
        elif dict_1[key] not in colors:
            colors[dict_1[key]] = 1
    if colors[dict_1[key]] > max_color_count or colors[dict_1[key]] == max_color_count:
        max_color.append(dict_1[key])
        max_color_count == colors[dict_1[key]]
    return max_color[0]


def count(list_1: list[str]) -> dict[str, int]:
    """Counts number of items and list and returns them in dictionary."""
    new_dict = dict[str, int]
    for elem in list:
        if elem not in new_dict:
            new_dict[elem] = 1
        elif elem in new_dict:
            new_dict[elem] += 1
    return new_dict