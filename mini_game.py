import random
import csv


def data_modifier():
    """Takes the data from the PokeList and transforms it into a form that is more effiecient for battle and only
    includes stats that are necessary for battle
    Returns a list that contains these stats for all the pokemon from which a pokemon will be randomly selected."""
    adjusted_list = []
    removables = []
    available_pokemon = []
    # Open the file and set it equal to the name data
    with open('PokeList_v2-1.csv', 'r') as data:
        given = csv.reader(data)
        # After using the csv reader to split the data, we set that data into a list form
        for pokemon in given:
            available_pokemon.append(pokemon)
            for index in range(1, len(available_pokemon)):
                pokemon = available_pokemon[index]
                if len(pokemon) != 10:
                    removables.append(index)
                else:
                    # Correctly formats the given stats into a form that is easily useable
                    pokemon.pop(0)
                    pokemon.pop(4)
                    pokemon[1] = int(pokemon[1])
                    pokemon[2] = int(pokemon[2])
                    pokemon[3] = int(pokemon[3])
                    pokemon[5] = int(pokemon[5])
        return available_pokemon


def attack(attacker, defender):
    """Takes an attacking pokemon and a defending pokemon (which are both in the form a of a list with stats)
    Returns the health of the defending pokemon.
    """
    defender[0] -= random.randint(attacker[4] - 6, attacker[4] + 6)
    return defender[0]


def heal(attacker):
    """Takes a pokemon as parameter
    Heals the pokemon based on their health and a random number
    Returns the new HP of that pokemon
    """
    attacker[0] += random.randint(int(attacker[6]/3), int(attacker[6]/2.5))
    return attacker[0]


def health_printer(user, rando):
    """Takes input of both the pokemon that are battling (again in their list form)
    Prints the current HP out of the total HP for the pokemons.
    """
    print(f'{user[1]} health: {user[0]}/{user[6]}')
    print(f'{rando[1]} health: {rando[0]}/{rando[6]}')


