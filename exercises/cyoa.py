"""Personality quiz: Choose your own adventure game."""

__author__ = "730556602"

smirk_emoji: str = "\U0001F60F"
sad_face_emoji: str = "\U0001F614"
lizard_emoji: str = "\U0001F40D"
whale_emoji: str = "\U0001F433"
cheetah_emoji: str = "\U0001F406"
player: str = ""
points: int = 0


def greet() -> None:
    """Greeting for quiz."""
    global player
    player = input("Player, what is your name?: ")
    print(f"Hello {player}, welcome to the adventure game!")


def main() -> None:
    """Main function for personality quizzes."""
    global points
    print(f"You currently have {points} game points!")
    greet()
    while True:
        personality_game: str = input("Do you want to take a personality quiz, yes or no?: ")
        if personality_game == "yes":
            points = animal_quiz(points)
        if personality_game == "no":
            number_game: str = input("Do you want to play a game to update your points instead? yes or no?: ")
            if number_game == "yes":
                update_points()
            elif number_game == "no":
                goodbye_message()
            while number_game not in ["yes", "no"]:
                number_game = input("Sorry, that is not an option, choose again! Yes or no?: ")
        while personality_game not in ["yes", "no"]:
            personality_game = input("Sorry, that is not an option, choose again! Yes or no?: ")


def animal_quiz(points: int) -> int:
    """Personaility quiz about animals."""
    print("Hello! Welcome to the animal personality quiz!")
    print("Answer the following questions with 'A', 'B', or 'C' to find out which animal you are most like!")
    questions_animal: list[str] = ["What is your favorite color? A-Red B-Blue C-Green ", "What is your favorite food? A-Meat B-Vegetables C-Fruits", "What is your favorite activity? A-Running B-Swimming C-Climbing"]
    response_points = 0
    for i in range(len(questions_animal)):
        current_question = questions_animal[i]
        print(current_question)
        response_for_animal = input("Enter your answer: ")
        while response_for_animal not in ["A", "B", "C"]:
            response_for_animal = input("Invalid answer, please enter 'A', 'B', or 'C': ")
        if response_for_animal == "A":
            response_points += 1
        if response_for_animal == "B":
            response_points += 2
        if response_for_animal == "C":
            response_points += 3
    if response_points >= 3 and response_points < 5:
        print(f"Yay! You are most like a cheetah{cheetah_emoji}!")
    elif response_points >= 5 and response_points < 7:
        print(f"Yay you are most like a whale!{whale_emoji}")
    elif response_points >= 7 and response_points <= 9:
        print(f"Yay! You are most like a lizard!{lizard_emoji}")
    points += 2
    print(f"Congrats! For taking this quiz, you now have {points} game points")
    main_screen = input("Would you like to return to the main screen? Yes or no: ")
    while True:
        if main_screen == "yes":
            main()
            return points
        elif main_screen == "no":
            goodbye_message()
            return points
        while main_screen not in ["yes", "no"]:
            main_screen = input("Sorry, that is not an option, choose again! Yes or no?: ")
        

def update_points() -> None:
    """Update points game."""
    from random import randint
    global player, points
    print(f"Hello {player}, you currently have {points}! You now have the opportunity to earn or lose some points!")
    print("You can enter 'A' to add points, but the system has a mind of its own and won't always follow directions.")
    print("Sometimes the system will give you points if you press 'A', but it can also subtract points! Beware and test your luck with this game!")
    choice = input(f"Choose 'A' or enter 'X' to return to main{smirk_emoji}: ")
    if choice != "A" and choice != "X":
        choice = input("Sorry, that was not a valid option, choose again!")
    while choice == "A":
        random_number = randint(-5, 5)
        points += random_number
        print(f"You gained {random_number} points. Your total score is now {points}")
        choice = input("Choose 'A' or enter 'X' to return to main: ")
    if choice == "X":
        print(f"You have {points} game points.")
        main()
    main_screen = input("Would you like to return to the main screen? Yes or no: ")
    while True:
        if main_screen == "yes":
            main()
        elif main_screen == "no":
            goodbye_message()
        while main_screen not in ["yes", "no"]:
            main_screen = input("Sorry, that is not an option, choose again! Yes or no?: ")


def goodbye_message() -> None:
    """Goodbye message for game."""
    print(f"Sorry to see you go{sad_face_emoji}.")
    print(f"You have accumulated a total of {points} game points!")
    main()


if __name__ == "__main__":
    main()