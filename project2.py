#table top RPG Character Creator
print("Welcome to the Table Top RPG Character Creator!")
import random

def get_name():
    return input("Enter your character's name: ")
# Simulate rolling 4 six-sided dice and dropping the lowest roll
def sum_of_four_six_sided_dice_with_lowest_dropped():
    rolls = []
    for i in range(4):
        rolls.append(random.randint(1, 6))

    rolls.remove(min(rolls))

    return sum(rolls)
# Calculate the ability modifier based on the ability score
def get_ability_modifier(score):
    return (score - 10) // 2
def display_menu():
    print("\nChoose an action:")
    print("1. Attack")
    print("2. Negotiate")
    print("3. Search")
    print("4. Eat")

    return input("Enter your choice: ")
def get_random_treasure():
    treasures = [
        "Gold Coins",
        "Magic Ring",
        "Silver Sword",
        "Ancient Scroll",
        "Jeweled Crown"
    ]

    return random.choice(treasures)
# Simulate an attack action using strength or dexterity modifier which ever is higher, and determine if the attack hits or 
# misses based on a d20 roll

def attack(str_mod, dex_mod):
    modifier = max(str_mod, dex_mod)
    roll = random.randint(1, 20)
    total = roll + modifier

    if total >= 12:
        damage = random.randint(1, 6) + modifier
        print(f"You rolled a {roll} and hit!")
        print(f"You dealt {damage} damage.")
    else:
        print(f"You rolled a {roll} and missed.")
# Simulate a negotiation action using charisma modifier and determine if the negotiation is successful based on a d20 roll        
def negotiate(charisma_mod):
    roll = random.randint(1, 20)
    total = roll + charisma_mod

    if total >= 15:
        print(f"You rolled a {roll}. Negotiation successful!")
    else:
        print(f"You rolled a {roll}. Negotiation failed.")
# Simulate a search action using intelligence or wisdom modifier which ever is higher, and determine if the search is 
# successful based on a d20 roll. If successful, randomly select a treasure from a predefined list and display it to the user.        
def search(int_mod, wis_mod):
    modifier = max(int_mod, wis_mod)

    roll = random.randint(1, 20)
    total = roll + modifier

    if total >= 12:
        treasure = get_random_treasure()
        print(f"You rolled a {roll} and found treasure!")
        print(f"Treasure: {treasure}")
    else:
        print(f"You rolled a {roll} and found nothing.")
# Simulate an eat action using constitution modifier and determine if the character gets sick based on a d20 roll. If the total
# is 10 or higher, the character does not get sick. If the total is less than 10, the character gets sick.        
def eat(con_mod):
    print("The food was bad.")

    roll = random.randint(1, 20)
    total = roll + con_mod

    if total >= 10:
        print(f"You rolled a {roll}. You don't get sick.")
    else:
        print(f"You rolled a {roll}. You get sick.")
# Main function to create a character, display the character sheet, and allow the user to choose actions to perform. The user can 
# choose to perform 4 actions, and after each action, the results are displayed based on the character's ability modifiers and 
# random rolls.        
def main():
    name = get_name()
    strength = sum_of_four_six_sided_dice_with_lowest_dropped()
    dexterity = sum_of_four_six_sided_dice_with_lowest_dropped()
    constitution = sum_of_four_six_sided_dice_with_lowest_dropped()
    intelligence = sum_of_four_six_sided_dice_with_lowest_dropped()
    wisdom = sum_of_four_six_sided_dice_with_lowest_dropped()
    charisma = sum_of_four_six_sided_dice_with_lowest_dropped()
    strength_mod = get_ability_modifier(strength)
    dexterity_mod = get_ability_modifier(dexterity)
    constitution_mod = get_ability_modifier(constitution)
    intelligence_mod = get_ability_modifier(intelligence)
    wisdom_mod = get_ability_modifier(wisdom)
    charisma_mod = get_ability_modifier(charisma)

    print("\n===== CHARACTER SHEET =====")
    print("Name:", name)
    print("\nAbility Scores")
    print("Strength:", strength)
    print("Dexterity:", dexterity)
    print("Constitution:", constitution)
    print("Intelligence:", intelligence)
    print("Wisdom:", wisdom)
    print("Charisma:", charisma)
    print("\nAbility Modifiers")
    print("Strength Mod:", strength_mod)
    print("Dexterity Mod:", dexterity_mod)
    print("Constitution Mod:", constitution_mod)
    print("Intelligence Mod:", intelligence_mod)
    print("Wisdom Mod:", wisdom_mod)
    print("Charisma Mod:", charisma_mod)
    print("\n===== ACTIONS =====")

    for i in range(4):
        choice = display_menu()
        if choice == "1":
            attack(strength_mod, dexterity_mod)
        elif choice == "2":
            negotiate(charisma_mod)
        elif choice == "3":
            search(intelligence_mod, wisdom_mod)
        elif choice == "4":
            eat(constitution_mod)
        else:
            print("Invalid choice.")
main()