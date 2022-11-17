from Database import Database
from Trainer import Trainer
from Pokemon import Pokemon
class Game:
    def __init__(self, db, player):
        self.__state = 0
        self.__db = db
        self.__player = player
    def runState(self, input):
        if self.__state == 0:
            if input == 0:
                self.__state = 0
            elif input == 1:
                self.__state = 1
            elif input == 2:
                self.__state = 2
            else:
                return False
        elif self.__state == 1:
            if input == 1:
                print('level up placeholder')# level up process
            elif input == 2:
                self.__state = 0
            else:
                return False
        elif self.__state == 2:
            if 0 < input < len(self.__player.getCollection()):
                self.__player.setHandPokemon(input)
            elif input == 0:
                self.__state = 0
            else:
                return False
        if self.__state == 0:
            print(30 * '-', f"{'MAIN MENU':^20}", 30 * '-')
            print('0. Stay in Main Menu')
            print('1. View current Pokemon')
            print('2. Change current Pokemon')
            print('3. Catch a new Pokemon')
        elif self.__state == 1:
            print(30 * '-', f"{'Current Pokemon':^20}", 30 * '-')
            pokemon = self.__player.getHandPokemon()
            print(pokemon.name)
            print()
            print(f"{'Current CP: ' + str(pokemon.currCP):<30}{1:^20}{1:>30}")
            print(f"{'Current Level: ' + str(pokemon.level):<30}{1:^20}{1:>30}")
            print(f"{'Candies: ' + str(pokemon.candy):<30}{1:^20}{1:>30}")
            print()
            print('1 - Use Candy to Level-Up')
            print('2 - Exit to Main Menu')
        elif self.__state == 2:
            print(30 * '-', f"{'Pokemon Selection Menu':^20}", 30 * '-')
            pokemon = self.__player.getHandPokemon()
            print(pokemon.name)
            print()
            print(f"{'Current CP: ' + str(pokemon.currCP):<30}{1:^20}{1:>30}")
            print(f"{'Current Level: ' + str(pokemon.level):<30}{1:^20}{1:>30}")
            print(f"{'Candies: ' + str(pokemon.candy):<30}{1:^20}{1:>30}")
            print()
            print(80 * '-')
            collection = self.__player.getCollection()
            for i, pokemon in enumerate(collection):
                if pokemon == 0:
                    continue
                elif i % 4 == 0:
                    print(f"{str(i) + '. ' + str(pokemon.name):<20}")
                    for j in range(i + 1 - 4, i + 1):
                        print(f"{'   CP ' + str(collection[j].currCP):<20}", end=' ')
                    print('\n')
                elif i % 4 != 4 and i == len(collection) - 1:
                    print(f"{str(i) + '. ' + str(pokemon.name):<20}")
                    for j in range(i + 1 - (i % 4), i + 1):
                        print(f"{'   CP ' + str(collection[j].currCP):<20}", end=' ')
                else:
                    print(f"{str(i) + '. ' + str(pokemon.name):<20}", end=' ')
            print('\n' + 80 * '-')
            print(f'Select a new Pokemon (1-{len(collection) - 1})')
        return True

    def setState(self, state):
        self.__state = state
