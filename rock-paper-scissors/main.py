rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
throw = [rock, paper, scissors]

humanthrow = int(input("Enter 0 for rock, 1 for paper, 2 for scissors.\n"))
humanbattle = throw[humanthrow]
print(f"You chose {humanbattle}")


computerbattle = random.choice(throw)
print(f"The computer chose {computerbattle}")

if humanbattle > computerbattle:
  print("You win!")
elif humanbattle < computerbattle:
  print("You lose...")
else:
  print("It's a draw.")

print("Thanks for playing!")
