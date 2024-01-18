from datetime import datetime
from sense_hat import SenseHat
from time import sleep
import os
import psutil
import datetime

# Initialiser l'objet SenseHat
sense = SenseHat()

try:
    welcome_message = "Bonjour."
    sense.show_message(welcome_message, text_colour=(0, 0, 127), scroll_speed=0.1)
    print("appuyez sur le joysick du sense hat pour procedéder à l'installation.")

    while True:
        # Obtenir les événements du joystick
        events = sense.stick.get_events()

        # Boucle sur les événements du joystick
        for event in events:
            if event.action == "pressed" and event.direction == "middle":
                extinction_message = "installation..."
                sense.show_message(extinction_message, text_colour=(90, 0, 127), scroll_speed=0.1)
                sleep(1)  # Attendre une seconde pour éviter une fermeture accidentelle
                
                sense.set_pixel(0, 3, 90, 127, 0)

                sense.set_pixel(0, 4, 90, 127, 0)
                os.system("sudo apt-get update")
                os.system("sudo apt-get upgrade")
                sense.set_pixel(1, 3, 90, 127, 0)
                
                sense.set_pixel(1, 4, 90, 127, 0)

                sense.set_pixel(2, 3, 90, 127, 0)

                sense.set_pixel(2, 4, 90, 127, 0)

                sense.set_pixel(3, 3, 90, 127, 0)

                sense.set_pixel(3, 4, 90, 127, 0)
                os.system("sudo rm /etc/rc.local")
                os.system("sudo mv /root/installation/installation/rc.local /etc/rc.local")
                os.system("sudo mv /root/installation/installation/start.sh /root/")
                os.system("chmod +x /root/start.sh")

                sense.set_pixel(4, 3, 90, 127, 0)

                sense.set_pixel(4, 4, 90, 127, 0)

                os.system("sudo mkdir /root/python/ /root/python/update/")
                os.system("sudo mv /root/installation/main.py /root/python/")
                os.system("sudo mv /root/installation/version.txt /root/python/")
                sense.set_pixel(5, 3, 90, 127, 0)

                sense.set_pixel(5, 4, 90, 127, 0)

                sense.set_pixel(6, 3, 90, 127, 0)

                sense.set_pixel(6, 4, 90, 127, 0)
                os.system("sudo rm -r /root/installation/")

                sense.set_pixel(7, 3, 90, 127, 0)

                sense.set_pixel(7, 4, 90, 127, 0)
                sleep(1) # Attendre une seconde pour éviter une fermeture accidentelle
                os.system("sudo reboot")

        # Attendre quelques secondes avant de répéter
        sleep(3)

except KeyboardInterrupt:
    # Terminer le programme proprement lorsqu'on appuie sur Ctrl+C
    pass