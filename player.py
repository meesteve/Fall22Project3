import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.health = 50
        self.alive = True
        self.cry_count = 0
    # goes in specified direction if possible, returns True
    # if not possible returns False
    def cry(self):
        self.cry_count += 1
        clear()
        print("You cry.")
        print()
        if self.cry_count > 5:
            print('Your eyes are starting to feel dry.')
            print()
        if self.cry_count > 50:
            print('You are starting to feel dehydrated.\nMaybe you should stop crying so much.')
            print()
        if self.cry_count > 90:
            print('You feel you are dying of thirst!\nAll the water in your body is exiting through your eyes!')
            print()
        if self.cry_count > 100:
            print('All the water in your body is gone!\nYour body no longer has enough water to function.')
            print()
            print('You lose.')
            self.alive = False
        print()
        input("Press enter to continue...")
    def go_direction(self, direction):
        new_location = self.location.get_destination(direction.lower())
        if new_location is not None:
            self.location = new_location
            return True
        return False
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.remove_item(item)
    def show_inventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")
    def attack_monster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
        if self.health > mon.health:
            self.health -= mon.health
            print("You win. Your health is now " + str(self.health) + ".")
            mon.die()
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")

