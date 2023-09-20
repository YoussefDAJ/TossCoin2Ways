# Toss coin with random.random and random.randint:
import random

print(
    """Welcome to the Coin Guessing Game!")
         Choose a method to toss the coin:
         1. Using random.random()
         2. Using random.randit()
    """
)
user_choice = int(input("Enter you choice (1 or 2): \n"))

computer_Choice2 = random.randint(0, 1)
computer_Choice1 = random.random()

if user_choice == 2:
    print("Good what do you want play? ")
    user_guess = input("Heads or Tails: ").lower()
    if user_guess == "heads" and computer_Choice2 == 1:
        print(f"Well matching {user_guess} match {computer_Choice2}")
    elif user_guess == "tails" and computer_Choice2 == 0:
        print(f"Well matching {user_guess} match {computer_Choice2}")
    elif user_guess == "tails" and computer_Choice2 != 0:
        print(f"Hard luck {user_guess} don't match {computer_Choice2}")
    elif user_guess == "heads" and computer_Choice2 != 1:
        print(f"Hard luck {user_guess} don't match {computer_Choice2}")
    else:
        print(f"the {user_guess} you have enter is not in our systeme")

elif user_choice == 1:
    print("Good what do you want to play?")
    user_guess2 = input("Heads or Tails: ").lower()
    if user_guess2 == "tails" and computer_Choice1 < 0.5:
        print(f"Good guessing your {user_guess2} has matched {computer_Choice1}")
    elif user_guess2 == "heads" and computer_Choice1 >= 0.5:
        print(f"Good guessing your choice {user_guess2} has matched {computer_Choice1}")
    elif user_guess2 == "tails" and computer_Choice1 > 0.5:
        print(f"Sorry your {user_guess2} not matching {computer_Choice1}")
    elif user_guess2 == "heads" and computer_Choice1 <= 0.5:
        print(f"Hard luck next time")
    else:
        print(f"your {user_guess2} not in our system")

else:
    print(f"the {user_choice} must be 1 or 2")
