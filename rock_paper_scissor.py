import random 
options = ("Rock", "Paper", "Scissors")
while True:
    player_choice = input("Choose One (Rock, Paper, Scissors): ").capitalize()
    if player_choice not in options:
        print("Invalid choice. Please choose from (rock , paper, scissors) ")
        continue
    computer_choice = random.choice(options)

    print(f"Your choice: {player_choice} \nComputer choice: {computer_choice}")

    if player_choice == "Rock" and computer_choice == "Scissors":
        print("Congrats! You win")
    elif player_choice == "Paper" and computer_choice == "Rock":
        print("Congrats! You win")
    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("Congrats! You win")
    elif player_choice == computer_choice:
        print("Oh.... It's a tie")
    else:
        print("You lose... Better luck next time")

    play_again = input("Do you want to play again ? yes/no: ").lower()
    if play_again != "yes":
        print('Thanks for playing.')
        break
