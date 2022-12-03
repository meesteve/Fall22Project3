import os
import updater
from random import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Event:
    def __init__(self, odds, player, room = None):
        self.odds = odds # number between 0 and 1, probability of occurence
        self.room = room
        self.player = player
        updater.register(self)
    
    def update(self):
        if self.room != None:
            if self.player.location == self.room:
                if random() < self.odds:
                    self.happen()
        else:
            if random() < self.odds:
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


