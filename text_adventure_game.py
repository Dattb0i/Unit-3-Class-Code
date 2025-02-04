'''
Name: August Doe
Date: 1/20/25
Description: Text Adventure Game
'''
import random
import time
#These lines make the code slowly type itself out
def slow_print(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def slow_print2(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
#ASCII art for the title
title_art = r'''   ___                     ___               _ _           
  / __\__ ___   _____     /   \__      _____| | | ___ _ __ 
 / /  / _` \ \ / / _ \   / /\ /\ \ /\ / / _ \ | |/ _ \ '__|
/ /__| (_| |\ V /  __/  / /_//  \ V  V /  __/ | |  __/ |   
\____/\__,_| \_/ \___| /___,'    \_/\_/ \___|_|_|\___|_|   
'''
# Main story
slow_print("The world is in a crisis, the sun is growing weaker and energy is becoming harder to come by.")
slow_print("Energy will run out worldwide in a few days, so you must move fast.")
slow_print(f"You, {input("Enter your name: ")}, have been set the task of retrieving the fabled Nexus Crystal, an energy source that would flood the world with plenty of energy once again.")
slow_print("In legend, the Nexus Crystal resided in a desolate cave far from civilization, at the deepest point.")
slow_print("You must journey to this cave and find the crystal before the world goes dark forever.")
slow_print("Good luck,")
slow_print2(title_art)
print()
#score tracker
def score_tracker():
    score_tracker.counter -= 1
score_tracker.counter = 0
def game_restart():
    game_restart1 = int(input("Want to play again? yes(1) no(2)"))
    if game_restart1 == 1:
        game()
    if game_restart1 == 2:
        exit() 
#shroom random generator
def rando_shroom():
    super_shroom_count = 0
    shroom_safeness = random.randint(1,3)
    if shroom_safeness > 1:
        slow_print("You picked a poisonous mushroom that paralyzes you, good luck getting out now!\n Game Over")
        score_tracker()
        game_restart()
    if shroom_safeness == 1:
        slow_print("You picked a non-deadly mushroom that may be handy later on.")
        super_shroom_count += 1
#chest opening scene
def chest_opening():
    slow_print("You open the chest, and toxic gas fumes spill out of it.")
    while True:
        try:
            chest_decision = int(input("Do you run back into the previous cave(1) or dash through to the exit of this cave(2)?"))
        except ValueError:
            print("Decide to run back(1) or run forward(2)")
            continue
        if chest_decision == 1:
            slow_print("You make a break for it towards the back of the cave, and just barely make it out.")
            slow_print("After waiting for the poison to dissipate, you continue through the cave.")
            break
        if chest_decision == 2:
            slow_print("You try to run forward, but the gas has spread too fast and you die from the fumes.\nGame Over")
            score_tracker()
            game_restart()
#The final room
def endgame():
    while True:
        try:
            door_choice = int(input("What door do you think houses the Crystal? (1), (2), or (3)?"))
        except ValueError:
            print("Enter either (1) (2) or (3)")            
        if door_choice == 1:
            slow_print("You open the first door and walk inside, only for the door to slam shut and the walls to start closing in, crushing you.\nGame Over")
            score_tracker()
            game_restart()
        if door_choice == 2:
            slow_print("You open the second door and are greeted by a raging inferno that spreads quickly, roasting you to a crisp.\nGame Over")
            score_tracker()
            game_restart()
        if door_choice == 3:
            slow_print("You open the third door and are blinded by the light of the Nexus Crystal!\nYou have saved the world from a dark future, all thanks to your wit and survival instincts.\nGood game, and thanks for playing!")
            slow_print(f"Your final score was {score_tracker.counter}.")
            game_restart()
#full game
def game():
    count = 0
    super_shroom_count = 0
    print("The goal here is to complete the game whilst having the least points possible.")
    print()
    slow_print("As you approach the cave entrance, you take a deep breath, preparing yourself for whatever lies ahead.")
    slow_print("You take a few steps inside, turn on your flashlight, and see that there are two pathways you could take.\nRight(1) or left(2)?")
    while count == 0:
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
                    score_tracker()
                    game_restart()
                if way11 == 2:
                    slow_print("You decide to leave the gear behind and keep moving around the lake until you reach a large circular cave full of glowing mushrooms.")
                    slow_print("Do you want to pick one up or continue onward?")
                    while True:
                        try:
                            shroom = int(input("Pick up? yes(1) no(2)"))   
                        except ValueError:
                            print("Enter either yes(1) or no(2)")  
                            continue
                        if shroom == 2:
                            break
                        if shroom == 1:
                            rando_shroom()
                            super_shroom_count += 1
                            break
                        else:
                            print("Invalid input, type in either: (1) or (2)")
                            continue
                else:
                    print("Invalid input, type in either: (1) or (2)")
                    continue
                break
        count += 1
        if way == 2:
            slow_print("You walk toward the left side and continue until you reach a large cave full of stalactites.")
            chance_to_get_hit = random.randint(1,80)
            if chance_to_get_hit == 34:
                slow_print("You take off your helmet to scratch your head, and a stalactite falls on you.\nGame Over")
                score_tracker()
                game_restart()
            slow_print("You look around and see that the cave stretches onward for a while, with a large dropoff on your right.\nDo you go forward(1) or look over the dropoff(2)?")
            while True:
                try:
                    way22 = int(input("What do you do?"))
                except ValueError:
                    print("Enter what you want to do: move forward(1) or look over the side(2)")
                    continue
                if way22 == 2:
                    slow_print("You decide to peek over the edge of the dropoff, but just as you reach the edge, the ground collapses beneath you, plummenting you to your doom.\nGame Over")
                    score_tracker()
                    game_restart()
                if way22 == 1:
                    slow_print("You travel farther into the cave and come across a room with a rusted old chest in the center.")
                    while True:
                        try:
                            chest = int(input("Will you open(1) or not open(2)"))
                        except ValueError:
                            print("Enter either open(1) or not open(2)")
                            continue
                        if chest == 2:
                            break
                        if chest == 1:
                            chest_opening()
                            break
                        else:
                            print("Invalid input, type in either: (1) or (2)")
                            continue
                else:
                    print("Invalid input, type in either: (1) or (2)")
                    continue
                break
        else:  
            print("Invalid input, type in either: (1) or (2)")
            continue         
        break
    slow_print("You walk into a large cavern that contains three doors, with large words above them.")
    slow_print("The lettering above the doors reads:\nThe Crystal is behind one of these three doors, and you must decide which of them is lying to you, and which are telling the truth(if any).")
    ready = int(input("Type '1' when ready to start."))
    while True:
        if ready == 1:
            slow_print("The sign by the first door reads:\nDoor two is telling the truth.")
            ready2 = int(input("Type '1' when ready to move on."))
            if ready2 == 1:
                slow_print("The sign by the second door reads:\nI have the Crystal.")
                ready3 = int(input("Type '1' when ready to move on."))
                if ready3 == 1:
                    slow_print("The sign by the third door reads:\nBoth doors are telling the truth. Also, door one has the Crystal behind its door.")
                    if super_shroom_count == 1:
                        slow_print("You have a super shroom! It's allowed you to tell that door two is lying.")
                    readyfr = int(input("Type '1' when ready to answer."))
                    if readyfr == 1:
                        break
    endgame()
#Starting input
while True:
    game_start = int(input("Ready to play?\nyes(1) no(2)"))
    if game_start == 1:
        game()
    if game_start == 2:
        exit() 


