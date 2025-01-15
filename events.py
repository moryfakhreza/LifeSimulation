import random

def random_event(character):
    events = [find_money, get_sick, study_hard]
    event = random.choice(events)
    event(character)

def find_money(character):
    money_found = random.randint(20, 100)
    character.money += money_found
    print(f"You found ${money_found} on the ground!")

def get_sick(character):
    health_loss = random.randint(5, 20)
    character.health -= health_loss
    print(f"You got sick and lost {health_loss} health points.")

def study_hard(character):
    intelligence_gain = random.randint(1, 5)
    character.intelligence += intelligence_gain
    print(f"You studied hard and gained {intelligence_gain} intelligence points.")