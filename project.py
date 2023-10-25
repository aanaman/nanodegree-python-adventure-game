import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(enemy, weapon):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is "
                "somewhere around here, and has "
                "been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your trusty "
                f"(but not very effective) {weapon}.")


def fight(enemy, weapon):
    win_or_lose = random.choice(['win', 'lose'])
    if win_or_lose == 'win':
        win(enemy)
    else:
        lose(enemy, weapon)


def run(enemy, weapon, cave_entry):
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.")
    field(enemy, weapon, cave_entry)


def cave(enemy, weapon, cave_entry):
    print_pause("You peer cautiously into the cave.")
    if cave_entry == []:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        cave_entry.append('entered')
    else:
        print_pause("You've been here before, and "
                    "gotten all the good stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field.")
    field(enemy, weapon, cave_entry)


def house(enemy, weapon, cave_entry):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the "
                f"door opens and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    print_pause(f"You feel a bit under-prepared for this, "
                f"what with only having a tiny {weapon}.")
    print_pause("Would you like to (1) fight or (2) run away?")
    choice = input()
    if choice == '1':
        fight(enemy, weapon)
        play_again()
    elif choice == '2':
        run(enemy, weapon, cave_entry)
    else:
        print_pause("Sorry, I don't understand. Please try again.")
        house(enemy, weapon, cave_entry)


def win(enemy):
    print_pause(f"As the {enemy} moves to attack, "
                "you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly "
                "in your hand as you brace "
                "yourself for the attack.")
    print_pause(f"But the {enemy} takes one look "
                "at your shiny new toy and runs away!")
    print_pause(f"You have rid the town of the {enemy}. You are victorious!")
    play_again()


def lose(weapon, enemy):
    print_pause("You do your best...")
    print_pause(f"but your {weapon} is no match for the {enemy}.")
    print_pause("You have been defeated!")
    play_again()


def play_again():
    print_pause("Would you like to play again? (y/n)")
    again = input().lower()
    if again == 'y':
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif again == 'n':
        print_pause("Thanks for playing! See you next time.")
        exit()
    else:
        print_pause("Sorry, I don't understand. Please try again.")
        play_again()


def field(enemy, weapon, cave_entry):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    print_pause("(Please enter 1 or 2.)")
    choice = input()
    if choice == '1':
        house(enemy, weapon, cave_entry)
    elif choice == '2':
        cave(enemy, weapon, cave_entry)
    else:
        print_pause("Sorry, I don't understand. Please try again.")
        field(enemy, weapon, cave_entry)


def play_game():
    enemy = random.choice(['python', 'lion', 'dragon',
                           'leopard', 'gorgon', 'bear'])

    weapon = random.choice(['sword', 'gun', 'axe',
                            'bow and arrow', 'spear', 'machete'])

    cave_entry = []
    intro(enemy, weapon)
    field(enemy, weapon, cave_entry)


play_game()
