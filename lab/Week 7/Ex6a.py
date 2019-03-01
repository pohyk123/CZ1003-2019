#This script obtains RGB values from the user input and prints out the text in chosen color combi.

from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)

#--- function get_color() ---------------------------

def get_color(color):
    keep_looping = True
    no_of_try=0
    while keep_looping:
        
        #increment try count
        no_of_try+=1
        
        #ensure try count does not exceed 3, else return 0
        if(no_of_try>3):
            return 0
        
        #get input value for r/g/b
        color_str=input("Enter the value of the " + color + " color for message (0 to 255):")
        
        #try/catch to check for valid format type, and if-else condition to check for valid range 0-255
        try:
            color_int = int(color_str)
            if(0<=color_int<=255):
                keep_looping = False
            else:
                continue
        except:
            print('oops wrong format!')
            continue

    return color_int

#---------------------------------------------------
r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")
msg_color = (r_int, g_int, b_int)
print(msg_color)
sense.show_message("I got it!", text_colour=msg_color)