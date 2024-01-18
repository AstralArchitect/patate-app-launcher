from sense_hat import SenseHat
from time import sleep
import os
import psutil

# Initialiser l'objet SenseHat
sense = SenseHat()

try:
    os.system("sudo rm -r /root/python/update/.git /root/python/update/*")
    sense.set_pixel(0, 3, 127, 127, 0)

    sense.set_pixel(0, 4, 127, 127, 0)
                
    os.system("sudo git clone https://github.com/AstralArchitect/python-sense-hat.git /root/python/update/")
    f = open("/root/python/version.txt")
    f2 = open("/root/python/update/version.txt")
    v = f.read()
    vn = f2.read()
    b = 1
    if v == vn:
        b = 0
    if b == 1:
        sense.set_pixel(1, 3, 127, 127, 0)
                
        sense.set_pixel(1, 4, 127, 127, 0)
        
        sense.set_pixel(2, 3, 127, 127, 0)

        sense.set_pixel(2, 4, 127, 127, 0)

        sense.set_pixel(3, 3, 127, 127, 0)

        sense.set_pixel(3, 4, 127, 127, 0)
                
        os.system("sudo mv /root/python/update/main.py /root/python/")
        os.system("sudo mv /root/python/update/version.txt /root/python/")

        sense.set_pixel(4, 3, 127, 127, 0)

        sense.set_pixel(4, 4, 127, 127, 0)

        sense.set_pixel(5, 3, 127, 127, 0)

        sense.set_pixel(5, 4, 127, 127, 0)

        os.system("sudo rm -r /root/python/update/.git /root/python/update/README.md /root/python/update/installation/")

        sense.set_pixel(6, 3, 127, 127, 0)

        sense.set_pixel(6, 4, 127, 127, 0)

        sense.set_pixel(7, 3, 127, 127, 0)

        sense.set_pixel(7, 4, 127, 127, 0)
        sleep(1)
        os.system("sudo reboot")
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
                message = "pong..."
                sense.show_message(message, text_colour=(127, 127, 0), scroll_speed=0.1)
                ballx = 3
                bally = 3
                youx = 0
                youy = [3, 4]
                ennemix = 7
                ennemiy = [3, 4]
                sleep(1)
                a = 0
                while (a == 0):
                    events = sense.stick.get_events()
                    for event in events:
                        if event.action == "pressed" and event.direction == "up":
                            if not (youy[0] < 1):
                                youy[0] = youy[0] - 1
                                youy[1] = youy[1] - 1
                        elif event.action == "pressed" and event.direction == "down":
                            if not (youy[1] > 6):
                                youy[0] = youy[0] + 1
                                youy[1] = youy[1] + 1
                        else:
                            sense.clear()
                            sense.set_pixel(youx, youy[0], 127, 127, 0)
                            sense.set_pixel(youx, youy[1], 127, 127, 0)
                            sense.set_pixel(ballx, bally, 127, 127, 0)
                            sense.set_pixel(ennemix, ennemiy[0], 127, 127, 0)
                            sense.set_pixel(ennemix, ennemiy[1], 127, 127, 0)
                            ballx = ballx + 1
                            bally = bally + 1
                        if bally > 4:
                            ennemiy[0] = bally
                            ennemiy[1] = bally + 1
                            sleep(1)
                        elif bally < 4:
                            ennemiy[0] = bally + 1
                            ennemiy[1] = bally
                            sleep(1)
                        if ennemiy[0] == bally & ennemix == ballx or ennemiy[1] == bally & ennemix or youy[0] == bally & youx == ballx or youy[1] == bally & youx:
                            m = 1

            elif event.action == "pressed" and event.direction == "down":
                extinction_message = "Arret..."
                sense.show_message(extinction_message, text_colour=(127, 0, 0), scroll_speed=0.1)
                sleep(1)  # Attendre une seconde pour éviter une fermeture accidentelle
                os.system("sudo shutdown now")
            # Vérifier le type d'événement
            elif event.action == "pressed" and event.direction == "middle":
                extinction_message = "Mise a jour..."
                sense.show_message(extinction_message, text_colour=(127, 0, 127), scroll_speed=0.1)
                sleep(1)  # Attendre une seconde pour éviter une fermeture accidentelle
                
                os.system("sudo rm -r /root/python/update/.git /root/python/update/*")
                sense.set_pixel(0, 3, 127, 127, 0)

                sense.set_pixel(0, 4, 127, 127, 0)
                
                sense.set_pixel(1, 3, 127, 127, 0)
                
                sense.set_pixel(1, 4, 127, 127, 0)
                os.system("sudo git clone https://github.com/AstralArchitect/python-sense-hat.git /root/python/update/")
                f = open("/root/python/version.txt")
                f2 = open("/root/python/update/version.txt")
                v = f.read()
                vn = f2.read()

                if v == vn:
                    message = "Bonjour."
                    sense.show_message(message, text_colour=(0, 0, 127), scroll_speed=0.1)
                    break

                sense.set_pixel(2, 3, 127, 127, 0)

                sense.set_pixel(2, 4, 127, 127, 0)

                sense.set_pixel(3, 3, 127, 127, 0)

                sense.set_pixel(3, 4, 127, 127, 0)
                
                os.system("sudo mv /root/python/update/main.py /root/python/")
                os.system("sudo mv /root/python/update/version.txt /root/python/")

                sense.set_pixel(4, 3, 127, 127, 0)

                sense.set_pixel(4, 4, 127, 127, 0)

                sense.set_pixel(5, 3, 127, 127, 0)

                sense.set_pixel(5, 4, 127, 127, 0)

                os.system("sudo rm -r /root/python/update/.git /root/python/update/README.md /root/python/update/installation/")

                sense.set_pixel(6, 3, 127, 127, 0)

                sense.set_pixel(6, 4, 127, 127, 0)

                sense.set_pixel(7, 3, 127, 127, 0)

                sense.set_pixel(7, 4, 127, 127, 0)
                sleep(1) # Attendre une seconde pour éviter une fermeture accidentelle
                os.system("sudo reboot")

        # Attendre quelques secondes avant de répéter
        sleep(3)

except KeyboardInterrupt:
    # Terminer le programme proprement lorsqu'on appuie sur Ctrl+C
    pass