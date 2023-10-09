import random

tries = 100
doors = ['goat', 'goat', 'car']
outcome = [0, 0, 0, 0] # 1. wins after change 2. losses after change 3. wins after not change 4. losses after not change

while tries > 0:
    random.shuffle(doors)
    change = random.randint(0,1) # change or not to change?
    # chose first door
    if doors[1] == 'goat': # open the second door and show the goat
        if change: # if change the door
            if doors[2] == 'car':
                outcome[0] += 1
            else:
                outcome[1] += 1
        else:
            if doors[0] == 'car':
                outcome[2] += 1
            else:
                outcome[3] += 1
    else: # open the third door and show the goat
        if change: # if change the door
            outcome[0] += 1
        else:
            outcome[3] += 1

    tries -= 1

print("Wins after switch = " + str(outcome[0]))
print("\nLosses after switch = " + str(outcome[1]))
print("\nWins after staying = " + str(outcome[2]))
print("\nLosses after staying = " + str(outcome[3]))