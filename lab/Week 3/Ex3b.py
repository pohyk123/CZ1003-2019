from sense_hat import SenseHat
sense = SenseHat()

text_colorname = input('Choose a text color (black,blue,red,green,yellow,orange): ')
back_colorname = input('Choose a bg color (black,blue,red,green,yellow,orange): ')
rotation_str = input('How much do you want to rotate your text? (0,90,180,360): ')
scroll_speed = float(input('What scroll speed do you want? '))
text = input('Write your text - ')


rotation_val = int(rotation_str) % 360

colours = {
    "black":(0,0,0),
    "blue":(0,0,255),
    "red":(255,0,0),
    "green":(0,255,0),
    "yellow":(255,255,0),
    "orange":(255,128,0)
}

sense.set_rotation(rotation_val)
color_msg = colours[text_colorname]
color_bg = colours[back_colorname]

sense.show_message(text, text_colour = color_msg, \
 back_colour = color_bg, \
 scroll_speed = scroll_speed)