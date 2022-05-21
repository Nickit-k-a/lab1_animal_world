import json
import random

from Animal import Animal
from Predator import Bear
from herbivore import Bird
from Predator import Boar
from herbivore import Deer
from Predator import Fox
from herbivore import Rabbit
from Predator import Wolf


class Reserve:
    __FIELD_SIZE = 10

    def __init__(self):
        self.animals = []
        self.animals_field = None

    def initialization(self):
        self.create_animals_field()
        self.create_animals()
        for animal in self.animals:
            animal.pos_x = random.randint(0, self.__FIELD_SIZE - 1)
            animal.pos_y = random.randint(0, self.__FIELD_SIZE - 1)
        self.print_animals_field()

    def create_animals_field(self):
        self.animals_field = []
        for iterator1 in range(self.__FIELD_SIZE):
            self.animals_field.append([])
        for iterator1 in range(self.__FIELD_SIZE):
            for iterator2 in range(self.__FIELD_SIZE):
                self.animals_field[iterator1].append("o")

    def create_animals(self):
        for iterator1 in range(3):
            self.animals.append(Fox())
            self.animals.append(Deer())
            self.animals.append(Wolf())
            self.animals.append(Boar())
            self.animals.append(Bear())
            self.animals.append(Rabbit())
            self.animals.append(Bird())

        self.print_animal_state()

    def fill_animals_field(self):
        for iterator1 in range(self.__FIELD_SIZE):
            for iterator2 in range(self.__FIELD_SIZE):
                self.animals_field[iterator1][iterator2] = "o"
        for iterator1 in range(len(self.animals)):
            if self.animals_field[self.animals[iterator1].pos_y][self.animals[iterator1].pos_x] == "o":
                self.animals_field[self.animals[iterator1].pos_y][self.animals[iterator1].pos_x] = self.animals[iterator1].symbol
            else:
                self.animals_field[self.animals[iterator1].pos_y][self.animals[iterator1].pos_x] += self.animals[iterator1].symbol

    def print_animals_field(self):
        self.fill_animals_field()

        for iterator1 in range(self.__FIELD_SIZE):
            print(self.animals_field[iterator1])
        print("---------------------------")

    def print_animal_state(self):
        for animal in self.animals:
            print(animal)

    def move(self):
        for iterator1 in range(len(self.animals)):
            control_motion = random.randint(1, 4)
            if control_motion == 1 and self.animals[iterator1].pos_x < self.__FIELD_SIZE - 1:
                self.animals[iterator1].pos_x = self.animals[iterator1].pos_x + 1
            elif control_motion == 2 and self.animals[iterator1].pos_x > 0:
                self.animals[iterator1].pos_x = self.animals[iterator1].pos_x - 1
            elif control_motion == 3 and self.animals[iterator1].pos_y < self.__FIELD_SIZE - 1:
                self.animals[iterator1].pos_y = self.animals[iterator1].pos_y + 1
            elif control_motion == 4 and self.animals[iterator1].pos_y > 0:
                self.animals[iterator1].pos_y = self.animals[iterator1].pos_y - 1

    def add_animal(self):
        print(
            "Выберите животное для добавления: 1. Птица 2. Волк 3. Заяц 4. Медведь 5. Олень 6. Лиса 7. Кабан 0. Выход")
        while True:
            try:
                switch_key = int(input())
                while switch_key < 0 or switch_key > 7:
                    print("Введите число от 0 до 7")
                    switch_key = int(input())
                break
            except ValueError:
                print("Введите число от 0 до 7")
        if switch_key == 1:
            self.animals.append(Bird())
        elif switch_key == 2:
            self.animals.append(Wolf())
        elif switch_key == 3:
            self.animals.append(Rabbit())
        elif switch_key == 4:
            self.animals.append(Bear())
        elif switch_key == 5:
            self.animals.append(Deer())
        elif switch_key == 6:
            self.animals.append(Fox())
        elif switch_key == 7:
            self.animals.append(Boar())
        elif switch_key == 0:
            return
        print("Введите позициию животного на карте")

        print("Введите номер строки")

        while True:
            try:
                switch_key_y = int(input())
                while switch_key_y > self.__FIELD_SIZE or switch_key_y < 0:
                    print("Введите значение строки в пределах от 0 до", self.__FIELD_SIZE - 1)
                    switch_key_y = int(input())
                break
            except ValueError:
                print("Введите число от 0 до", self.__FIELD_SIZE - 1)
        self.animals[-1].pos_y = switch_key_y

        print("Введите номер столбца")
        while True:
            try:
                switch_key_x = int(input())
                while switch_key_x > self.__FIELD_SIZE or switch_key_x < 0:
                    print("Введите значение столбца в пределах от 0 до", self.__FIELD_SIZE - 1)
                    switch_key_x = int(input())
                break
            except ValueError:
                print("Введите число от 0 до", self.__FIELD_SIZE - 1)
        self.animals[-1].pos_x = switch_key_x

        self.print_animals_field()

    def save_simulation(self):
        json.dump(self.animals, open("simulation.txt", "w"), cls=AnimalEncoder, indent=4)

    def load_simulation(self):
        self.animals = json.load(open("simulation.txt", "r"), object_hook=decode_object)

    def interaction(self):
        iterator1 = 0
        while iterator1 < len(self.animals):
            if self.animals[iterator1].maturation_age > 0:
                self.animals[iterator1].maturation_age = self.animals[iterator1].maturation_age - 2
            self.animals[iterator1].age = self.animals[iterator1].age - 1
            self.animals[iterator1].life_points = self.animals[iterator1].life_points - 2
            self.animals[iterator1].food_points = self.animals[iterator1].food_points - 2
            if self.animals[iterator1].life_points <= 0 or self.animals[iterator1].food_points <= 0 or self.animals[iterator1].age <= 0:
                self.animals.pop(iterator1)
                iterator1 -= 1
            else:
                iterator2 = iterator1 + 1
                while iterator2 < len(self.animals):
                    if self.animals[iterator1].maturation_age == 0 and self.animals[iterator2].maturation_age == 0:
                        if type(self.animals[iterator1]) == type(self.animals[iterator2]):
                            if self.animals[iterator1].pos_x == self.animals[iterator2].pos_x and \
                                    self.animals[iterator1].pos_y == self.animals[iterator2].pos_y:
                                self.animals.insert(0, (type(self.animals[iterator1])()))
                                iterator1 += 1
                                iterator2 += 1
                                self.animals[0].maturation_age = 12
                                self.animals[iterator1].maturation_age = 4
                                self.animals[iterator2].maturation_age = 4
                                self.animals[0].pos_x = self.animals[iterator1].pos_x
                                self.animals[0].pos_y = self.animals[iterator1].pos_y
                                break
                    iterator2 += 1
                iterator1 += 1
        self.nutrition()

    def nutrition(self):
        iterator1 = 0
        while iterator1 < len(self.animals):
            if self.animals[iterator1].is_predator:
                iterator2 = 0
                while iterator2 < len(self.animals):
                    if not self.animals[iterator2].is_predator:
                        if self.animals[iterator1].pos_x == self.animals[iterator2].pos_x and \
                                self.animals[iterator1].pos_y == self.animals[iterator2].pos_y:
                            self.animals[iterator1].food_points = self.animals[iterator1].food_points + self.animals[iterator2].food_points
                            self.animals.pop(iterator2)
                            if iterator2 > iterator1:
                                iterator1 -= 1
                            else:
                                iterator1 += 1
                            break
                    iterator2 += 1
            iterator1 += 1


class AnimalEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, Animal):
            return {f'__{object.__class__.__name__}__': object.__dict__}
        return json.JSONEncoder.default(self, object)


def decode_object(object):
    if '__Bear__' in object:
        animal = Bear()
        animal.__dict__.update(object['__Bear__'])
        return animal
    elif '__Bird__' in object:
        animal = Bird()
        animal.__dict__.update(object['__Bird__'])
        return animal
    elif '__Boar__' in object:
        animal = Boar()
        animal.__dict__.update(object['__Boar__'])
        return animal
    elif '__Deer__' in object:
        animal = Deer()
        animal.__dict__.update(object['__Deer__'])
        return animal
    elif '__Fox__' in object:
        animal = Fox()
        animal.__dict__.update(object['__Fox__'])
        return animal
    elif '__Rabbit__' in object:
        animal = Rabbit()
        animal.__dict__.update(object['__Rabbit__'])
        return animal
    elif '__Wolf__' in object:
        animal = Wolf()
        animal.__dict__.update(object['__Wolf__'])
        return animal
    return object


if __name__ == '__main__':
    reserve = Reserve()
    reserve.initialization()

    while True:
        print("Выберите вариант для продолжения:")
        print("1 - Сделать ход")
        print("2 - Добавить животное")
        print("3 - Сохранить симуляцию в файл")
        print("4 - Загрузить симуляцию из файла")
        print("5 - Вывести игровое поле")
        print("0 - Выход")
        try:
            switch_key = int(input())
        except ValueError:
            print("Некорретный ввод")
            switch_key = -1
        if switch_key == 1:
            reserve.move()
            reserve.print_animals_field()
            reserve.interaction()
        elif switch_key == 2:
            reserve.add_animal()
            reserve.interaction()
        elif switch_key == 3:
            reserve.save_simulation()
        elif switch_key == 4:
            reserve.load_simulation()
        elif switch_key == 5:
            reserve.print_animals_field()
        elif switch_key == 0:
            break
    print(switch_key)
