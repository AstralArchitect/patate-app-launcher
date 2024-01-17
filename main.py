from sense_hat import SenseHat
from time import sleep
import os
import psutil

# Initialiser l'objet SenseHat
sense = SenseHat()

try:
    welcome_message = "Bonjour."
    sense.show_message(welcome_message, text_colour=(0, 0, 127), scroll_speed=0.1)

    while True:
        # Obtenir les événements du joystick
        events = sense.stick.get_events()

        # Boucle sur les événements du joystick
        for event in events:
            if event.action == "pressed" and event.direction == "right":
                temperature = sense.get_temperature()
                pressure = sense.get_pressure()
                humidity = sense.get_humidity()

                message = f'T:{temperature:.1f}C, P:{pressure:.1f} hPa, H:{humidity:.1f}%'
                sense.show_message(message, text_colour=(0, 0, 127), scroll_speed=0.1)

            elif event.action == "pressed" and event.direction == "left":
                cpu_usage = psutil.cpu_percent()
                memory_usage = psutil.virtual_memory().percent

                message = f'CPU:{cpu_usage:.1f}%, Mem:{memory_usage:.1f}%'
                sense.show_message(message, text_colour=(0, 127, 0), scroll_speed=0.1)
            elif event.action == "pressed" and event.direction == "up":
                message = "hello"
                sense.show_message(message, text_colour=(127, 127, 0), scroll_speed=0.1)
            elif event.action == "pressed" and event.direction == "down":
                extinction_message = "Arret..."
                sense.show_message(extinction_message, text_colour=(127, 0, 0), scroll_speed=0.1)
                sleep(1)  # Attendre une seconde pour éviter une fermeture accidentelle
                os.system("sudo shutdown")
            # Vérifier le type d'événement
            elif event.action == "pressed" and event.direction == "middle":
                extinction_message = "Mise a jour..."
                sense.show_message(extinction_message, text_colour=(127, 60, 127), scroll_speed=0.1)
                sleep(1)  # Attendre une seconde pour éviter une fermeture accidentelle
                os.system("sudo rm -r /root/python/update/.git /root/update/main.py")
                os.system("sudo git clone https://github.com/AstralArchitect/python-sense-hat.git /root/python/update/")
                os.system("sudo mv /root/python/update/* /root/python/")
                os.system("sudo apt update -y")
                os.system("sudo apt upgrade -y")
                sleep(1)
                os.system("sudo reboot")

        # Attendre quelques secondes avant de répéter
        sleep(3)

except KeyboardInterrupt:
    # Terminer le programme proprement lorsqu'on appuie sur Ctrl+C
    pass