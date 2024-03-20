import random

class Ball:
    def __init__(self, number):
        self.number = number

    @classmethod
    def draw(cls):
        return cls(random.randint(1, 20))