import random
hidden = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess: "))
    attempts += 1
    
    if guess < hidden:
        print("higher")
    elif guess > hidden:
        print("lower")
    else:
        print(f" correct! ({attempts}attempy)")
        break
