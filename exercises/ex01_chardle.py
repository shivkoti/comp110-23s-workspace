"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730556602"


if letter == word[2]:
    print(letter + " found at index 2")
    number = number + 1
if letter == word[3]:
    print(letter + " found at index 3")
    number = number + 1 
if letter == word[4]:
    print(letter + " found at index 4")
    number = number + 1

    if number == 1:
        print(str(number) + " instance of " + letter + " found in " + word)
    if number > 1:
        print(str(number) + " instances of " + letter + " found in " + word)
    else:
        if number == 0:
            print("No instances of " + letter + " found in " + word)
    print("Error: Word must contain 5 characters")
    SystemExit  




    if number == 1:
        print(str(number) + " instance oword: str = input("Enter a 5-character word: ")
else:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        SystemExit
    number: int = 0
if len(word) == 5:
    print("Searching for " + letter + " in " + word)
if letter == word[0]:
    print(letter + " found at index 0")
    number = number + 1
if letter == word[1]:
    print(letter + " found at index 1") 
    number = number + 1f " + letter + " found in " + word)
    if number > 1:
        print(str(number) + " instances of " + letter + " found in " + word)
    else:
        if number == 0:
            print("No instances of " + letter + " found in " + word)