import time
import random as rand
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

while(True):
    
    #Creates 4 pixels of different color values
    for i in range(4):
        x = rand.randint(0,7)
        y = rand.randint(0,7)
        
        #Randomly generate RGB values
        R = rand.randint(0,255)
        G = rand.randint(0,255)
        B = rand.randint(0,255)

        #Display colour
        sense.set_pixel(x,y,(R,G,B))
        
    #Pause for 1 second to admire the effect   
    time.sleep(1)
    
    #Refresh screen
    sense.clear()