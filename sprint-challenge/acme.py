import random

class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def name(self):
        return self.name

    def price(self):
        return self.price

    def weight(self):
        return self.weight

    def flammability(self):
        return self.flammability

    def identifier(self):
        self.identifier = random.randint(1000000,9999999)
        return self.identifier

    def stealability(self):
        self.stealability = self.price / self.weight
        if self.stealability < 0.5:
            return 'Not so stealable...'
        if (self.stealability >= 0.5) & (self.stealability < 1.0):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        self.explode = self.flammability * self.weight
        if self.explode < 10:
            return '...fizzle.'
        if (self.explode >= 10) & (self.explode < 50):
            return '...boom!'
        else:
            return '...BABOOM!!'
