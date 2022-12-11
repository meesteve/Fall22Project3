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
        self.alive = True
        room.add_creature(self)
        updater.register(self)
        self.kind = 'Neutral'
        self.items = []
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.room.remove_item(item)
    def drop(self, item, target = None):
        target = target or self.room
        self.items.remove(item)
        item.put_in_room(target)
    def drop_all(self, target = None):
        while self.items != []:
            self.drop(self.items[0], target)
    def get_item_by_name(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def has_items(self):
        return self.items != []
    def show_inventory(self):
        clear()
        print(f"{self.name} is currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")
    def add_item(self, item):
        self.items.append(item)
    def update(self):
        if random.random() < .5:
            self.move_to(self.room.random_neighbor())
        if random.random() < .2 and self.room.has_items():
            self.pickup(self.room.random_item())
    def move_to(self, room):
        self.room.remove_creature(self)
        self.room = room
        room.add_creature(self)
    def die(self):
        self.alive = False
        self.room.remove_creature(self)
        self.drop_all(self.room.player)
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
            if mon.has_items():
                print(f"{mon.name} had items!")
                print("They drop the following items:")
                for i in mon.items:
                    print(i.name)
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
        if self.health <= 0:
            print(f"{self.name} loses.")
            if self.has_items():
                print(f"{self.name} had items!")
                print("They drop the following items:")
                for i in self.items:
                    print(i.name)
                    self.drop(i, mon)
            self.die()
        else:
            print(f"{self.name}'s health is now {self.health}")
        if mon.health <= 0:
            print(f"{self.name} wins! {mon.name} is now dead.")
            if mon.has_items():
                print(f"{mon.name} had items!")
                print("They drop the following items:")
                for i in mon.items:
                    print(i.name)
            mon.die()
        else:
            print(f"{mon.name}'s health is now {mon.health}.")
        print()
        input("Press enter to continue...")