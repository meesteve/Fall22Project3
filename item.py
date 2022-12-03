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
        self.open = False

    def open_up(self):
        if self.open:
            return False
        self.open = True
        return True
    
    def close_up(self):
        if self.open:
            self.open = False
            return True
        return False

    def get_item_by_name(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False

    def drop(self, item, target = None):
        target = target or self.loc
        self.items.remove(item)
        item.put_in_room(target)

    def add_item(self, item):
        self.items.append(item)
    
    def describe(self):
        clear()
        print(self.desc)
        if self.open:
            self.show_contents()
        else:
            print("It's locked.")
        input("Press enter to continue...")

    def show_contents(self):
        print("It contains the following:")
        for i in self.items:
            print(i.name)
        print()