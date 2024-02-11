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
    sense.clear()
    welcome_message = "Bonjour."
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
                # Initialisez toutes les variables globales
                message = "pong..."
                sense.show_message(message, text_colour=(127, 127, 0), scroll_speed=0.1)
                sense.clear()
                ballx = 4
                bally = 3
                youx = 0
                youy = [3, 4]
                ennemix = 7
                ennemiy = [3, 4]
                mx = 0
                my = 0
                temps = 1.5
                a = 0

                # Définissez la fonction afficher()
                def afficher():
                    sense.set_pixel(youx, youy[0], 127, 127, 0)
                    sense.set_pixel(youx, youy[1], 127, 127, 0)
                    sense.set_pixel(ballx, bally, 127, 127, 0)
                    sense.set_pixel(ennemix, ennemiy[0], 127, 127, 0)
                    sense.set_pixel(ennemix, ennemiy[1], 127, 127, 0)
                    sense.set_pixel(7, 7, 0, 127, 127)

                sleep(0.5)

                # Définissez la fonction move()
                def move():
                    global a
                    while(a == 0):
                        events = sense.stick.get_events()
                        for event in events:
                            if event.action == "pressed" and event.direction == "up":
                                if not (youy[1] < 2):
                                    sense.set_pixel(youx, youy[0], 0, 0, 0)
                                    sense.set_pixel(youx, youy[1], 0, 0, 0)
                                    sense.set_pixel(0, 0, 0, 127, 127)
                                    sense.set_pixel(0, 7, 0, 127, 127)
                                    youy[0] = youy[0] - 1
                                    youy[1] = youy[1] - 1
                                    afficher()
                            elif event.action == "pressed" and event.direction == "down":
                                if not (youy[1] > 6):
                                    sense.set_pixel(youx, youy[0], 0, 0, 0)
                                    sense.set_pixel(youx, youy[1], 0, 0, 0)
                                    sense.set_pixel(0, 0, 0, 127, 127)
                                    sense.set_pixel(0, 7, 0, 127, 127)
                                    youy[0] = youy[0] + 1
                                    youy[1] = youy[1] + 1
                                    afficher()

                move_thread = threading.Thread(target=move)
                move_thread.start()

                # Définissez la fonction ball()
                def ball():
                    global a, temps, my, ennemix, ennemiy, youx, youy, ballx, bally, mx
                    while (a == 0):
                        sense.set_pixel(youx, youy[0], 0, 0, 0)
                        sense.set_pixel(youx, youy[1], 0, 0, 0)
                        sense.set_pixel(ballx, bally, 0, 0, 0)
                        sense.set_pixel(ennemix, ennemiy[0], 0, 0, 0)
                        sense.set_pixel(ennemix, ennemiy[1], 0, 0, 0)
                        if mx == 0:
                            ballx = ballx + 1
                        elif mx == 1:
                            ballx = ballx - 1
                        if my == 0:
                            bally = bally + int(randint(0, 1))
                        elif my == 1:
                            bally = bally - int(randint(0, 1))
                        if bally > 4 :
                            ennemiy[0] = bally + 1
                            ennemiy[1] = bally
                            afficher()
                            sleep(temps)
                        elif bally < 4:
                            ennemiy[0] = bally
                            ennemiy[1] = bally + 1
                            afficher()
                            sleep(temps)
                        if ballx == 6:
                            mx = 1
                        elif (ballx == 1 and bally == youy[1]) or (ballx == 1 and bally == youy[0]):
                            mx = 0
                        elif (ballx == 1 and not(bally == youy[1])) or (ballx == 1 and not(bally == youy[0])):
                            mx = 0
                            message = "Vous avez perdu !"
                            sense.show_message(message, text_colour=(127, 0, 0), scroll_speed=0.1)
                            a = 1
                            break
                        if bally == 6 and bally == (ennemiy[1] or ennemiy[0]):
                            my = 1
                        if temps < 0.3 or bally == 6 and not bally == (ennemiy[1] or ennemiy[0]):
                            my = 1
                            message = "Vous avez gagné !"
                            sense.show_message(message, text_colour=(70, 127, 70), scroll_speed=0.1)
                            a = 1
                            break
                        elif bally == 1:
                            my = 0
                            temps = temps - 0.01

                ball_thread = threading.Thread(target=ball)
                ball_thread.start()
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
