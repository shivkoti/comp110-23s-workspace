"""One-Shot Wordle"""

__author__ = "730556602"

word: str = "python"
guess: str = str(input("What is your 6-letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emojis: str = ""
counter: int = 0
characterexist: bool = False
alternatecounter: int = 0

while len(guess) != len(word):
    guess = str(input("That was not 6 letters! Try again: "))


if len(guess) == len(word):
        while counter < len(word):
            if guess[counter] == word[counter]:
                emojis = emojis + GREEN_BOX
            else:
                characterexist = False
                alternatecounter = 0
                while characterexist == False and (alternatecounter < len(word)):
                    if word[alternatecounter] == guess[counter]:
                        characterexist = True
                    else:
                        alternatecounter = alternatecounter + 1
                if characterexist == True:
                    emojis = emojis + YELLOW_BOX
                else:
                    emojis = emojis + WHITE_BOX
                    counter = counter + 1

print(emojis)

if guess == word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")

