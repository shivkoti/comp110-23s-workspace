"""Value Exists Practice for Quiz"""

def value_exists(old_dict: dict[str, int], x: int) -> bool:
    """Returns True if int exists as a value in dictionary"""
    if x in old_dict:
        return True
    elif x not in old_dict:
        return False
       
test_dict: dict[str ,int] = {"a": 2 , "b": 4 , "c": 7 , "d": 1}
test_val: int = 4
value_exists(test_dict, test_val)