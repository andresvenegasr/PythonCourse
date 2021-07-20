import random

life_score_pikachu = 100
life_score_squirtle = 100

pikachu_attacks = {0: {'attack': 'electro ball', 'damage': 10},
                   1: {'attack': 'thunderbolt', 'damage': 11}}

squirtle_attacks = {0: {'attack': 'tackle', 'damage': 10},
                    1: {'attack': 'water gun', 'damage': 12},
                    2: {'attack': 'bubble', 'damage': 9}}
username = None
cpu_user = 'CPU'

last_shift = random.randint(0, 1)
username = input('Enter your username: ')

print(f'The first user to attack is: {username if last_shift == 1 else cpu_user}')

while life_score_pikachu > 0 and life_score_squirtle > 0:
    print(f'Pikachu: {life_score_pikachu} Squirtle: {life_score_squirtle}')
    if last_shift == 0:
        print('--------------')
        print('Pikachu turn')
        attack = pikachu_attacks[random.randint(0, 1)]
        print('Pikachu attack with {}'.format(attack['attack']))
        life_score_squirtle = life_score_squirtle - attack['damage']
        last_shift = 1
    if last_shift == 1:
        print('--------------')
        print('Squirtle turn')
        selected_attack = None

        while selected_attack is None:
            str_selected_attack = input('Select attack [0: tackle, 1:water gun, 2:bubble]: ')
            selected_attack = int(str(str_selected_attack))

        attack = squirtle_attacks[selected_attack]
        print('Squirtle attack with {}'.format(attack['attack']))
        life_score_pikachu = life_score_pikachu - attack['damage']
        last_shift = 0

if life_score_squirtle <= 0:
    print('CPU is the winner')

if life_score_pikachu <= 0:
    print('Squirtle is the winner')