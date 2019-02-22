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
random_colour = False
choice = input('Generate random colours? (y/n)')

if('y' in choice):
    random_colour = True

#Runs infinitely
while(True):
    
    #List representing 8x8 pixels in 1x64 list
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
    rotation = (rotation+90)%360
    sense.set_rotation(rotation)
        
    #Pause for 1 second to admire the effect    
    time.sleep(1)
    
    #Refresh screen
    sense.clear()
    
    #Change colour combinations
    if(random_colour == False):
        y,b = b,y
    else:
        y,b = gen_rand_color(),gen_rand_color()
        
