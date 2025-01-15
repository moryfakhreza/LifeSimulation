# main.py
from character import Character
from events import random_event

def main():
    name = input("Enter your character's name: ")
    player = Character(name)

    while True:
        print("\nCurrent Status:")
        player.display_status()
        action = input("\nChoose an action: (1) Age Up, (2) Random Event, (3) Quit: ")

        if action == "1":
            player.age_up()
        elif action == "2":
            random_event(player)
        elif action == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()