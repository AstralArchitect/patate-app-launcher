from sense_hat import SenseHat
from time import sleep
import os
import psutil
import sys
from random import randint
import threading

# Initialiser l'objet SenseHat
sense = SenseHat()

try:
    welcome_message = "Bonjour."
    sense.clear()
    sense.show_message(welcome_message, text_colour=(0, 0, 127), scroll_speed=0.1)

    while True:
        # Obtenir les événements du joystick
        events = sense.stick.get_events()

        # Boucle sur les événements du joystick
        for event in events:
            #donner la pression l'humidité et la température
            if event.action == "pressed" and event.direction == "right":
                temperature = sense.get_temperature()
                pressure = sense.get_pressure()
                humidity = sense.get_humidity()

                message = f'T:{temperature:.1f}C, P:{pressure:.1f} hPa, H:{humidity:.1f}%'
                sense.show_message(message, text_colour=(0, 0, 127), scroll_speed=0.1)

            #donner l'utilisation du CPU et de la mémoire
            elif event.action == "pressed" and event.direction == "left":
                cpu_usage = psutil.cpu_percent()
                memory_usage = psutil.virtual_memory().percent

                message = f'CPU:{cpu_usage:.1f}%, Mem:{memory_usage:.1f}%'
                sense.show_message(message, text_colour=(0, 127, 0), scroll_speed=0.1)
            #jouer à pong
            elif event.action == "pressed" and event.direction == "up":
                up = open("configup")
                loc = up.read()
                with open(loc) as f:
                    exec(f.read())
                up.seek(0)
                up.close()
            #éteindre l'ordinateur
            elif event.action == "pressed" and event.direction == "down":
                extinction_message = "Arret..."
                sense.show_message(extinction_message, text_colour=(127, 0, 0), scroll_speed=0.1)
                sleep(1)  # Attendre une seconde pour éviter une fermeture accidentelle
                os.system("sudo shutdown now")
            # Mettre à jour le programme
            elif event.action == "pressed" and event.direction == "middle":
                sense.set_pixel(0, 3, 127, 127, 0)

                sense.set_pixel(0, 4, 127, 127, 0)
                
                message = "Mise a jour..."
                
                sense.show_message(message, text_colour=(127, 0, 127), scroll_speed=0.1)
                
                sense.set_pixel(0, 3, 127, 127, 0)

                sense.set_pixel(0, 4, 127, 127, 0)
                os.system("git pull")
                sleep(0.1)
                
                sense.set_pixel(1, 3, 127, 127, 0)
                
                sense.set_pixel(1, 4, 127, 127, 0)
                sleep(0.1)

                sense.set_pixel(2, 3, 127, 127, 0)

                sense.set_pixel(2, 4, 127, 127, 0)
                sleep(0.1)

                sense.set_pixel(3, 3, 127, 127, 0)

                sense.set_pixel(3, 4, 127, 127, 0)
                
                sleep(0.1)
                sense.set_pixel(4, 3, 127, 127, 0)

                sense.set_pixel(4, 4, 127, 127, 0)
                sleep(0.1)
                sense.set_pixel(5, 3, 127, 127, 0)

                sense.set_pixel(5, 4, 127, 127, 0)

                os.system("sudo rm -r /root/python/update/README.md /root/python/installation/")
                sleep(0.1)
                sense.set_pixel(6, 3, 127, 127, 0)

                sense.set_pixel(6, 4, 127, 127, 0)
                sleep(0.1)
                sense.set_pixel(7, 3, 127, 127, 0)

                sense.set_pixel(7, 4, 127, 127, 0)
                sys.exit()

        # Attendre quelques secondes avant de répéter
        sleep(2)

except KeyboardInterrupt:
    # Terminer le programme proprement lorsqu'on appuie sur Ctrl+C
    pass
