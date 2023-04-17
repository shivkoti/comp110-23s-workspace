"""Practice Functions"""


def mimic_letter(my_words:str, letter_idx:int) -> str:
    if len(my_words)>=letter_idx:
        return("Too high of an index")
    else:
        return my_words[letter_idx]
        

