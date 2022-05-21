from Animal import Animal


class Predator(Animal):
    def __init__(self):
        super().__init__()
        self.is_predator = True

class Fox(Predator):
    def __init__(self):
        super().__init__()
        self.name = "Foxik"
        self.age = 6
        self.life_points = 30
        self.food_points = 30
        self.symbol = "F"

class Wolf(Predator):
    def __init__(self):
        super().__init__()
        self.name = "Seriy"
        self.age = 40
        self.life_points = 40
        self.food_points = 35
        self.symbol = "W"

class Bear(Predator):
    def __init__(self):
        super().__init__()
        self.name = "Miwka"
        self.age = 45
        self.life_points = 80
        self.food_points = 40
        self.symbol = "M"

class Boar(Predator):
    def __init__(self):
        super().__init__()
        self.name = "Kaban"
        self.age = 30
        self.life_points = 50
        self.food_points = 70
        self.symbol = "K"
