import random

guess = int(input("Pick a number between 0 (head) and 1 (tail) to flip the coin: "))
flip = random.randint(0, 1)

print("Correct" if guess == flip else "Wrong")
