import os
import random
import readchar

POS_X = 0
POS_Y = 1
NUM_OF_POKEMON_TRAINERS = 5

my_position = [1, 1]
trainers_objects = []
end_game = False

# Representation of the map
map_definition = """\
############################
#                   ########
#                   ########
###      ####              #
###      ####         ######
#                          #
#         #########        #
#        ###########       #
#         #########        #
#            ###      ###  #
#                     ###  #
###########                #
#      ####           ######
#                     ######
############################
"""

# Create obstacle map
map_definition = [list(row) for row in map_definition.split("\n")]
MAP_WIDTH = len(map_definition[0])
MAP_HEIGHT = 15

# Pokemon combat
# Life score of the Pokemon's
total_life_score_pokemon = 100;
life_score_pikachu = 100
life_score_squirtle = 100

# Collections with attacks per pokemon
pikachu_attacks = {0: {'attack': 'Electro ball', 'damage': 10},
                   1: {'attack': 'Thunderbolt', 'damage': 11}}

squirtle_attacks = {'T': {'attack': '[T]ackle', 'damage': 10},
                    'W': {'attack': '[W]ater gun', 'damage': 12},
                    'B': {'attack': '[B]ubble', 'damage': 9}}

last_shift = random.randint(0, 1)

os.system('cls')
while not end_game:
    os.system('cls')

    # Generate random objects on the map
    while len(trainers_objects) <= NUM_OF_POKEMON_TRAINERS:
        position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if position not in trainers_objects and position != my_position and \
                map_definition[position[POS_Y]][position[POS_X]] != "#":
            trainers_objects.append(position)

    # Draw map
    print("+" + "-" * MAP_WIDTH * 2 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            trainer_in_cell = None

            for trainer_object in trainers_objects:
                if trainer_object[POS_X] == coordinate_x and trainer_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    trainer_in_cell = trainer_object

            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                char_to_draw = " @"

                if trainer_in_cell is not None:
                    os.system('cls')
                    while life_score_pikachu > 0 and life_score_squirtle > 0:
                        # Pikachu turn
                        if last_shift == 0:
                            print('Pikachu turn')
                            attack = pikachu_attacks[random.randint(0, 1)]
                            print('Pikachu attack with {}'.format(attack['attack']))
                            life_score_squirtle = life_score_squirtle - attack['damage']
                            last_shift = 1

                            # Show life score of the pokemons
                            # Life bars pikachu
                            life_bars_pikachu = int((life_score_pikachu * 10) / total_life_score_pokemon)
                            print('Pikachu      [{}{}]({}/{})'.format('*' * life_bars_pikachu,
                                                                      ' ' * (10 - life_bars_pikachu),
                                                                      life_score_pikachu if life_score_pikachu > 0 else 0,
                                                                      total_life_score_pokemon))

                            # Life bars squirtle
                            life_bars_squirtle = int((life_score_squirtle * 10) / total_life_score_pokemon)
                            print('Squirtle     [{}{}]({}/{})'.format('*' * life_bars_squirtle,
                                                                      ' ' * (10 - life_bars_squirtle),
                                                                      life_score_squirtle if life_score_squirtle > 0 else 0,
                                                                      total_life_score_pokemon))

                            input("Press key to continue...")
                            os.system('cls')

                        # Squirtle turn
                        if last_shift == 1:
                            print('Squirtle turn')
                            selected_attack = None

                            while selected_attack not in ['T', 'W', 'B', 'S']:
                                selected_attack = input('Select attack [T]ackle, [W]ater gun, [B]ubble, [S]kip: ')

                            if selected_attack != 'S':
                                attack = squirtle_attacks[selected_attack]
                                print('Squirtle attack with {}'.format(attack['attack']))
                                life_score_pikachu = life_score_pikachu - attack['damage']

                            last_shift = 0

                            # Show life score of the pokemons
                            # Life bars pikachu
                            life_bars_pikachu = int((life_score_pikachu * 10) / total_life_score_pokemon)
                            print('Pikachu      [{}{}]({}/{})'.format('*' * life_bars_pikachu,
                                                                      ' ' * (10 - life_bars_pikachu),
                                                                      life_score_pikachu if life_score_pikachu > 0 else 0,
                                                                      total_life_score_pokemon))

                            # Life bars squirtle
                            life_bars_squirtle = int((life_score_squirtle * 10) / total_life_score_pokemon)
                            print('Squirtle     [{}{}]({}/{})'.format('*' * life_bars_squirtle,
                                                                      ' ' * (10 - life_bars_squirtle),
                                                                      life_score_squirtle if life_score_squirtle > 0 else 0,
                                                                      total_life_score_pokemon))

                            input("Press key to continue...")
                            os.system('cls')

                    if life_score_squirtle > life_score_pikachu:
                        print('Squirtle is the winner')
                        trainers_objects.remove(trainer_in_cell)
                    else:
                        print('Pikachu is the winner')

                    os.system('cls')

            if map_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    # Ask user where he wants to move
    # direction = input("Where do you want to move? [WASD]: ")
    direction = readchar.readchar().decode()
    new_position = None

    if direction == 'w':
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == 's':
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == 'a':
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == 'd':
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == 'q':
        end_game = True

    if new_position:
        if map_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position
