from sense_hat import SenseHat
from time import sleep
from random import randint
import time
from copy import deepcopy
sense = SenseHat()

# Constants
b=(0,0,0)
w=(255,255,255)
r=(255,0,0)
blue = (0,0,255)

# This function checks the pitch value and the x coordinate
# to determine whether to move the marble in the x-direction.
# Similarly, it checks the roll value and y coordinate to
# determine whether to move the marble in the y-direction.
def move_marble(pitch,roll,x,y):
    new_x = x #assume no change to start with
    new_y = y #assume no change to start with
    if 1 < pitch < 179 and x != 0:
        new_x -= 1 # move left
    elif 359 > pitch > 179 and x != 7:
        new_x += 1 # move right
    if 1 < roll < 179 and y != 7:
        new_y += 1 # move up
    elif 359 > roll > 179 and y != 0:
        new_y -= 1 # move down
    return new_x, new_y

# Ensures marble pos is not within the walls
def check_wall(x,y,new_x,new_y):
    if board[new_y][new_x] != r:
        return new_x, new_y
    elif board[new_y][x] != r:
        return x, new_y
    elif board[y][new_x] != r:
        return new_x, y
    else:
        return x,y

# Checks if target pos is achieved
def checkTarget(x,y,target_x,target_y):
    if(target_x==x and target_y==y):
        print('Target reached!')
        return True
    else:
        return False

# Create random maze where n = no. of blocks (less wall tiles)
def generateMaze(n):
    maze = [[r,r,r,r,r,r,r,r],
             [r,b,b,b,b,b,b,r],
             [r,b,r,b,b,r,b,r],
             [r,b,b,b,b,r,b,r],
             [r,b,b,b,b,b,b,r],
             [r,b,r,b,b,b,b,r],
             [r,b,b,b,b,b,b,r],
             [r,r,r,r,r,r,r,r] ]
    for i in range(n):
        i = randint(1,6)
        j = randint(1,6)
        while(maze[j][i]==r):
            i = randint(1,6)
            j = randint(1,6)
        maze[j][i] = r

    return maze

def seed(maze):
    i,j = randint(1,6),randint(1,6)
    while(maze[j][i]==r):
        i = randint(1,6)
        j = randint(1,6)
    return i,j

# Play Game!
while True:
    game_over = False
    timeElapsed = 0

    # countdown timer
    for i in range(3,0,-1):
        print('Starting game in {}'.format(i))
        sleep(1)

    # generate new maze and initialise board
    maze = generateMaze(5)
    x,y = seed(maze)
    target_y,target_x = seed(maze)

    # start timer
    startTime = time.time()

    # game ends if player wins or time left becomes 0
    while (not game_over) and (timeElapsed<10):

        # # Challenge: random target switch at 5s
        # if(4.95<timeElapsed<5.05):
        #     target_y,target_x = randint(1,6),randint(1,6)

        # restore maze and target so we don't create duplicate marbles
        board = deepcopy(maze)
        board[target_y][target_x] = blue

        # Get imu values
        pitch = sense.get_orientation()['pitch']
        roll = sense.get_orientation()['roll']

        # Move marbles wrt imu orientation
        new_x,new_y = move_marble(pitch,roll,x,y)

        # checks that marble doesn't exceed the wall when moving around
        x,y = check_wall(x,y,new_x,new_y)
        board[y][x] = w

        # checks if player has reached target
        game_over = checkTarget(x,y,target_x,target_y)

        # display pixels
        sense.set_pixels(sum(board,[]))

        # Eval time left
        timeElapsed = time.time()-startTime
        sleep(0.05)

        del board

    print('Game Over!')
    sleep(0.05)
