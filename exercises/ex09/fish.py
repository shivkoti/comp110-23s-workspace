"""File to define Fish class."""


class Fish:
    """Creating a class for Fish."""
    age: int
    
    def __init__(self):
        """Initializing fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """One day for a fish."""
        self.age += 1
        return None