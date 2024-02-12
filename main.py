from sense_hat import SenseHat
from time import sleep
import os
import psutil
from random import randint
import pyudev
import threading
import glob

# Initialiser l'objet SenseHat
sense = SenseHat()

try:
    welcome_message = "Bonjour."
    sense.clear()
    sense.show_message(welcome_message, text_colour=(0, 0, 127), scroll_speed=0.1)

    def detect_usb_insertion():
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by(subsystem='block')

        for device in iter(monitor.poll, None):
            if device.action == 'add' and 'ID_BUS' in device:
                a = 0
                if a == 0:
                    a = 1
                    if device['ID_BUS'] == 'usb':
                        cle = "Une cle USB a ete inseree."
                        sense.show_message(cle, text_colour=(0, 0, 127), scroll_speed=0.1)
                        os.system("mount /dev/sda1 /mnt/")
                        motif = "*.tar.xz"
                        fichiers = glob.glob(motif)
                        if fichiers:
                            chemin_fichier = fichiers[0]
                            message = chemin_fichier
                            sense.show_message(message, text_colour=(0, 0, 127), scroll_speed=0.1)
                            os.system("mv " + chemin_fichier + " /root/")
                            os.system("tar -xJvf " + (chemin_fichier - "/mnt/"))
                            os.system("mv " + ((chemin_fichier - "/mnt/") - ".tar.xz") + ".py /root/python-packages/")
                            os.system("mv /root/config/* /root/python-config/")

    detect_usb_insertion_thread = threading.Thread(target=detect_usb_insertion)
    detect_usb_insertion_thread.start()

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
                up = open("/root/python-config/configup")
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
                os.system("mv configup ../configup")
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
                os.system("mv ../configup ./configup")

                sense.set_pixel(6, 4, 127, 127, 0)
                sleep(0.1)
                sense.set_pixel(7, 3, 127, 127, 0)

                sense.set_pixel(7, 4, 127, 127, 0)
                os._exit(0)

        # Attendre quelques secondes avant de répéter
        sleep(2)

except KeyboardInterrupt:
    # Terminer le programme proprement lorsqu'on appuie sur Ctrl+C
    pass
