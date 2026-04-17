import random

print("Welcome to Rock, Paper, Scissors!\nPlease choose one of the following options:")
print("Enter 1 for Rock")
print("Enter 2 for Paper")
print("Enter 3 for Scissors")
print("Enter 0 to exit the Game...")

while 1:
    user_choice = int(input("Enter your choice (1, 2, or 3): "))

    moves = [1, 2, 3]
    computer_move = random.choice(moves)

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
    elif user_choice == 0:
        exit()
    else :
        print("Invalid choice! Please enter 1, 2, or 3.")
    
        

