max_satiation = 1000


class NotHungry(Exception):
    'Executed when animal is not hungry'
    pass


class Animal:
    def __init__(self):
        self.stomach = []
        self.satiation = 0

    def eat(self, grass):
        try:
            if self.__is_hungry():
                self.stomach.append(grass)
                self.satiation += grass.get_nutritional_value()
            else:
                raise NotHungry
        except NotHungry:
            print('Я не голоден')

    def __is_hungry(self):
        return len(self.stomach) == 0 or self.satiation < max_satiation


class Grass:
    def __init__(self, nv: int):
        self.nutritional_value = nv

    def get_nutritional_value(self):
        return self.nutritional_value


def print_result():
    animal = Animal()
    grass = Grass(150)

    animal.eat(grass)
    animal.eat(grass)
    animal.eat(grass)
    animal.eat(grass)
    animal.eat(grass)
    animal.eat(grass)
    animal.eat(grass)
    animal.eat(grass)
