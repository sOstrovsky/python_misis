class Storm:
    answer = "Вы сложили Воду и Воздух получили Шторм"


class Steam:
    answer = "Вы сложили Воду и Огонь получили Пар"


class Mud:
    answer = "Вы сложили Воду и Землю получили Грязь"


class Lightning:
    answer = "Вы сложили Огонь и Воздух получили Молнию"


class Dust:
    answer = "Вы сложили Землю и Воздух получили Пыль"


class Lava:
    answer = "Вы сложили Огонь и Землю получили Лаву"


class Fire:
    def __add__(self, other):
        if type(other) == Water:
            return Steam()
        elif type(other) == Soil:
            return Lava()
        elif type(other) == Air:
            return Lightning()
        else:
            return None


class Water:
    def __add__(self, other):
        if type(other) == Fire:
            return Steam()
        elif type(other) == Soil:
            return Mud()
        elif type(other) == Air:
            return Storm()
        else:
            return None


class Soil:
    def __add__(self, other):
        if type(other) == Fire:
            return Lava()
        elif type(other) == Water:
            return Mud()
        elif type(other) == Air:
            return Dust()
        else:
            return None


class Air:
    def __add__(self, other):
        if type(other) == Fire:
            return Lightning()
        elif type(other) == Soil:
            return Dust()
        elif type(other) == Water:
            return Storm()
        else:
            return None


def print_result():
    fire = Fire()
    water = Water()
    air = Air()
    soil = Soil()

    mix1 = fire + water
    mix2 = fire + air
    mix3 = fire + soil
    mix4 = water + air
    mix5 = water + soil
    mix6 = air + soil

    print(mix1.answer)
    print(mix2.answer)
    print(mix3.answer)
    print(mix4.answer)
    print(mix5.answer)
    print(mix6.answer)
