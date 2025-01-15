import random
def buy_asset(character, asset_name, cost):
    if character.money >= cost:
        character.money -= cost
        character.assets.append(asset_name)
        print(f"You bought a {asset_name} for ${cost}.")
    else:
        print(f"You don't have enough money to buy a {asset_name}.")

def sell_asset(character, asset_name, value):
    if asset_name in character.assets:
        character.assets.remove(asset_name)
        character.money += value
        print(f"You sold your {asset_name} for ${value}.")
    else:
        print(f"You don't own a {asset_name}.")