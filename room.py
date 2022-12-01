import random

class Room:
    def __init__(self, description):
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
    def add_exit(self, exit_name, destination):
        self.exits.append([exit_name, destination])
    def get_destination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
        return None
    def connect_rooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.add_exit(dir1, room2)
        room2.add_exit(dir2, room1)
    def exit_names(self):
        return [x[0] for x in self.exits]
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def add_monster(self, monster):
        self.monsters.append(monster)
    def remove_monster(self, monster):
        self.monsters.remove(monster)
    def has_items(self):
        return self.items != []
    def get_item_by_name(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def has_monsters(self):
        return self.monsters != []
    def get_monster_by_name(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False
    def random_neighbor(self):
        return random.choice(self.exits)[1]