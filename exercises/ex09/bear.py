"""File to define Bear class."""


class Bear:
    """Creating a class for Bear."""
    age: int
    hunger_score: int

    def __init__(self): 
        """Initialzing self."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """One day for a bear."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Eat method for bear."""
        self.hunger_score += num_fish
        return None