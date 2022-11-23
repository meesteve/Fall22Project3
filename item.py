import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def put_in_room(self, room):
        self.loc = room
        room.add_item(self)
