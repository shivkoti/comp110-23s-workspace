"""File to define River class."""
__author__ = "730556602"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Creation of class for River."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Fish] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes old animals."""
        new_fish = []
        for fish in self.fish:
            if fish.age > 3:
                new_fish.append(fish)
        self.fish = new_fish
        new_bears = []
        for bear in self.bears:
            if bear.age > 5:
                new_bears.append(bear)
        self.bears = new_bears
        return None
    
    def remove_fish(self, amount: int):
        """Method to remove fish."""
        for i in range(amount):
            if self.fish:
                self.fish.pop(0)
        return None

    def bears_eating(self):
        """Method to model bears eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                for i in range(3):
                    self.remove_fish()  
                    bear.eat()
        return None
    
    def check_hunger(self):
        """Method to check hunger of bears."""
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score > 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Method to repopulate fish."""
        num_new_fish = len(self.fish) // 2 * 4
        new_fish = []
        for i in range(num_new_fish):
            new_fish.append(Fish())
        self.fish += new_fish
        return None
    
    def repopulate_bears(self):
        """Method to repopulate bears."""
        num_new_bears = len(self.bears) // 2
        for i in range(num_new_bears):
            new_bear = Bear()
        self.bears.append(new_bear)
        return None
    
    def view_river(self):
        """View river function."""
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """One river week."""
        for i in range(7):
            self.one_river_day()
        
    def view_river(self):
        """Presents an update of the number of bears and fish in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
