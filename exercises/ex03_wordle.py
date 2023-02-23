__author__ = "730556602"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(secret_word: str, letter: str) -> bool:
    """If letter is found at any index of secret word, return True"""
    assert len(letter) == 1
    counter: int = 0
    while int(counter) < len(secret_word):
        if secret_word[counter] == letter:
            return True
        counter = counter + 1
    return False

def emojified(guess: str, secret_word: str) -> str:
    """If letter of guess is found in the index of secret word, return yellow or green emoji"""
    assert len(guess) == len(secret_word)
    counter: int = 0
    emojis: str = ""
    while int(counter) < len(secret_word):
        if secret_word[counter] == guess[counter]:
            emojis = emojis + GREEN_BOX
        else:
            if contains_char(secret_word, guess[counter]) == True:
                emojis = emojis + YELLOW_BOX
            else:
                emojis = emojis + WHITE_BOX
        counter = counter + 1
    return emojis

def input_guess(expected_length: int) -> str:
    guess: str = str(input(f"Enter a {expected_length} character word: "))
    while expected_length != len(guess):
        guess: str = str(input(f"That wasn't {expected_length} chars! Try again: "))
    if expected_length == len(guess):
        return(guess)

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret_word: str = "codes"
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        answer: str = input_guess(5)
        print(emojified(answer, "codes"))
        if turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
        if answer == "codes":
            print(f"You won in {turn}/6 turns!")
            turn = 7
    turn = turn + 1
    
if __name__ == "__main__":
    main()