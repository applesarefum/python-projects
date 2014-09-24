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

print('Welcome to Battleship!')
#TODO ADD ASCII ART
#TODO ASK COMPUTER AI DIFFICULTY
#TODO PRINT GRID

w = '~'
row = [
    [' ',0,1,2,3,4,5,6,7,8,9,
    ['A',w,w,w,w,w,w,w,w,w,w]
    ['B',w,w,w,w,w,w,w,w,w,w]
    ['C',w,w,w,w,w,w,w,w,w,w]
    ['D',w,w,w,w,w,w,w,w,w,w]
    ['E',w,w,w,w,w,w,w,w,w,w]
    ['F',w,w,w,w,w,w,w,w,w,w]
    ['G',w,w,w,w,w,w,w,w,w,w]
    ['H',w,w,w,w,w,w,w,w,w,w]
    ['I',w,w,w,w,w,w,w,w,w,w]
]
grid[3][7] = "*"

for row in grid:
    for col in row:

carrier = Carrier()

start_row = input('In what row would you like you Carrier to be placed?').strip().lower()
start_col = input('In what column would you like you Carrier to be placed?').strip().lower()
direct = input('What direction shall it point? [N|S|F|W]').strip().lower()

#TODO sanity check on input values, loop asking again until valid
#TODO include checking occupied positions as invalid

carrier.location = 
