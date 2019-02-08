from sense_hat import SenseHat
sense = SenseHat()

print("Type 'quit' to exit program.\n")
text_colorname = back_colorname = 'black'

# Colour dictionary
colours = {
    "black":(0,0,0),
    "blue":(0,0,255),
    "red":(255,0,0),
    "green":(0,255,0),
    "yellow":(255,255,0),
    "orange":(255,128,0)
}

# Runs indefinitely until terminated by 'quit'
while(True):
    text_colorname = input('Choose a text color (black,blue,red,green,yellow,orange): ').strip()
    back_colorname = input('Choose a bg color (black,blue,red,green,yellow,orange): ').strip()
    
    # Error catching for text & bg colour input
    if(text_colorname=='quit' or back_colorname=='quit'):
        break
    elif(text_colorname == back_colorname):
        print('Please choose different text and bg colours!')
        continue
    elif(text_colorname not in colours or back_colorname not in colours):
        print('Invalid colour(s) chosen!')
        continue
    
    # Error catching for scroll speed input
    while True:
        try:
            scroll_speed_str = input('What scroll speed do you want? ')
            scroll_speed = float(scroll_speed_str)
            break
        except ValueError as e:
            print(e)
            print('Try again!')
            continue
    
    text = 'This is fun!'
    
    color_msg = colours[text_colorname]
    color_bg = colours[back_colorname]
    
    # Output to sensehat
    sense.show_message(text, text_colour = color_msg, \
     back_colour = color_bg, \
     scroll_speed = scroll_speed)