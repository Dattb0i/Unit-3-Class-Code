import random
import time
score = 0
def slow_print(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def slow_print2(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
title_art = r'''   ___                     ___               _ _           
  / __\__ ___   _____     /   \__      _____| | | ___ _ __ 
 / /  / _` \ \ / / _ \   / /\ /\ \ /\ / / _ \ | |/ _ \ '__|
/ /__| (_| |\ V /  __/  / /_//  \ V  V /  __/ | |  __/ |   
\____/\__,_| \_/ \___| /___,'    \_/\_/ \___|_|_|\___|_|   
'''
slow_print("The world is in a crisis, energy is becoming harder anda harder to come by and is going to run out worldwide in a few days.")
slow_print(f"You, {input("Enter your name: ")}, have been set the task of retrieving the fabled Nexus Crystal, an energy source that would allow the world to flourish once again.")
slow_print("In legend, the Nexus Crystal resided in a desolate cave far from civilization, at the deepest point.")
slow_print("You must journey to this cave and find the crystal before the world shuts down for good.")
slow_print("Good luck,")
slow_print2(title_art)
print()
while True:
    game_start = int(input("Ready to play?\nyes(1) no(2)"))
    if game_start == 1:
        break
    if game_start == 2:
        exit()
print()
print()
slow_print("As you approach the cave entrance, you take note of what you have with you: ")
slow_print("A flashlight\nA helmet\nA med kit")
slow_print("You take a few steps inside, turn on your flashlight, and see that there are two pathways you could take.\nRight(1) or left(2)?")
while True:
    try:
        way = int(input("Which way?"))
    except ValueError:
        print("Enter either right(1) or left(2)")
        continue
    if way == 1:
        slow_print("You continue down the right path, and come across a large underground lake.")
        slow_print("You notice a set of diving gear lying by the lakeside, do you pick it up(1) or leave it(2)?")
        while True:
            try:
                way11 = int(input("What do you do?"))
            except ValueError:
                print("Enter either yes(1) or no(2)")
                continue
            if way11 == 1:
                slow_print("You pick up the diving gear and start putting it on, preparing to dive into the lake.")
                slow_print("You get the helmet's light working, and swap your own for it,\nturning your flashlight off and storing it in the waterproof bag you found.")
                slow_print("As you dive in, your helmet's light flickers off, and as you try to swim to the surface,\nthe giant cave fish lying in wait swims toward you and eats you in one bite.\nGame Over")
                exit()
            if way11 == 2:
                ...      
    if way == 2:
        slow_print("You walk toward the left side and continue until you reach a large cave full of stalactites.")
        chance_to_get_hit = random.randint(1,80)
        if chance_to_get_hit == 34:
            slow_print("You take off your helmet to scratch your head, and a stalactite falls on you.\nGame Over")
            exit()
        slow_print("You look around and see that the cave stretches onward for a while, with a large dropoff on your right.\nDo you go forward(1) or look over the side(2)?")
        while True:
            try:
                way22 = int(input("What do you do?"))
            except ValueError:
                print("Enter what you want to do: forward(1) or look over the side(2)")
                continue
            if way22 == 1:
                ...
            if way22 == 2:
                slow_print("You decide to peek over the edge of the dropoff,")


