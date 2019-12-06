import random

class Product:
    """Basic template for products with name, price, weight, flammability,
    stealability, explode."""

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



class BoxingGlove(Product):
    """Boxing Glove item that is inherited from Product class with added
    punch and altered explode."""

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        super().__init__(name=name, price=price, weight=10,
                            flammability=flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        if (self.weight >= 5) & (self.weight < 15):
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
