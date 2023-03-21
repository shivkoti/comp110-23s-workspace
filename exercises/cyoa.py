"""Personality quiz: Choose your own adventure game"""

__author__ = "730556602"

game_points = 0
sad_face = "\U0001F622"
happy_face = "\U0001F604"

def greet() -> None:
    """Greeting for quiz"""
    player_name: str = input("Player, what is your name?: ")
    print(f"Hello {player_name}, welcome to the personality game!")
    print(f"You currently have {game_points} game points!")


def main() -> None:
    """Main function for personality quizzes"""
    greet()
    global game_points
    continue_game: str = input("Do you want to take a personality quiz, yes or no?: ")
    while continue_game == "yes":
        option: str = input("Would you like to take the personality quiz on animals or plants?: ")
        if option == "animals":
            game_points += 1
            personality_quiz_animals()
        if option == "plants": 
            game_points += 1
            personality_quiz_plants()
        if option not in ["plants", "animals"]:
            option = input("Sorry that was an invalid option, please choose again!")
    while continue_game == "no":
        exit_game()
    while continue_game != "yes" or "no":
        continue_game: str = input("Sorry, that was an invalid option, choose again!")
        

def personality_quiz_animals() -> None:
    """Personality quiz on animals"""
    print(f"Hello! Welcome to the animal personality quiz!")
    print("Answer the following questions with 'A', 'B', or 'C' to find out which animal you are most like!")
    questions_animal: list[str] = ["What is your favorite color? A-Red B-Blue C-Green ", "What is your favorite food? A-Meat B-Vegetables C-Fruits", "What is your favorite activity? A-Running B-Swimming C-Climbing"]
    animal_responses: list[str] = []
    for i in range(len(questions_animal)):
        current_question = questions_animal[i]
        print(current_question)
        response_for_animal = input("Enter your answer: ")
        while response_for_animal not in ["A", "B", "C"]:
            response_for_animal = input("Invalid answer, please enter 'A', 'B', or 'C': ")
        animal_responses.append(response_for_animal)
    score_animal: dict[str, int] = {"snake": 0, "cheetah": 0, "bear": 0}
    for response_for_animal in animal_responses:
        if response_for_animal == "A":
            score_animal["snake"] += 1
        elif response_for_animal == "B":
            score_animal["cheetah"] += 1
        elif response_for_animal == "C":
            score_animal["bear"] += 1
    max_score = 0
    animal_type = []
    for key, value in score_animal.items(): 
        if value > max_score:
            max_score = value
            animal_type = [key]
        elif value == max_score:
            animal_type.append(key)
    if len(animal_type) == 1:
        print(f"You are most like a {animal_type}")
    else:
         print(f"You are a mix of animals: {animal_type}!")

    
def personality_quiz_plants() -> None:
    """Personality quiz on plants"""
    print(f"Hello! Welcome to the plants personality quiz!")
    print("Answer the following questions with 'A', 'B', or 'C' to find out which animal you are most like!")
    questions_plants: list[str] = ["What is your favorite color? A-Pink B-White C-Purple ", "What is your favorite fruit? A-Apple B-Pinapple C-Grapes", "Pick one. A-Sleeping B-Studying C-Hanging out with friends"]
    plants_responses: list[str] = []
    for i in range(len(questions_plants)):
        current_question = questions_plants[i]
        print(current_question)
        response_for_plants= input("Enter your answer: ")
        while response_for_plants not in ["A", "B", "C"]:
            response_for_plants = input("Invalid answer, please enter 'A', 'B', or 'C': ")
        plants_responses.append(response_for_plants)
    score_plant: dict[str, int] = {"rose": 0, "lily": 0, "lavender": 0}
    for response_for_plants in plants_responses:
        if response_for_plants == "A":
            score_plant["rose"] += 1
        elif response_for_plants == "B":
            score_plant["lily"] += 1
        elif response_for_plants == "C":
            score_plant["lavender"] += 1
    max_score = 0
    plant_type = []
    for key, value in score_plant.items(): 
        if value > max_score:
            max_score = value
            plant_type = [key]
        elif value == max_score:
            plant_type.append(key)
    if len(plant_type) == 1:
        print(f"You are most like the plant: {plant_type}")
    else:
         print(f"You are a mix of plants: {plant_type}!")



def exit_game() -> str:
    """Goodbye message to player"""
    global sad_face, happy_face
    print(f"Aww, we are sad to see you go! You have {game_points} game points.")
    random_trick: input("Before you go, we have one special trick for you to earn more game points! Would you like to continue, 'yes' or 'no'")
    if random_trick == "no":
        print(f"Alright{sad_face}, we will let you go with {game_points} points.")
    if random_trick == "yes":
        print(f"Hooray{happy_face}! The number generator will soon give you a random number of points!")
        import random
        random_points = random.randint(1, 10)
        print(f"Congrats! You now have {random_points} game points!{happy_face}!")
        random_points = game_points
    

if __name__ == "__main__":
    main()