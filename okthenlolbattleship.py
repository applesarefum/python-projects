class Ship():
    size = None

class Carrier(Ship):
    size = 5

class Battleship(Ship):
    size = 4

class Submarine(Ship):
    size = 3

class Destroyer(Ship):
    size = 3

class Patrol_Boat(Ship):
    size = 2
#-----------------------------------------

print('Welom to Battleship!')
#TODO ADD ASCII ART
#TODO ASK COMPUTER AI DIFFICULTY
#TODO PRINT GRID

grid = [['~ ' * 10] * 10]

for row in grid:
    fir col in row:

carrier = Carrier()

start_row = input('In what row would you like you Carrier to be placed?').strip().lower()
start_col = input('In what column would you like you Carrier to be placed?').strip().lower()
direct = input('What direction shall it point? [N|S|F|W]').strip().lower()

#TODO sanity check on input values, loop asking again until valid
#TODO include checking occupied positions as invalid

carrier.location = 
