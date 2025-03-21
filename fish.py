import os
import random
import math

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fish_game():
    def print_situation():
        clear()
        print("You are a salmon! There's a salmon run going on.")
        print("Your objective is to have as many children as possible.")
        print("The number of children have is influenced by how far you are up the river.")
        print("However, \x1B[3mbear\x1B[0m in mind that there may be some dangers up the river.")
        print()
        player.print_description()
        print()
    def show_help():
        clear()
        print("swim -- lets you swim")
        print("reproduce -- you reproduce")
        print("exit -- quits the game")
        print("kids -- looks at your children")
        print()
        input("Press enter to continue...")
    class Player:
        def __init__(self):
            self.name = 'Setanta'
            self.health = 100
            self.distance = 0
            self.alive = True
            self.children = []
        def cry(self):
            clear()
            print("You're a fish.")
            print("You can't cry.\n")
            input("Press enter to continue...")
        def swim(self):
            dist = random.randint(15,25)
            self.distance += dist
            clear()
            print(f"You swim {dist} meters upstream.")
            print()
            if random.random() < 0.1/(1+math.e**(-0.001*(self.distance-2000))):
                print("You've been eaten by a bear!")
                self.health = 0
            if self.health <= 0:
                print('You are dead.')
                if len(self.children) == 0:
                    input('And what do you have to show for it?')
                    input('Did you just swim this entire time?')
                    input('Did you not read what it said at the top?')
                    input('Let me rehash it for you.')
                    input("'Your objective is to have as many children as possible', I said.")
                    input("You didn't read that, did you?")
                    input("Can you read at all?")
                    input("Well, you're dead now anyway.")
                self.alive = False
            input('Press enter to continue...')
        def reproduce(self):
            kids = 0
            for i in range(int(self.distance ** 0.3)):
                kids += random.randint(0, 5)
            clear()
            if kids == 0:
                print('You failed to have children.\nYou are a horrible salmon.')
            else:
                print(f'You had {kids} children!', end = ' ')
                if kids < 10:
                    print('Not a very successful salmon.')
                if kids > 20:
                    print('Very successful salmon! Get it!')
                else:
                    print('Normal salmon behavior.')
            if kids != 0:
                input('Press enter to continue...')
                clear()
                print("You've had kids! Would you like to name any of them?")
                conf = 'a'
                _ = 0
                while conf not in ['y', 'n', 'yes', 'no']:
                    conf = input("Enter 'y' or 'n' to select a response: ")
                if conf in ['y', 'yes']:
                    for i in range(kids):
                        clear()
                        input('Why? Why are you doing this?')
                        name = input("Name your child: ")
                        self.children.append(name)
                        print("Name another?")
                        conf = 'a'
                        while conf not in ['y', 'n', 'yes', 'no']:
                            conf = input("Enter 'y' or 'n' to select a response: ")
                        if conf in ['n', 'no']:
                            _ = i
                            break
                    for i in range(kids - _):
                        self.children.append(f"salmon{len(self.children)}")
                else:
                    for i in range(kids):
                        self.children.append(f"salmon{len(self.children)}")
            self.health -= 1 + kids
            if self.health <= 0:
                self.alive = False
                print("You are dead. You fucked too hard.")
            input('Press enter to continue...')
        def print_description(self):
            if self.distance == 0:
                print("You are in the ocean still.")
                print("You can tell that you won't be able to have children here.")
            else:
                print(f"You are {self.distance} meters into the river.")
                print(f"You will be able to have {int(self.distance**0.3)} group{'s' if int(self.distance**0.3) != 1 else ''} of children")
                if self.distance >= 1517:
                    print("Going any further won't provide much benefit on your ability to have children.")
            print(f"You have {len(self.children)} kid{'s' if len(self.children) != 1 else ''}.")
            print(f"You have {self.health} hit points.")
        def look_at_kids(self):
            clear()
            if len(self.children) == 0:
                print("You don't have any children!")
            for k in self.children:
                input(f"Look at your beautiful child, {k}")
            input("\nPress enter to continue...")
    player = Player()
    playing = True
    while playing and player.alive:
        print_situation()
        command_success = False
        while not command_success:
            command_success = True
            command = input("What now? ")
            if len(command) == 0:
                continue
            match command.lower():
                case "swim":
                    player.swim()
                case "fuck":
                    player.reproduce()
                case "reproduce":
                    player.reproduce()
                case "cry":
                    player.cry()
                case "help":
                    show_help()
                case "exit":
                    playing = False
                case "kids":
                    player.look_at_kids()
                case _:
                    clear()
                    print("Not a valid command!\n")
                    input("Press enter to continue...")
    print(f"\nYou had {len(player.children)} kid{'s' if len(player.children) != 1 else ''}")