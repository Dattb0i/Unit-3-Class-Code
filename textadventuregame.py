import random
import time
name = input("Enter your name: ")
def slow_print(text, delay=0.07):
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
slow_print("The world is in a crisis, energy is becoming harder and harder to come by and is going to run out worldwide in a few days.")
slow_print(f"You, {name}, have been set to the task of retrieving the fabled Nexus Crystal, an energy source that would allow the world to flourish once again.")
slow_print("In legend, the Nexus Crystal resided in a desolate cave, far from civilization, at the deepest point.")
slow_print("You must journey to this cave and find the crystal before the world shuts down.")
slow_print("Good luck,")
slow_print2(title_art)
