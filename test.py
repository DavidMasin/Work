class Animal():
    def __init__(self, name, age, type):
        self.name = name
        self.age = age


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 14, "Cat")
        self.sound = 'Meow'

    def print(self):
        print(self.sound)
        print(self.name)
        print(self.age)


class Kitty(Cat):
    def __init__(self):
        super().__init__("Kitty")

    def print(self):
        print(self.sound)
        print(self.name)
        print(self.age)


if __name__ == '__main__':
    Kitty().print()
