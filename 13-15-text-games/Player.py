import random

import constants

class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name

    @classmethod
    def create(cls):
        name = input('Type a player name: ') or 'Player #'
        return cls(name)

    def go(self):
        return random.choice(constants.CHOICES)

    def scored(self):
        self.score += 1

    def __str__(self):
        return self.name
