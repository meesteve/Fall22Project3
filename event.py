import os
import updater
import random
import creature
import item

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# event
class Event:
    def __init__(self, odds, player, room = None, player_needed = False):
        self.odds = odds # number between 0 and 1, probability of occurence
        self.room = room
        self.player = player
        self.player_needed = player_needed
        updater.register(self)
    # updates event if less than odds
    def update(self):
        if self.room is not None:
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
    # actual thing that happens
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
# specific event that spawns slimes
class SpawnSlime(Event):
    # spawns slime, can be of type friend, enemy, or neutral
    def happen(self):
        rand = random.random()
        if rand < .7:
            creature.Creature("Green Slime", 60, 5, self.room)
        elif rand < .8:
            creature.Enemy("Red Slime", 60, 5, self.room)
        else:
            creature.Friend("Blue Slime", 80, 5, self.room)
        if self.room.player:
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
# specific event that spawns chicken
class SpawnChicken(Event):
    # spawns chicken, can be of type friend, enemy, or neutral
    def happen(self):
        rand = random.random()
        if rand < .7:
            creature.Creature("Speckled Chicken", 20, 15, self.room)
        elif rand < .8:
            creature.Enemy("Orpington Chicken", 20, 15, self.room)
        else:
            creature.Friend("Andalusian Chicken", 40, 15, self.room)
        if self.room.player:
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
# specific event that spawns bears
class SpawnBear(Event):
    # spawns bear, can be of type friend, enemy, or neutral
    def happen(self):
        rand = random.random()
        if rand < .7:
            creature.Creature("Normal Bear", 40, 10, self.room)
        elif rand < .8:
            creature.Enemy("Mean Bear", 40, 10, self.room)
        else:
            creature.Friend("Nice Bear", 60, 10, self.room)
        if self.room.player:
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
# spawns nuggets
class SpawnNugget(Event):
    def happen(self):
        rand = random.random()
        if rand < .9:
            i = item.Food("Chicken Nugget", "Chicken Nugget. You can eat this nugget! yumpy.", 8)
        else:
            i = item.Gold("Gold", "Gold nugget. You can't eat the nugget. Wrong kind.")
        i.put_in_room(self.room)
# wins the game
class Win(Event):
    def happen(self):
        if self.player.count_gold() >= 500:
            self.player.alive = False
            clear()
            print("You win the game!")
            print("Congrats!")
            print()
            input("Press enter to end the game...")