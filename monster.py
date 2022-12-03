import random
import updater
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Monster:
    def __init__(self, name, health, room):
        self.name = name
        self.health = health
        self.room = room
        room.add_monster(self)
        updater.register(self)
        self.kind = 'Neutral'
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

class Enemy(Monster):
    def __init__(self, name, health, room):
        super().__init__(name, health, room)
        self.kind = 'Enemy'
    
    def update(self):
        if self.room.player != False:
            self.attack(self.room.player)
        else:
            super().update()

    def attack(self, player):
        clear()
        print(f"You are attacked by {self.name}!")
        input("Press enter to continue...")
        if player.asleep:
            print(f"As you are asleep, {self.name} fucking gets you.\nGet bodied moron.")
            input("Press enter to continue...")
            player.alive = False
        else:
            player.attack_monster(self)
        

# class Friend(Monster):