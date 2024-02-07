import random
rock = """
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
signs = [rock, paper, scissor]


def randomChoiceGenerator():
    randomChoice = random.randint(0, 2)
    return randomChoice


def winner(user_choice, computer_choice):
    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif user_choice == computer_choice:
        print("Draw")


def main():
    userChoice = int(
        input("What do you choose?\n0:Rock\n1:Paper\n2:Scissor\n"))
    if userChoice > 2 or userChoice < 0:
        print("Wrong choice")
    else:
        print("User has chosen:\n"+signs[userChoice]+"\n")
        myChoice = randomChoiceGenerator()
        print("Computer has chosen:\n"+signs[myChoice]+"\n")
        winner(userChoice, myChoice)


if __name__ == "__main__":
    main()
