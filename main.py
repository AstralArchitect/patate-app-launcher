from sense_hat import SenseHat
from time import sleep
import os
from random import randint
import pyudev
import threading

# Initialiser l'objet SenseHat
sense = SenseHat()

try:
    a = 0
    welcome_message = "Bonjour."
    sense.clear()
    sense.show_message(welcome_message, text_colour=(0, 0, 127), scroll_speed=0.1)

    def detect_usb_insertion():
        global a
        context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by(subsystem='block')

        for device in iter(monitor.poll, None):
            if device.action == 'add' and 'ID_BUS' in device:
                if a == 0:
                    a = 1
                    if device['ID_BUS'] == 'usb':
                        os.system("mount /dev/sda1 /mnt/")
                        message = "install..."
                        sense.show_message(message, text_colour=(0, 127, 127), scroll_speed=0.1)
                        os.system("mkdir /root/install/")
                        sense.set_pixel(0, 4, 127, 0, 0)
                        os.system("cp /mnt/install.tar.xz /root/")
                        sense.set_pixel(1, 4, 127, 0, 0)
                        os.system("cd /root/ ; tar -xJvf /root/install.tar.xz ; mv /root/config/ /root/install/ ; mv /root/main.py /root/install/ ; mv /root/name /root/install/")
                        sense.set_pixel(2, 4, 127, 0, 0)
                        install = open("/root/install/name")
                        name = install.read()
                        os.system("mkdir /root/python-packages/" + name + "/")
                        sense.set_pixel(3, 4, 127, 0, 0)
                        os.system("mv /root/install/main.py /root/python-packages/" + name + "/")
                        sense.set_pixel(4, 4, 127, 0, 0)
                        os.system("mv /root/install/config/* /root/python-config/")
                        sense.set_pixel(5, 4, 127, 0, 0)
                        os.system("rm -r /root/install/ /root/install.tar.xz")
                        sense.set_pixel(6, 4, 127, 0, 0)
                        os.system("umount /dev/sda1")
                        sense.set_pixel(7, 4, 0, 127, 0)
                        sleep(1)
                        sense.clear()
                        os._exit(0)

    detect_usb_insertion_thread = threading.Thread(target=detect_usb_insertion)
    detect_usb_insertion_thread.start()

    programmes = os.listdir("/root/python-config/")
    programme = 0
    while True:
        # Obtenir les événements du joystick
        events = sense.stick.get_events()
        # Boucle sur les événements du joystick
        for event in events:
            sense.clear()
            if event.action == "pressed" and event.direction == "up":
                sense.show_message(programmes[programme], text_colour=(0, 0, 127), scroll_speed=0.1)
                events = sense.stick.get_events()
                truc = False
                sleep(1)
                for event in events:
                    if event.action == "pressed" and event.direction == "middle":
                        up = open("/root/python-config/" + programmes[programme])
                        loc = up.read()
                        with open(loc) as f:
                            exec(f.read())
                        up.seek(0)
                        up.close()
                    elif event.action == "pressed" and event.direction == "left":
                        up = open("/root/python-config/" + programmes[programme])
                        loc = up.read()
                        uninstall = "desintallation..."
                        sense.show_message(uninstall, text_colour=(0, 0, 127), scroll_speed=0.1)
                        os.system("rm -r /root/python-packages/" + programmes[programme] +  "/ " + loc)
                if programme == len(programmes) - 1:
                    programme = 0
                    continue
                programme = (programme + 1)
            elif event.action == "pressed" and event.direction == "middle":
                sense.clear()
                message = "Mise a jour..."
                
                sense.show_message(message, text_colour=(127, 0, 127), scroll_speed=0.1)
                
                sense.set_pixel(0, 2, 65, 65, 65)
                sense.set_pixel(1, 2, 65, 65, 65)
                sense.set_pixel(2, 2, 65, 65, 65)
                sense.set_pixel(3, 2, 65, 65, 65)
                sense.set_pixel(4, 2, 65, 65, 65)
                sense.set_pixel(5, 2, 65, 65, 65)
                sense.set_pixel(6, 2, 65, 65, 65)
                sense.set_pixel(7, 2, 65, 65, 65)
                sense.set_pixel(0, 5, 65, 65, 65)
                sense.set_pixel(1, 5, 65, 65, 65)
                sense.set_pixel(2, 5, 65, 65, 65)
                sense.set_pixel(3, 5, 65, 65, 65)
                sense.set_pixel(4, 5, 65, 65, 65)
                sense.set_pixel(5, 5, 65, 65, 65)
                sense.set_pixel(6, 5, 65, 65, 65)
                sense.set_pixel(7, 5, 65, 65, 65)
                
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
