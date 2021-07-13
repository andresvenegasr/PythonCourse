import random

secretNumber = random.randint(0,10)
attempts = 0
flag = False

print(secretNumber)

print('Welcome to the game.')

while not flag:
    number = int(input('Type the secret number: '))
    if number != secretNumber:
        print(f'{number} is not the secret number')
        attempts = attempts + 1
    else:
        flag = True

    if attempts == 3:
        print('I am sorry! you only have three tries')
        exit(0)

print(f'You are the winner! {number} is the secret number')