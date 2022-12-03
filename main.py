from room import *
from player import *
from item import *
from monster import *
import os
import updater
from fish import *

player = Player()

def create_world():
    a = Room("You are in a weird hotel lobby")
    b = Room("You are on the first floor of a weird hotel.\nIt's green!")
    c = Room("You are on the second floor of a weird hotel.\nIt's the color that you fail to see whenever you try to think up new colors!\nThe color could make Lovecraft less racist.")
    d = Room("You are on the third floor of a weird hotel.\nIt's blue!")
    e = Room("You are on the fourth floor of a weird hotel.\nIt's gay. Homosexual.")
    r = Room("You are on the roof of a weird hotel.\nYou look around you.\nThere is nothing that you can see.\nNothing at all.\nNo trees. No buildings. No stars.\nNo stars.\nNo stars.")
    hell = Room("You are in hell")
    Room.connect_rooms(a, "upstairs", b, "downstairs")
    Room.connect_rooms(b, "upstairs", c, "downstairs")
    Room.connect_rooms(c, "upstairs", d, "downstairs")
    Room.connect_rooms(d, "upstairs", e, "downstairs")
    Room.connect_rooms(e, "upstairs", r, "downstairs")
    i = Item("Note", "This is a note. You can't read what it says.\nFun fact! This is because you can't read.")
    i.put_in_room(b)
    balongadongas = Bed("Bed", "Comfy, comfy bed. Go eep in the bed.")
    balongadongas.put_in_room(a)
    hellbox = Container("Hellbox", "Box on fire. Maybe you should sleep in the box.")
    hellbox.put_in_room(hell)
    f = Food("Kronkle",'''This is kronkle, your favorite treat.\nYou remember when your grandmother would bake a kronkle for you.\n"Yonkle wonkle!", she would say. "Ihonkle gonkle fonkle yonkle."\nYou hardly need her encouragement now.\nYou are overcome by a lust for the kronkle.''', 12)
    f.put_in_room(d)
    player.location = a
    a.player = player
    Monster("Bonkle donkle", 20, b)
    Enemy("Johnny", 1, r)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_situation():
    clear()
    print(player.location.desc)
    print()
    if player.location.has_monsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.has_items():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exit_names():
        print(e)
    print()

def show_help():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("exit -- quits the game")
    print()
    input("Press enter to continue...")

def time_pass():
    updater.update_all()

if __name__ == "__main__":
    create_world()
    playing = True
    while playing and player.alive:
        print_situation()
        command_success = False
        time_passes = False
        while not command_success:
            command_success = True
            command = input("What now? ")
            if len(command) == 0:
                continue
            command_words = command.split()
            if len(command_words) == 0:
                continue
            match command_words[0].lower():
                case "go":   #cannot handle multi-word directions
                    okay = player.go_direction(command_words[1]) 
                    if okay:
                        time_passes = True
                    else:
                        print("You can't go that way.")
                        command_success = False
                case "pickup":  #can handle multi-word objects
                    target_name = command[7:] # everything after "pickup "
                    target = player.location.get_item_by_name(target_name)
                    if target != False:
                        player.pickup(target)
                    else:
                        print("No such item.")
                        command_success = False
                case "drop":  #can handle multi-word objects
                    target_name = command[5:] # everything after "pickup "
                    if target_name == 'all':
                        player.drop_all()
                    else:
                        target = player.get_item_by_name(target_name)
                        if target != False:
                            player.drop(target)
                        else:
                            print("No such item.")
                            command_success = False
                case "inspect":
                    target_name = command[8:]
                    target = player.get_item_by_name(target_name)
                    if target == False:
                        target = player.location.get_item_by_name(target_name)
                    if target != False:
                        target.describe()
                    else:
                        print("No such item.")
                        command_success = False
                case "sleep":
                    target_name = command[6:]
                    target = player.location.get_item_by_name(target_name)
                    if target != False:
                        if target.kind == 'Bed':
                            clear()
                            print("You fall into a dream.")
                            input("Press enter to continue...")
                            fish_game()
                            input("Press enter to continue...")
                            target.sleep(player)
                            for _ in range(3):
                                updater.update_all()
                        else:
                            print("That's not a bed!")
                            command_success = False
                    else:
                        print("No such item.")
                        command_success = False
                case "eat":
                    target_name = command[4:]
                    target = player.location.get_item_by_name(target_name)
                    if target != False:
                        if target.kind == 'Food':
                            player.eat(target)
                        else:
                            print("You can't eat that!")
                            command_success = False
                    else:
                        print("No such item.")
                        command_success = False
                case "inventory":
                    player.show_inventory()
                case "help":
                    show_help()
                case "wait":
                    time = 1
                    if len(command) > 4:
                        time = int(command[5:])
                    clear()
                    print("Some time has passed.")
                    input("Press enter to continue...")
                    player.asleep = True
                    for i in range(time):
                        updater.update_all()
                    player.asleep = False
                case "exit":
                    playing = False
                case "attack":
                    target_name = command[7:]
                    target = player.location.get_monster_by_name(target_name)
                    if target != False:
                        player.attack_monster(target)
                    else:
                        print("No such monster.")
                        command_success = False
                case "cry":
                    player.cry()
                case other:
                    print("Not a valid command")
                    command_success = False
        if time_passes == True:
            updater.update_all()




