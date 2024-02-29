Rock =('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

Paper =('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

Scissors =('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

variable = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
list = [Rock, Paper, Scissors]

if variable >= 3 or variable < 0:
    print("That's not a valid input.")

print(list[variable])

print("Computer chose:")

import random
jo =random.randint(0,2)
print(list[jo])

if variable == 0 and jo == 0:
    print("It's a tie.")
elif variable == 0 and jo == 1:
    print("You lose.")
elif variable == 0 and jo == 2:
    print("You win.")

if variable == 1 and jo == 0:
    print("You win.")
elif variable == 1 and jo == 2:
    print("You lose.")

if variable == 2 and jo == 0:
    print("You lose.")
elif variable == 2 and jo ==1:
    print("You win.")
