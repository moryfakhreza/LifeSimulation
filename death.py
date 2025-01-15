import random

def check_death(character):
    if character.health <= 0:
        character.alive = False
        print(f"{character.name} has died.")
        distribute_inheritance(character)
        return True
    return False

def distribute_inheritance(character):
    if character.alive == False:
        heirs = ["Family", "Charity"]
        inheritance = random.choice(heirs)
        print(f"{character.name}'s assets are inherited by {inheritance}.")