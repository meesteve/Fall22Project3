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
        if self.cry_count > 5:
            print('Your eyes are starting to feel dry.')
        if self.cry_count > 50:
            print('You are starting to feel dehydrated.\nMaybe you should stop crying so much.')
        if self.cry_count > 90:
            print('You feel you are dying of thirst!\nAll the water in your body is exiting through your eyes!')
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
    def drop(self, item):
        self.items.remove(item)
        item.put_in_room(self.location)
    def drop_all(self):
        while self.items != []:
            self.drop(self.items[0])
    def gain_hp(self, hp):
        self.health += hp
    def eat(self, item):
        self.health += item.nv
        if item in self.items:
            self.items.remove(item)
        if item in self.location.items:
            self.location.items.remove(item)
        clear()
        print(f"You slurp {item.name} up. Slurpity slurp slurp slurp. Sluuuurrrrrrp. Fuck, that tastes {'good' if item.nv > 0 else 'awful'}. Who knows where it goes.")
        print()
        input("Press enter to continue...")
    def get_item_by_name(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
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

