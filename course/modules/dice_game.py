import random

class Dice:
    def roll(self):
        dice_tuple = (random.randint(0, 9), random.randint(0, 9))
        return dice_tuple
dice_game = Dice()
print(dice_game.roll())
