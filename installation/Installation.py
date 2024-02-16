from sense_hat import SenseHat
from time import sleep
import os

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
            extinction_message = "installation..."
            sense.show_message(extinction_message, text_colour=(90, 0, 127), scroll_speed=0.1)
            sleep(1)  # Attendre une seconde pour éviter une fermeture accidentelle
            
            sense.set_pixel(0, 3, 90, 127, 0)
            os.system("mkdir /save/ ; mv /root/* /save/")

            sense.set_pixel(0, 4, 90, 127, 0)
            os.system("apt-get update -y")
            sense.set_pixel(1, 3, 90, 127, 0)

            sense.set_pixel(1, 4, 90, 127, 0)

            sense.set_pixel(2, 3, 90, 127, 0)

            sense.set_pixel(2, 4, 90, 127, 0)
            os.system("apt-get upgrade -y")

            sense.set_pixel(3, 3, 90, 127, 0)

            sense.set_pixel(3, 4, 90, 127, 0)
            os.system("rm /etc/rc.local ; mv /root/installation/installation/rc.local /etc/rc.local ; mv /root/installation/installation/start.sh /root/ ; chmod 500 /root/start.sh ; chmod 500 /etc/rc.local ; mv /root/installation/installation/repeat.txt /root/")

            sense.set_pixel(4, 3, 90, 127, 0)

            sense.set_pixel(4, 4, 90, 127, 0)
            os.system("rm -r /root/python/")
            os.system("mkdir /root/python/")
            os.system("git clone https://github.com/AstralArchitect/patateOS /root/python/")
            sense.set_pixel(5, 3, 90, 127, 0)

            sense.set_pixel(5, 4, 90, 127, 0)
            os.system("apt-get install python3-psutil python3-pip zip ; pip download pyudev ; unzip pyudev-0.24.1-py3-none-any.whl ; sudo mv pyudev /usr/lib/python3.11/ ; rm -r pyudev-0.24.1.dist-info pyudev-0.24.1-py3-none-any.whl")

            sense.set_pixel(6, 3, 90, 127, 0)

            sense.set_pixel(6, 4, 90, 127, 0)
            os.system("rm -r /root/python-config/ ; rm -r /root/python-packages/ ; mkdir /root/python-config ; mkdir /root/python-packages/ ; mkdir /root/python-packages/exemple/ ; mkdir /root/python-packages/cpu/")
            with open('/root/python-config/configup', 'w') as f:
                f.write('/root/python-packages/exemple/main.py')
            with open('/root/python-config/configleft', 'w') as f:
                f.write('/root/python-packages/cpu/CPU.py')
            with open('/root/repeat.txt', 'w') as f:
                f.write('now')
            os.system("mv /root/installation/installation/CPU.py /root/python-packages/cpu/ ; mv /root/installation/installation/main.py /root/python-packages/exemple/")

            sense.set_pixel(7, 3, 90, 127, 0)

            sense.set_pixel(7, 4, 90, 127, 0)
            os.system("rm -r /root/installation/")
            sleep(0.5) # Attendre une seconde pour éviter une fermeture accidentelle
            os.system("sudo reboot")

except KeyboardInterrupt:
    # This block is to handle if the user interrupts the script with Ctrl+C
    pass
