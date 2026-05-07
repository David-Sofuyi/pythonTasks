import random
user = int(input("0=Scissors, 1=Rock, 2=Paper: "))
comp = random.randint(0, 2)
print(f"Computer: {comp}")

if user == comp:
    print("Draw")
elif (user - comp) % 3 == 1:
    print("You win")
else:
    print("You lose")
