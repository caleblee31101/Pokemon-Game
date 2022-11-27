import random
class Pokemon:
    def __init__(self, name, minCP, maxCP, level, candy, moveName, moveDMG, evolutionNum, pokeType, currCP):
        self.name = name
        self.minCP = minCP
        self.maxCP = maxCP
        if currCP == minCP:
            self.currCP = random.randint(int(minCP), int(maxCP))
        else:
            self.currCP = currCP
        self.currCP = currCP
        self.level = level
        self.candy = candy
        self.moveName = moveName
        self.moveDMG = moveDMG
        self.evolutionNum = evolutionNum
        self.pokeType = pokeType
"""
The other unlisted stats to determine
maxHp
currHp
def
spd
"""
"""
    def attack(Pokemon other): # inflict DMG on other pokemon
        other.hp -= moveDMG
        if other.hp <= 0:
            return false
        else:
            return true
"""
