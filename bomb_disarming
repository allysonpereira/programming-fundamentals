import random
import time

def display_intro():
    print("********************************")
    print("***   BOMB DISARMAMENT GAME   ***")
    print("********************************")
    print("You have been presented with a bomb that needs to be disarmed.")
    print("You must cut the correct wires to disarm the bomb.")
    print("Be careful, cutting the wrong wire may trigger the bomb!")
    print("You have limited attempts. Good luck!\n")

def choose_wire():
    return random.choice(["red", "blue", "green", "yellow", "white", "purple", "orange"])

def disarm_bomb():
    correct_wire = choose_wire()
    wires = ["red", "blue", "green", "yellow", "white", "purple", "orange"]
    
    print("Wires available: Red, Blue, Green, Yellow, White, Purple, Orange")
    
    attempts = 3
    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt} of {attempts}")
        user_choice = input("Which wire will you cut? ").strip().lower()

        if user_choice in wires:
            if user_choice == correct_wire:
                print("\nCongratulations! You successfully disarmed the bomb!")
                return True
            else:
                print("BOOM! The bomb exploded. You have", attempts - attempt, "attempts remaining.")
                time.sleep(1)
        else:
            print("Invalid choice. Please choose a valid wire.")

    print("\nGAME OVER! The correct wire was", correct_wire)
    return False

def play_game():
    display_intro()
    while True:
        if disarm_bomb():
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    play_game()
