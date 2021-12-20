class SpaceObject:
    def __init__(self, name=None):
        self.name = name


class Planet(SpaceObject):
    def __init__(self, name, population=None):
        super().__init__(name)
        self.population = population or 0

    def __str__(self):
        return f'Population of {self.name} = {self.population}'


class Animal:
    def __init__(self, name=None, planet=None):
        self.name = name
        self.planet = planet

    def creation(self, planet):
        self.planet = planet
        self.planet.population += 1


class Dog(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().creation(planet)
        self.mood = 15
        self.health = 60

    def eat(self):
        self.health += 5
        self.mood += 5

    def run(self):
        self.health += 10
        self.mood -= 5


class Cat(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().creation(planet)
        self.mood = 20
        self.health = 40

    def eat(self):
        self.health += 10
        self.mood += 5

    def sleep(self):
        self.health += 5
        self.mood -= 5


class Reptile(Animal):
    def __init__(self, name, planet):
        super().__init__(name, planet)
        super().creation(planet)
        self.mood = 30
        self.health = 30

    def eat(self):
        self.health += 20
        self.mood += 10

    def play(self):
        self.health -= 10
        self.mood += 5


earth = Planet('Earth')

dogs = [Dog('Laika', earth),
        Dog('Belka', earth),
        Dog('Strelka', earth),
        ]
cats = [Cat('Boris', earth)]
reptiles = [Reptile('Vupsen', earth),
            Reptile('Pupsen', earth)
            ]

print(earth)
