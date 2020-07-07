class Thing():
    pass


print(Thing)
example = Thing()
print(example)


class Thing2:
    letters = "abc"


print(Thing2.letters)


class Thing3:
    def __init__(self):
        self.letters = "xyz"


print(Thing3().letters)


class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        print("wow")
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return str((self.name, self.symbol, self.number))


class Bear:
    def eats(self):
        return "berries"


class Rabbit:
    def eats(self):
        return "clover"


class Octothorpe:
    def eats(self):
        return "campers"


hydrogen = Element("Hydrogen", "H", "1")
print(hydrogen)
hydrogen.name
print(Bear().eats())
print(Rabbit().eats())
print(Octothorpe().eats())


class Laser:
    def does(self):
        return "disintegrate"


class Claw:
    def does(self):
        return "crush"


class SmartPhone:
    def does(self):
        return "ring"


class Robot:
    def __init__(self):
        self.l = Laser()
        self.c = Claw()
        self.s = SmartPhone()

    def does(self):
        print("lazer", self.l.does())
        print("claw", self.c.does())
        print("smartphone", self.s.does())


Robot().does()
