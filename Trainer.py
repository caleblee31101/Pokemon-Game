from Pokemon import Pokemon

class Trainer:
    def __init__(self, name, pokemon):
        self.__name = name
        self.__pokemonHand = pokemon
        self.__pokemonCollection = [0]
        self.__pokemonCollection.append(pokemon)
    def addPokemon(self, pokemon):
        self.__pokemonCollection.append(pokemon)
    def setHandPokemon(self, index):
        self.__pokemonHand = self.__pokemonCollection[index]
    def getName(self):
        return self.__name
    def getPokemon(self, index):
        return self.__pokemonCollection[index]
    def getCollection(self):
        return self.__pokemonCollection
    def getHandPokemon(self):
        return self.__pokemonHand
