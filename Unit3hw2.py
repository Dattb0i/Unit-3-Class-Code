print("Your mind feels fuzzy as you awaken on a hard stone floor.")
print("There are 2 pathways, one to your right, and one to your left.")
print(f"1. Head left\n2. Head right\n.")
decision = int(input("--> " ))
if decision == 1:
    print("The new room that awaits you contains a pit of lava with platforms to jump between.")

elif decision == 2:
    print("The right side was a trap, the floor collapses beneath you and you fall to your death.")

else:
    print("You stood thinking too long and got crushed by a spike.")