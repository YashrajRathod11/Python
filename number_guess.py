import math
import random

#Input Lower and Higher Bound for the Guessing Game.
lower = int(input("Enter the lower Bound: "))
higher = int(input("Enter the higher bound: "))

#Generating Random Number between Lower and Higher
x = random.randint(lower, higher)
total_chances = math.ceil(math.log(higher - lower + 2, 2))

count = 0
flag = False

while count <= total_chances:
    count += 1
    guess = int(input("Guess the number: "))
    if guess == x:
        print("Congratulations! U choose the right Number!")
        flag = True
        break
    elif x > guess:
        print("You choose to Smaller!")
    elif x < guess:
        print("You choose to Higher")

if not flag:
    print('The number was: ', x)
    print('Better luck next time!!!')