def minigame(current_pokemon):
    """Takes a pokemon as parameter
    Generates a random pokemon for the given pokemon to fight
    Simulates a battle between the two pokemon asking user if they want to heal or attack with their pokemon.
    Ends with either pokemon falling below 0 hp
    If victorious returns a list with the stats with the captured pokemon so it can be added to the database
    If unsuccessful returns False
    """
    # pokemon_call_number = random.randint(0, 151)
    # Somehow obtain the list of the pokemon and use the call number to call the pokemon that we want.
    # Format of the list will

    dataList = data_modifier()

    # Tbh idk if it was worth typing this in but whatever.

    # Weakness: Defender is the key, if attacker is in the list of types then damage is amplified
    # Resistance: Defender is the key if the attacker is in the list of types, then damage is reduced
    weaknesses = {'Normal': ['Fighting'],
                  'Fire': ['Water', 'Ground', 'Rock'],
                  'Water': ['Grass', 'Electric'],
                  'Grass': ['Fire', 'Ice', 'Poison', 'Flying', 'Bug'],
                  'Electric': ['Ground'],
                  'Ice': ['Fire', 'Fighting', 'Rock', 'Steel'],
                  'Fighting': ['Flying', 'Psychic', 'Fairy'],
                  'Poison': ['Ground', 'Psychic'],
                  'Ground': ['Water', 'Grass', 'Ice'],
                  'Flying': ['Electric', 'Ice', 'Rock'],
                  'Psychic': ['Bug', 'Ghost', 'Dark'],
                  'Bug': ['Fire', 'Flying', 'Rock'],
                  'Rock': ['Water', 'Grass', 'Fighting', 'Ground', 'Steel'],
                  'Ghost': ['Ghost', 'Dark'],
                  'Dragon': ['Ice', 'Dragon', 'Fairy'],
                  'Dark': ['Fighting', 'Bug', 'Fairy'],
                  'Steel': ['Fire', 'Fighting', 'Ground'],
                  'Fairy': ['Poison', 'Steel']}

    resistances = {'Normal': [],
                   'Fire': ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy'],
                   'Water': ['Fire', 'Water', 'Ice', 'Steel'],
                   'Grass': ['Water', 'Grass', 'Electric', 'Ground'],
                   'Electric': ['Electric', 'Flying', 'Steel'],
                   'Ice': ['Ice'],
                   'Fighting': ['Bug', 'Rock', 'Dark'],
                   'Poison': ['Grass', 'Fighting', 'Poison', 'Bug', 'Fairy'],
                   'Ground': ['Poison', 'Rock'],
                   'Flying': ['Grass', 'Fighting', 'Bug'],
                   'Psychic': ['Fighting', 'Psychic'],
                   'Bug': ['Grass', 'Fighting', 'Ground'],
                   'Rock': ['Normal', 'Fire', 'Poison', 'Flying'],
                   'Ghost': ['Poison', 'Bug'],
                   'Dragon': ['Fire', 'Water', 'Grass', 'Electric'],
                   'Dark': ['Ghost', 'Dark'],
                   'Steel': ['Normal', 'Grass', 'Ice', 'Flying', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy'],
                   'Fairy': ['Fighting', 'Bug', 'Dark']}

    my_pokemon = current_pokemon
    random_pok = dataList[random.randint(0, 150)]
    random_pokcp = random.randint(random_pok[1], random_pok[2])
    result_pokemon = random_pok + [random_pokcp]
    result_pokemon.insert(4, 0)
    # index(0 = HP, 1 = Name, 2 = CP, 3 = Attack name, 4 = Damage, 5 = Type, 6 = Max HP)
    current_pokemon = [int(my_pokemon[1] / 2), my_pokemon[0], my_pokemon[1], my_pokemon[3], my_pokemon[4],
                       my_pokemon[6], int(my_pokemon[1] / 2)]

    random_pokemon = [int(random_pokcp / 2), random_pok[0], random_pok[1], random_pok[4], random_pok[5],
                      random_pok[7], int(random_pokcp / 2)]
    if random_pokemon[5] in weaknesses[current_pokemon[5]]:
        random_pokemon[4] *= 1.5
    if current_pokemon[5] in weaknesses[random_pokemon[5]]:
        current_pokemon[4] *= 1.5
    if random_pokemon[5] in resistances[current_pokemon[5]]:
        random_pokemon[4] *= .75
    if current_pokemon[5] in resistances[random_pokemon[5]]:
        current_pokemon[4] *= .75
    z = 0
    i = 0
    print(current_pokemon[1], 'vs', random_pokemon[1])
    health_printer(current_pokemon, random_pokemon)
    print('If you can defeat the encountered pokemon you capture it, you have two options on each turn, attack or heal:'
          ' Enter 1 to attack and 2 to heal')
    while z == 0:  # cp/5] > 0 and random_pokemon[0] > 0:
        if i % 2 == 0:
            print('Choose your move:\n'
                  '1. Attack\n'
                  '2. Heal\n')
            x = 0
            while x == 0:
                try:
                    user = input('>>')
                    if user == '1':
                        random_pokemon[0] = attack(current_pokemon, random_pokemon)
                        print(f'{current_pokemon[1]} used {current_pokemon[3]} on {random_pokemon[1]}')
                        i += 1
                        x += 1
                        if random_pokemon[0] <= 0:
                            random_pokemon[0] = 0
                            z += 1
                        health_printer(current_pokemon, random_pokemon)
                        print('\n')
                    elif user == '2':
                        current_pokemon[0] = heal(current_pokemon)
                        if current_pokemon[0] > current_pokemon[6]:
                            current_pokemon[0] = current_pokemon[6]
                        i += 1
                        x += 1
                        if random_pokemon[0] <= 0:
                            random_pokemon[0] = 0
                            z += 1
                        health_printer(current_pokemon, random_pokemon)
                    else:
                        print('Invalid input try again')
                except TypeError:
                    print('Invalid input try again')
        else:
            attack(random_pokemon, current_pokemon)
            print(f'{random_pokemon[1]} used {random_pokemon[3]} on {current_pokemon[1]}')
            i += 1
            if current_pokemon[0] <= 0:
                current_pokemon[0] = 0
                z += 1
            health_printer(current_pokemon, random_pokemon)
            print('\n')
    x = 0
    if random_pokemon[0] <= 0:
        random_pokemon[0] = 0
        print(f'You won the round and captured {random_pokemon[1]}')
    else:
        print('You lost, sorry better luck next time, you also get 0 candies.')
        return False
    return result_pokemon


def candy_gen():
    x = random.randint(0, 2)
    if x == 0:
        x = 3
    elif x == 1:
        x = 5
    else:
        x = 10
    return x


def level_up(candies, level):
    x = 1
    buff = 0
    while x == 1:
        if level < 31 and candies >= 1:
            level += 1
            candies -= 1
            buff += 1
        elif level < 40 and candies >= 2:
            level += 1
            candies -= 2
            buff += 2
        elif level == 40:
            print('ALREADY MAX LEVEL')
            x = 0
        else:
            x = 0
            if buff == 0:
                print('You do not have enough candies for an upgrade')
    return buff, level, candies