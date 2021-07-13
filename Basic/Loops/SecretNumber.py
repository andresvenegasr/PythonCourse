import random

secretNumber = random.randint(0,10)
flag = False

print(secretNumber)

print('Welcome to the game.')

while not flag:
    number = int(input('Type the secret number: '))
    if number != secretNumber:
        print(f'{number} is not the secret number')
    else:
        flag = True

print(f'You are the winner! {number} is the secret number')