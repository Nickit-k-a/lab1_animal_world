class Animal:
    def __init__(self):
        self.__age: int = 0
        self.__name: str = ""
        self.__life_points: int = 0
        self.__food_points: int = 0
        self.__symbol: str = ""
        self.__pos_x: int = 0
        self.__pos_y: int = 0
        self.__maturation_age: int = 0
        self.__is_predator = False

    def __str__(self):
        return f"{self.name}||{self.age}||{self.food_points}||{self.life_points}||{self.symbol}||{self.pos_x}||{self.pos_y}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def life_points(self):
        return self.__life_points

    @life_points.setter
    def life_points(self, life_points: int):
        self.__life_points = life_points

    @property
    def food_points(self):
        return self.__food_points

    @food_points.setter
    def food_points(self, food_points: int):
        self.__food_points = food_points

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: int):
        self.__symbol = symbol

    @property
    def pos_x(self):
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, pos_x: int):
        self.__pos_x = pos_x

    @property
    def pos_y(self):
        return self.__pos_y

    @pos_y.setter
    def pos_y(self, pos_y: int):
        self.__pos_y = pos_y

    @property
    def maturation_age(self):
        return self.__maturation_age

    @maturation_age.setter
    def maturation_age(self, maturation_age: int):
        self.__maturation_age = maturation_age

    @property
    def is_predator(self):
        return self.__is_predator

    @is_predator.setter
    def is_predator(self, is_predator: bool):
        self.__is_predator = is_predator
