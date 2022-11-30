#!/usr/bin/env python3
from Pokemon import Pokemon
from Trainer import Trainer
import csv

class Savefile:
    __playerData = []
    def read(self):
        with open('pokemon.sav', 'r') as csvfile:
            data = csv.reader(csvfile)
            player = 0
            for playerInfo in data:
                #print(playerInfo)
                if playerInfo[0][0] == '$':
                    self.__playerData.append(player)
                    name = playerInfo[0][1:]
                    handPokemonName = playerInfo[1]
                    minCP = int(playerInfo[2])
                    maxCP = int(playerInfo[3])
                    level = int(playerInfo[4])
                    candy = int(playerInfo[5])
                    moveName = playerInfo[6]
                    moveDMG = int(playerInfo[7])
                    evolutionNum = int(playerInfo[8])
                    pokeType = playerInfo[9]
                    currCP = int(playerInfo[10])
                    handPokemon = Pokemon(handPokemonName, minCP, maxCP, level, candy, moveName, moveDMG, evolutionNum, pokeType, currCP)
                    player = Trainer(name, handPokemon)
                else:
                    name = playerInfo[0]
                    minCP = int(playerInfo[1])
                    maxCP = int(playerInfo[2])
                    level = int(playerInfo[3])
                    candy = int(playerInfo[4])
                    moveName = playerInfo[5]
                    moveDMG = int(playerInfo[6])
                    evolutionNum = int(playerInfo[7])
                    pokeType = playerInfo[8]
                    currCP = int(playerInfo[9])
                    pokemon = Pokemon(handPokemonName, minCP, maxCP, level, candy, moveName, moveDMG, evolutionNum, pokeType, currCP)
                    player.addPokemon(pokemon)
            self.__playerData.append(player)
        self.__playerData = self.__playerData[1:]
    def write(self):
        with open('pokemon.sav', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for player in self.__playerData:
                row = ['$' + player.getName(),
                       player.getHandPokemon().name,
                       player.getHandPokemon().minCP,
                       player.getHandPokemon().maxCP,
                       player.getHandPokemon().level,
                       player.getHandPokemon().candy,
                       player.getHandPokemon().moveName,
                       player.getHandPokemon().moveDMG,
                       player.getHandPokemon().evolutionNum,
                       player.getHandPokemon().pokeType,
                       player.getHandPokemon().currCP]
                writer.writerow(row)
                for pokemon in player.getCollection():
                    if pokemon == player.getHandPokemon() or pokemon == 0:
                        continue
                    #print('test')
                    #print(pokemon)
                    #print(player.getCollection())
                    row = [pokemon.name,
                           pokemon.minCP,
                           pokemon.maxCP,
                           pokemon.level,
                           pokemon.candy,
                           pokemon.moveName,
                           pokemon.moveDMG,
                           pokemon.evolutionNum,
                           pokemon.pokeType,
                           pokemon.currCP]
                    writer.writerow(row)
    def access(self, name):
        for player in self.__playerData:
            if name == player.getName():
                return player
        return False
    def addPlayer(self, player):
        print('added player')
        self.__playerData.append(player)
    def update(self, player):
        for index in range(len(self.__playerData)):
            if player.getName() == self.__playerData[index].getName():
                self.__playerData[index] = player
    def getNames(self):
        names = ""
        for player in self.__playerData:
            names += player.getName() + '\n'
        return names
    def print(self):
        print(self.__playerData)
