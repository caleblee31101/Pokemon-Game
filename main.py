from Database import Database
from Trainer import Trainer
from Game import Game

db = Database("PokeList_v2-1.csv")
starter = db.at(5)
#print(starter)
#print(starter.getName())
player = Trainer('Caleb', starter)
player.addPokemon(db.at(6))
player.addPokemon(db.at(7))
player.addPokemon(db.at(8))
player.addPokemon(db.at(9))
player.addPokemon(db.at(10))
player.addPokemon(db.at(11))
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
