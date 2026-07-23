import random
print('Lets play rock, paper, scissors!')
random.randint(1, 3)
rock=1
paper=2
sissors=3
user_input = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))
if user_input == 1:
    print("You chose rock")
elif user_input == 2:
    print("You chose paper")
elif user_input == 3:
    print("You chose scissors")
else:    print("Invalid input")
computer_input = random.randint(1, 3)
if computer_input == 1:
    print("Computer chose rock")
elif computer_input == 2:
    print("Computer chose paper")
elif computer_input == 3:
    print("Computer chose scissors")
if user_input == computer_input:
    print("It's a tie!")
elif (user_input == 1 and computer_input == 3) or (user_input == 2 and computer_input == 1) or (user_input == 3 and computer_input == 2):
    print("You win!")
else:    print("Computer wins!")