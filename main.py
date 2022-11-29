from Database import Database
from Trainer import Trainer
from Game import Game
import random

db = Database("PokeList_v2-1.csv")
random_poker = random.randint(0, 150)
starter = db.at(random_poker)
#print(starter)
#print(starter.getName())
player = Trainer('Caleb', starter)
game = Game(db, player)
game.runState(0)
userInput = input('>> ')

while userInput != 'q':
    try:
        userInput = int(userInput)
        if not game.runState(userInput):
            raise ValueError('Input value out of range!')
    except ValueError:
        print('Invalid Input! Try again:')
        userInput = input('>> ')
        continue
    userInput = input('>> ')

    # TODO create a savefile system with a savefile that updates over time
