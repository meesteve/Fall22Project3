import random
import updater
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Creature:
    def __init__(self, name, health, attack, room):
        self.name = name
        self.health = health
        self.room = room
        self.atk = attack
        room.add_creature(self)
        updater.register(self)
        self.kind = 'Neutral'
    def update(self):
        if random.random() < .5:
            self.move_to(self.room.random_neighbor())
    def move_to(self, room):
        self.room.remove_creature(self)
        self.room = room
        room.add_creature(self)
    def die(self):
        self.room.remove_creature(self)
        updater.deregister(self)

class Enemy(Creature):
    def __init__(self, name, health, attack, room):
        super().__init__(name, health, attack, room)
        self.kind = 'Enemy'
    
    def update(self):
        if self.room.player != False:
            self.attack(self.room.player)
        else:
            super().update()

    def attack(self, player):
        mon = self
        clear()
        print(f"You are attacked by {self.name}!")
        input("Press enter to continue...")
        if player.asleep:
            print(f"As you are asleep, {self.name} fucking gets you.\nGet bodied moron.")
            player.health -= self.atk*3
            input("Press enter to continue...")
        else:
            print("Your health is " + str(self.health) + ".")
            print(f"Your attack is {self.atk}.")
            print(mon.name + "'s health is " + str(mon.health) + ".")
            print(f"{mon.name}'s attack is {mon.atk}.")
            print()
            player.health -= mon.atk
            mon.health -= self.atk
            print("You fight.")
        if mon.health <= 0:
            print(f"You win! {mon.name} is now dead.")
            mon.die()
        else:
            print(f"{mon.name}'s health is now {mon.health}.")
        if player.health <= 0:
            print("You lose.")
            player.alive = False
        else:
            print(f"Your health is now {player.health}")
        print()
        input("Press enter to continue...")
        

class Friend(Creature):
    def __init__(self, name, health, attack, room):
        super().__init__(name, health, attack, room)
        self.kind = 'Friend'
    
    def update(self):
        if self.room.player != False:
            for m in self.room.creatures:
                if m.kind == 'Enemy':
                    self.attack(m)
                    return None
        else:
            for r in self.room.exits:
                if r[1].player != False:
                    self.move_to(r[1])
                    return None
            super().update()
    
    def attack(self, enemy):
        mon = enemy
        clear()
        print(f"{self.name} attacks {enemy.name}!")
        print(f"{self.name}'s health is {self.health}")
        print(f"{self.name}'s attack is {self.atk}.")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print(f"{mon.name}'s attack is {mon.atk}.")
        print()
        self.health -= mon.atk
        mon.health -= self.atk
        print("They fight.")
        if mon.health <= 0:
            print(f"{self.name} wins! {mon.name} is now dead.")
            mon.die()
        else:
            print(f"{mon.name}'s health is now {mon.health}.")
        if self.health <= 0:
            print(f"{self.name} loses.")
            self.die()
        else:
            print(f"{self.name}'s health is now {self.health}")
        print()
        input("Press enter to continue...")