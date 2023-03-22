"""Personality quiz: Choose your own adventure game"""

__author__ = "730556602"


def greet() -> None:
    """Greeting for quiz"""
    global player_name
    player_name = input("Player, what is your name?: ")
    print(f"Hello {player_name}, welcome to the adventure game!")



def main() -> None:
    """Main function for personality quizzes"""
    greet()
    global game_points
    game_points = 0
    print(f"You currently have {game_points} game points!")
    while True:
        personality_game: str = input("Do you want to take a personality quiz, yes or no?: ")
        if personality_game == "yes":
            game_points = animal_quiz(game_points)
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

def animal_quiz(game_points: int) -> int:
    """Personaility quiz about animals"""
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
        print("Yay! You are most like a cheetah!")
    elif response_points >= 5 and response_points < 7:
        print("Yay you are most like a whale!")
    elif response_points >= 7 and response_points <= 9:
        print("Yay! You are most like a lizard!")
    game_points += 2
    print(f"Congrats! For taking this quiz, you now have {game_points} game points")
    main()
    return game_points

    


def update_points() -> None:
    from random import randint
    global player_name, game_points
    print(f"Hello {player_name}, you currently have {game_points}! You now have the opportunity to earn or lose some points!")
    print("You can enter 'A' to add points, but the system has a mind of its own and won't always follow directions.")
    print("Sometimes the system will give you points if you press 'A', but it can also subtract points! Beware and test your luck with this game!")
    choice = input("Choose 'A' or enter 'X' to return to main: ")
    if choice != "A" and choice != "X":
        choice = input("Sorry, that was not a valid option, choose again!")
    while choice == "A":
        random_number = randint(-5, 5)
        game_points += random_number
        print(f"You gained {random_number} points. Your total score is now {game_points}")
        choice = input("Choose 'A' or enter 'X' to return to main: ")
    if choice == "X":
        print(f"You have {game_points} game points.")
        main()

def goodbye_message() -> None:
    print("Sorry to see you go")
    print(f"You have {game_points} game points!")
    main()


if __name__ == "__main__":
    main()