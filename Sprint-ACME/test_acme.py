from pdb import set_trace as breakpoint
import random
from random import randint


class Product():
    def __init__(
        self, name, price=10, weight=20, flammability=0.5,
        identifier=random.randint(1000000, 9999999)
    ):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if self.price/self.weight < 0.5:
            print('Not so stealable')
        if self.price/self.weight >= 0.5 and self.price/self.weight < 1.0:
            print('Kinda stealable')
        else:
            print('Very stealable')

if __name__ == '__main__':
    prod = Product('New Toy')
    prod.stealability()