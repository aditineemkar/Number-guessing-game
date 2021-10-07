import random 
number = random.randint(1, 9)
chances = 0
print('Number guessing game')
print('Guess a number between 1 and 9')
while chances<5:
    inputNumber=int(input("Enter your guess:- "))
    if inputNumber==number:
        print('You Won!')
        break
    elif inputNumber<number:
        print('The guess was too low')
    else:
        print('The guess was too high')
    chances=chances+1

if not chances<5:
    print('You lose!')

