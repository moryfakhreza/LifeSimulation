import random

def commit_crime(character):
    crimes = ["Steal", "Fraud", "Murder"]
    crime = random.choice(crimes)
    success = random.choice([True, False])
    
    if success:
        reward = random.randint(100, 1000)
        character.money += reward
        print(f"You successfully committed {crime} and earned ${reward}.")
    else:
        print(f"You got caught while committing {crime}.")
        go_to_jail(character)

def go_to_jail(character):
    print("You are in jail.")
    escape_success = random.choice([True, False])
    if escape_success:
        print("You successfully escaped from jail!")
    else:
        print("You failed to escape from jail and served your time.")