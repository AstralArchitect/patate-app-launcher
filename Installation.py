from sense_hat import SenseHat
from time import sleep
import os

sense = SenseHat()

try:
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

                os.system("sudo rm -r /root/python/update/.git /root/python/update/README.md")

                sense.set_pixel(6, 3, 127, 127, 0)

                sense.set_pixel(6, 4, 127, 127, 0)

                sense.set_pixel(7, 3, 127, 127, 0)

                sense.set_pixel(7, 4, 127, 127, 0)
                sleep(1) # Attendre une seconde pour éviter une fermeture accidentelle
                os.system("sudo reboot")