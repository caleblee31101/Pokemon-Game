from Database import Database
from Trainer import Trainer
from Game import Game
from Savefile import Savefile
from random import randint
save = Savefile()
save.read()
db = Database("PokeList_v2-1.csv")
"""
starter = db.at(5)
player = Trainer('Caleb', starter)
player.addPokemon(db.at(6))
player.addPokemon(db.at(7))
player.addPokemon(db.at(8))
player.addPokemon(db.at(9))
player.addPokemon(db.at(10))
player.addPokemon(db.at(11))
"""
print(30 * '-', f"{'AVAILABLE SAVE FILES':^20}", 30 * '-')
print(save.getNames())
print('\n')
userInput = input('>> ')
player = save.access(userInput)
if not player:
    print('Player data does not exist, creating new player data...')
    starter = db.at(randint(1, 151))
    player = Trainer(userInput, starter)
    save.addPlayer(player)
game = Game(db, player)

game.runState(0)
userInput = input('>> ')
while userInput != 'q':
    try:
        userInput = int(userInput)
        if not game.runState(userInput):
            raise ValueError('Input value out of range!')
        #save.update(player)
    except ValueError:
        print('Invalid Input! Try again:')
        userInput = input('>> ')
        continue
    userInput = input('>> ')
save.write()
