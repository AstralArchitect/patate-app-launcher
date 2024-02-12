import threading
from random import randint
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

# Initialisez toutes les variables globales
message = "Vous n'avez rien installé..."
sense.show_message(message, text_colour=(127, 127, 0), scroll_speed=0.1)
sense.clear()
