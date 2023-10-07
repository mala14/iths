import random

def pc_choice():
    """
        Game rock, paper scissors. Played until a win.
        Pc rand choice from choices.
    """
    cpu_choice = random.choice(choices)
    return cpu_choice

def main():
    """
        Main game. Player selects choice. If tied a new round starts.
    """
    game = input("Play rock, paper scissors (Y/N)? ").lower()
    if game == "y":
        while True:
            us_choice = input(f"Choose one from: {choices}? ").lower()
            print()
            cpu_choice = pc_choice()
            print(f"Your choice: {us_choice}")
            print(f"Computer chose: {cpu_choice}")
            print()
            if us_choice == cpu_choice:
                print("It's a tie!")              
            elif (
                (us_choice == "rock" and cpu_choice == "scissors")
                or (us_choice == "paper" and cpu_choice == "rock")
                or (us_choice == "scissors" and cpu_choice == "paper")
            ):
                print("You win!")
                break
            else:
                print("Computer wins!")
                break
    else:
        print("Bye bye, maybe next time..")


choices = ["rock", "paper", "scissors"]

if __name__ == "__main__":
    main()
