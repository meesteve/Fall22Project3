import os
import updater
from random import *
from creature import *
from item import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Event:
    def __init__(self, odds, player, room = None, player_needed = False):
        self.odds = odds # number between 0 and 1, probability of occurence
        self.room = room
        self.player = player
        self.player_needed = player_needed
        updater.register(self)
    
    def update(self):
        if self.room != None:
            if self.player_needed:
                if self.player.location == self.room:
                    if random.random() < self.odds:
                        self.happen()
            else:
                if random.random() < self.odds:
                    self.happen()
        else:
            if random.random() < self.odds:
                self.happen()
    
    def happen(self): # this should be edited in other kinds of classes
        clear()
        print("You hear voices down the corridor.")
        print("You think you hear them say:")
        print('''"Welcome to the Hotel California"''')
        print('''"Such a lovely place (Such a lovely place)"''')
        print('''"Such a lovely face."''')
        print('''"Plenty of room at the Hotel California"''')
        print('''"Any time of year (Any time of year)"''')
        print('''"You can find it here."''')
        print()
        input("Press enter to continue...")

class SpawnSlime(Event):
    def happen(self):
        rand = random.random()
        if rand < .7:
            Creature("Green Slime", 20, 10, self.room)
        elif rand < .8:
            Enemy("Red Slime", 30, 10, self.room)
        else:
            Friend("Blue Slime", 30, 10, self.room)
        if self.room.player != False:
            clear()
            print("A slime has appeared!")
            if rand < .7:
                print("The slime is green. You can't read slime emotions.")
            elif rand < .8:
                print("The slime is red. You can't tell what it's thinking.")
            else:
                print("The slime is blue. You can't tell what it's thinking.")
            print()
            input("Press enter to continue...")

class SpawnChicken(Event):
    def happen(self):
        rand = random.random()
        if rand < .7:
            Creature("Speckled Chicken", 10, 30, self.room)
        elif rand < .8:
            Enemy("Orpington Chicken", 10, 30, self.room)
        else:
            Friend("Andalusian Chicken", 10, 30, self.room)
        if self.room.player != False:
            clear()
            print("A chicken has appeared!")
            if rand < .7:
                print("It's a speckled chicken! It doesn't seem interested in you.")
            elif rand < .8:
                print("It's an orpington chicken! It glares at you from across the room.")
            else:
                print("It's an andalusian chicken! It runs up to you and cuddles you!")
            print()
            input("Press enter to continue...")

class SpawnBear(Event):
    def happen(self):
        rand = random.random()
        if rand < .7:
            Creature("Normal Bear", 40, 40, self.room)
        elif rand < .8:
            Enemy("Mean Bear", 40, 40, self.room)
        else:
            Friend("Nice Bear", 40, 40, self.room)
        if self.room.player != False:
            clear()
            print("A bear has appeared!")
            if rand < .7:
                print("It's a normal bear. Leave it alone and it'll leave you alone.")
            elif rand < .8:
                print("It's a mean bear. It will attack you for fun.")
            else:
                print("It's a nice bear. It will help you fight.")
            print()
            input("Press enter to continue...")

class SpawnNugget(Event):
    def happen(self):
        rand = random.random()
        if rand < .9:
            i = Food("Chicken Nugget", "Chicken Nugget. You can eat this nugget! yumpy.", 8)
        else:
            i = Gold("Gold", "Gold nugget. You can't eat the nugget. Wrong kind.")
        i.put_in_room(self.room)

class Win(Event):
    def happen(self):
        if self.player.count_gold() >= 1000:
            self.player.alive = False
            clear()
            print("You win the game!")
            print("Congrats!")
            print()
            input("Press enter to end the game...")