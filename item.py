import os
from random import randint

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None
        self.kind = 'Generic'
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def put_in_room(self, room):
        self.loc = room
        room.add_item(self)

class Bed(Item):
    def __init__(self, name, desc):
        super().__init__(name, desc)
        self.kind = 'Bed'
    def sleep(self, player):
        hp = sum([randint(0,3) for _ in range(10)])
        player.gain_hp(hp)
        clear()
        print("You've ept! Hope you had a good eep.")
        print(f"You've regenerated {hp} hitpoints!")
        print()
        input("Press enter to continue...")

class Food(Item):
    def __init__(self, name, desc, nutrition_value):
        super().__init__(name, desc)
        self.kind = 'Food'
        self.nv = nutrition_value

class Container(Item):
    def __init__(self, name, desc):
        super().__init__(name, desc)
        self.kind = 'Container'
        self.items = []

    def show_contents(self):
        print(self.desc)
        print("It contains the following:")
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")