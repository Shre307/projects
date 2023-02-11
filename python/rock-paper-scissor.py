import random

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

images=[Rock, Paper, Scissors]
choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if choice>=3:
    print("You could'nt even follow the instructions? You lose! ")
else:
    print(images[choice])

    computer_choice=random.randint(0,2)
    print(f"Computer chose:")
    print(images[computer_choice])


    if choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and choice ==0:
        print("YOu lose!")
    elif computer_choice > choice:
        print("Computer Wins!")
    elif choice > computer_choice:
        print("You Win!")
    elif computer_choice == choice:
        print("It's a DRAW! ")




# print("Your chose:")
# if choice=="0":
#     print(Rock)
# elif choice=="1":
#     print(Paper)
# else:
#     print(Scissors)

# print("Computer chose: \n")

# if computer_choice==0:
#     print(Rock)
# elif computer_choice==1:
#     print(Paper)
# else:
#     print(Scissors)
