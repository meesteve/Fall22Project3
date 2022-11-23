import random
import updater

class Monster:
    def __init__(self, name, health, room):
        self.name = name
        self.health = health
        self.room = room
        room.add_monster(self)
        updater.register(self)
    def update(self):
        if random.random() < .5:
            self.move_to(self.room.random_neighbor())
    def move_to(self, room):
        self.room.remove_monster(self)
        self.room = room
        room.add_monster(self)
    def die(self):
        self.room.remove_monster(self)
        updater.deregister(self)
