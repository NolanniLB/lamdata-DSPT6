from pdb import set_trace as breakpoint
from random import randint


class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if self.price/self.weight < 0.5:
            print('Not so stealable')
        if self.price/self.weight >= 0.5 and < 1.0:
            print('Kinda stealable')
        else:
            print('Very stealable')

    def explode(self):
        if self.flammability*self.weight < 10:
            print('Fizzle')
        if self.flammability*self.weight >= 10 and < 50:
            print('Boom')
        else:
            print('BABOOM!!')


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):

        super().__init__()

    def explode(self):
        if self.explode is True:
            print('it is a glove')
        else:
            print('it is a glove')

    def punch(self):
        if self.punch < 5:
            print('That tickles')
        if self.punch >= 5 and < 15:
            print('Hey that hurts')
        else:
            print('OUCH!')


if __name__ == '__main__':
    breakpoint()
