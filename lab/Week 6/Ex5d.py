import time
import random as rand
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

#Generates random RGB combinations
def gen_rand_color():
    R = rand.randint(0,255)
    G = rand.randint(0,255)
    B = rand.randint(0,255)
    return (R,G,B)

y = (255, 255, 0)
b = (0, 0, 255) 
rotation = 0
wins = 0
delay = 2
random_colour = False
choice = input('Generate random colours? (y/n)')

if('y' in choice):
    random_colour = True

#Runs for 10 wins
while(True):
    
    image_pixels = [b, b, b, b, b, b, b, b,
    b, b, b, y, b, b, b, b,
    b, b, y, y, y, b, b, b,
    b, y, b, y, b, y, b, b,
    b, b, b, y, b, b, b, b,
    b, b, b, y, b, b, b, b,
    b, b, b, y, b, b, b, b,
    b, b, b, y, b, b, b, b] 
        
    #Set new pixel and rotation values 
    sense.set_pixels(image_pixels)
    rotation = rand.randint(1,4)
    sense.set_rotation(rotation*90%360)
    
    #Pause for 1 second to admire the effect     
    time.sleep(delay)
    
    #Increase player's reaction time
    delay*=0.95
    
    #Refresh screen
    sense.clear()
    
    #Collect IMU values
    acceleration = sense.get_accelerometer_raw()
    x_ = acceleration['x']
    y_ = acceleration['y']
    z_ = acceleration['z']
    
    #Add point if imu points in the correct orientation
    if(x_>0 and rotation == 1):
        wins+=1
    elif(y_>0 and rotation == 2):
        wins+=1
    elif(x_<0 and rotation == 3):
        wins+=1
    elif(y_<0 and rotation == 4):
        wins+=1
    else:
        print('Wrong! Try again :)')
        break
        
    print('Keep going! Wins:', wins)
    
    #Change colour combinations
    if(random_colour == False):
        y,b = b,y
    else:
        y,b = gen_rand_color(),gen_rand_color()
        
print('Gameover!')