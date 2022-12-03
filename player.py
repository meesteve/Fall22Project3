import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.health = 50
        self.atk = 7
        self.alive = True
        self.cry_count = 0
        self.asleep = False
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
            self.location.player = False
            self.location = new_location
            self.location.player = self
            return True
        return False
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.remove_item(item)
    def drop(self, item, target = None):
        target = target or self.location
        self.items.remove(item)
        item.put_in_room(target)
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
    def pet_creature(self, mon):
        clear()
        print(f"You are petting {mon.name}")
        if mon.kind == 'Friend':
            print(f"{mon.name} loves it! You can see them wagging their little tail.\nOr... no, wait, {mon.name} doesn't have a tail.\nWhat are you seeing? How can you tell that they're happy?\nHow do you know what's even real?\nWell, you can tell that {mon.name} is happy.\nExistential crisis postponed because ohmigosh they're so cuuuuuuteeeeeee~\n")
            print(f"Both you and {mon.name} gain hitpoints.")
            self.health += mon.atk
            mon.health += self.atk
        else:
            print(f"{mon.name} is hating this. They are scared of you.")
        input("Press enter to continue...")
    def show(self):
        clear()
        print("You sure have an appearance.")
        print(f"You have a height for sure, a hair color certainly.\nCan't forget eyes.{' They are looking rather red.' if self.cry_count > 10 else ''} All the usual limbs.")
        print(f"You have {self.health} health.")
        print(f"You have {self.atk} attack.")
        for c in self.location.creatures:
            if c.kind == 'Friend':
                print("You have a little friend!")
                print(f"{c.name} is your friend!")
        print()
        input("Press enter to continue...")
    def add_item(self, item):
        self.items.append(item)
    def attack_creature(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(f"Your attack is {self.atk}.")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print(f"{mon.name}'s attack is {mon.atk}.")
        print()
        if mon.kind != 'Friend':
            self.health -= mon.atk
        mon.health -= self.atk
        print("You fight. Your health is now " + str(self.health) + ".")
        if mon.kind == 'Friend':
            print(f"{mon.name} doesn't fight back.")
            print(f"{mon.name} is your friend.")
        if mon.health <= 0:
            print(f"You win! {mon.name} is now dead.")
            if mon.kind == 'Friend':
                print("Are you proud of yourself? Are you happy?")
                print(f"All {mon.name} wanted was to be your friend.")
            mon.die()
        else:
            print(f"{mon.name}'s health is now {mon.health}.")
        if self.health <= 0:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")

