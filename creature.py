import random
import updater
import os
import item

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# generates name based on a number
# to give each creature a unique name
def num_to_name(n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['p', 't', 'k', 'b', 'gl', 'd', 'w', 'y', 's', 'f', 'j', 'l', 'x', 'c', 'v', 'n', 'm', 'st', 'br', 'bl']
    syll = [c + v for c in consonants for v in vowels]
    b = len(syll)
    ret = ''
    while n != 0:
        ret += syll[n%b]
        n //= b
    if len(ret) != 0:
        ret = ret[0].upper() + ret[1:]
    return ret


class Creature:
    # number given to creature to generate unique name
    number = 0
    def __init__(self, name, health, attack, room):
        Creature.number += 1
        self.name = num_to_name(Creature.number) + ' the ' + name
        self.health = health
        self.room = room
        self.atk = attack
        self.alive = True
        room.add_creature(self)
        updater.register(self)
        self.kind = 'Neutral'
        self.items = []
    # prints description of the creature
    def describe(self):
        clear()
        print(self.name)
        if self.items == []:
            print("They are not carrying any items.")
        else:
            print(f"{self.name} is currently carrying:")
            print()
            present = {}
            for i in self.items:
                if i.name in present.keys():
                    present[i.name] += 1
                else:
                    present[i.name] = 1
            for k in present.keys():
                print(f"{k} x {present[k]}")
        print()
        input("Press enter to continue...")
    # picks up specified item
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.room.remove_item(item)
    # drops specified item
    # if target is specified, puts specified item in target's inventory
    def drop(self, item, target = None):
        target = target or self.room
        self.items.remove(item)
        item.put_in_room(target)
    # removes item from inventory
    def remove_item(self, item):
        self.drop(item, None)
    # # drops all items
    def drop_all(self, target = None):
        while self.items != []:
            self.drop(self.items[0], target)
    # returns item of specified name, if found
    # returns false if not
    def get_item_by_name(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    # returns true if if inventory is not empty, returns false otherwise
    def has_items(self):
        return self.items != []
    # prints inventory
    def show_inventory(self):
        clear()
        print(f"{self.name} is currently carrying:")
        print()
        present = {}
        for i in self.items:
            if i.name in present.keys():
                present[i.name] += 1
            else:
                present[i.name] = 1
        for k in present.keys():
            print(f"{k} x {present[k]}")
        print()
        input("Press enter to continue...")
    # adds specified item to inventory
    def add_item(self, item):
        self.items.append(item)
    # updates self, goes to random room occasionally, picks up random item in room occasionally
    def update(self):
        if random.random() < .5:
            self.move_to(self.room.random_neighbor())
        if random.random() < .2 and self.room.has_items():
            self.pickup(self.room.random_item())
    # moves self to room
    def move_to(self, room):
        self.room.remove_creature(self)
        self.room = room
        room.add_creature(self)
    # dies
    def die(self):
        self.alive = False
        self.room.remove_creature(self)
        self.drop_all(self.room.player)
        updater.deregister(self)

# enemy type of creature
# has gold in inventory, that drops when killed
class Enemy(Creature):
    def __init__(self, name, health, attack, room):
        super().__init__(name, health, attack, room)
        self.kind = 'Enemy'
        self.items = [item.Gold("Gold", "Hunk of gold.") for _ in range(10)]
    # updates self, attacks player if player in room, else does default Creature behavior
    def update(self):
        if self.room.player:
            self.attack(self.room.player)
        else:
            super().update()
    # attacks player
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
                present = {}
                for i in mon.items:
                    if i.name in present.keys():
                        present[i.name] += 1
                    else:
                        present[i.name] = 1
                for k in present.keys():
                    print(f"{k} x {present[k]}")
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
        
# friend type of creature
# follows player around, can carry items
# attacks enemy creatures
class Friend(Creature):
    def __init__(self, name, health, attack, room):
        super().__init__(name, health, attack, room)
        self.kind = 'Friend'
    # follows player around, attacks enemy creatures
    def update(self):
        if self.room.player:
            for m in self.room.creatures:
                if m.kind == 'Enemy':
                    self.attack(m)
                    return None
        else:
            for r in self.room.exits:
                if r[1].player:
                    self.move_to(r[1])
                    return None
            super().update()
    # attacks enemy creatures
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
                present = {}
                for i in self.items:
                    if i.name in present.keys():
                        present[i.name] += 1
                    else:
                        present[i.name] = 1
                    self.drop(i, mon)
                for k in present.keys():
                    print(f"{k} x {present[k]}")
            self.die()
        else:
            print(f"{self.name}'s health is now {self.health}")
        if mon.health <= 0:
            print(f"{self.name} wins! {mon.name} is now dead.")
            if mon.has_items():
                print(f"{mon.name} had items!")
                print("They drop the following items:")
                present = {}
                for i in mon.items:
                    if i.name in present.keys():
                        present[i.name] += 1
                    else:
                        present[i.name] = 1
                for k in present.keys():
                    print(f"{k} x {present[k]}")
            mon.die()
        else:
            print(f"{mon.name}'s health is now {mon.health}.")
        print()
        input("Press enter to continue...")