import os
import random

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
print('The first user to attack is: {}'.format('Pikachu' if last_shift == 1 else 'Squirtle'))
input("Press key to continue...")
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
else:
    print('Pikachu is the winner')
