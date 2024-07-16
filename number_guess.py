import math
import random

lower = int(input("Enter the lower Bound: "))
higher = int(input("Enter the higher bound: "))
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
        print("You choose to high!")
    elif x < guess:
        print("U choice to small")
if not flag:
    print('The number was: ', x)
    print('Better luck next time!!!')

