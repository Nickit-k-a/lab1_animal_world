from Animal import Animal


class Herbivore(Animal):
    def __init__(self):
        super().__init__()
        self.is_predator = False


class Rabbit(Herbivore):
    def __init__(self):
        super().__init__()
        self.name = "Zaika"
        self.age = 20
        self.life_points = 25
        self.food_points = 50
        self.symbol = "Z"

class Deer(Herbivore):
    def __init__(self):
        super().__init__()
        self.name = "Bembi"
        self.age = 50
        self.life_points = 20
        self.food_points = 60
        self.symbol = "B"

class Bird(Herbivore):
    def __init__(self):
        super().__init__()
        self.name = "Ququwka"
        self.age = 18
        self.life_points = 15
        self.food_points = 35
        self.symbol = "Q"


