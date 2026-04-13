import random

print("Welcome to Rock, Paper, Scissors!\n Please choose one of the following options:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
user_choice = int(input("Enter your choice (1, 2, or 3): "))

moves = [1, 2, 3]
computer_move = random.choice(moves)


while 1:
    if user_choice in [1, 2, 3]:
        if computer_move == 1 and user_choice == 1 :
            print("Tie! Computer chose Rock, you chose Rock")
        elif computer_move == 1 and user_choice == 2 :
            print("You win! Computer chose Rock, you chose Paper")
        elif computer_move == 1 and user_choice == 3 :
            print("You lose! Computer chose Rock, you chose Scissors")
        elif computer_move == 2 and user_choice == 1 :
            print("You lose! Computer chose Paper, you chose Rock")
        elif computer_move == 2 and user_choice == 2 :
            print("Tie! Computer chose Paper, you chose Paper")
        elif computer_move == 2 and user_choice == 3 :
            print("You win! Computer chose Paper, you chose Scissors")
        elif computer_move == 3 and user_choice == 1 :
            print("You win! Computer chose Scissors, you chose Rock")
        elif computer_move == 3 and user_choice == 2 :
            print("You lose! Computer chose Scissors, you chose Paper")
        elif computer_move == 3 and user_choice == 3 :
            print("Tie! Computer chose Scissors, you chose Scissors")
        else :
            print("Invalid choice! Please enter 1, 2, or 3.")
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

