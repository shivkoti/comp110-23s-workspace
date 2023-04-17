"""Short_words function for Quiz."""

___author___ = 730555602


def short_words(word_list = list[str]) -> list[str]:
    """Create a list of words shorter than 5 letters."""
    new_list = []
    for elem in word_list:
        if len(elem) < 5:
            new_list.append(elem)
        else:
            print(f"{elem} is too long!")
    return new_list
            
