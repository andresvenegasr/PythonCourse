import os
import random

import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OF_MAP_OBJECTS = 11

my_position = [0, 0]
map_objects = []
tail = []
tail_length = 0

# Generate random objects on the map
while len(map_objects) <= NUM_OF_MAP_OBJECTS:
    position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

    if position not in map_objects and position != my_position:
        map_objects.append(position)

os.system('cls')

while True:
    os.system('cls')
    # Draw map
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"

            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                char_to_draw = "@"

                if object_in_cell is not None:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Ask user where he wants to move
    # direction = input("Where do you want to move? [WASD]: ")
    direction = readchar.readchar().decode()

    if direction == 'w':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == 's':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == 'a':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == 'd':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == 'q':
        break