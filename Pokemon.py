class Pokemon:
    def __init__(self, name, minCP, maxCP, level, candy, moveName, moveDMG, evolutionNum, pokeType):
        self.name = name
        self.minCP = minCP
        self.maxCP = maxCP
        self.currCP = minCP
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
