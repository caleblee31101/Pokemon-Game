import csv
from Pokemon import Pokemon
class Database:
    __PokemonList = [0]
    def __init__(self, filename):
        self.filename = filename
        self.loadFile(filename)
    def loadFile(self, filename):
        with open(filename, 'r') as csvfile:
            data = csv.reader(csvfile)
            # remove the first title entry
            #data.pop(0)
            for pokeData in data:
                if pokeData[0] == 'Index':
                    continue
                name = pokeData[1]
                minCP = int(pokeData[2])
                maxCP = int(pokeData[3])
                level = int(pokeData[4])
                candy = int(pokeData[5])
                moveName = pokeData[6]
                moveDMG = int(pokeData[7])
                evolutionNum = int(pokeData[8])
                pokeType = pokeData[9]
                self.pokemon = Pokemon(name, minCP, maxCP, level, candy, moveName, moveDMG, evolutionNum, pokeType)
                self.__PokemonList.append(self.pokemon)
    def at(self, index):
        return self.__PokemonList[index]
    def printData(self):
        for pokemon in self.__PokemonList:
            print(pokemon)
