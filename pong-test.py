from datetime import datetime
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
message = "lancement du jeu..."
sense.show_message(message, text_colour=(127, 127, 0), scroll_speed=0.1)
ballx = 3
bally = 3
youx = 0
youy = [3, 4]
ennemix = 7
ennemiy = [3, 4]
sleep(1)
for event in events:
    if event.action == "pressed" and event.direction == "up":
        youy[0] + 1
        youy[1] + 1
        sense.set_pixel(youx, youy[0], 127, 127, 0)
        sense.set_pixel(youx, youy[1], 127, 127, 0)
        sense.set_pixel(ballx, bally, 127, 127, 0)
        sense.set_pixel(ennemix, ennemiy[0], 127, 127, 0)
        sense.set_pixel(ennemix, ennemiy[1], 127, 127, 0)
