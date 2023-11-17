# Create a Game (Guess a number)

import random

rand = random.randint(1,10)
user_guess = None
guess = 0

while user_guess != rand:
    user_guess = int(input("Enter the number : "))
    guess+=1
    if user_guess == rand:
        print(f"You guess right Number!\nNumber is {user_guess}")
    else:
        if user_guess > rand:
            print("Enter smaller number")
        else:
            print("Enter larger number")

print(f"You guess the number at {guess} times")

# Don't forget to make hiscore.txt
with open('hiscore.txt','r') as f:
    hiscore = f.read()

if int(hiscore) > guess:
    with open('hiscore.txt', 'w') as f:
      f.write(str(guess))