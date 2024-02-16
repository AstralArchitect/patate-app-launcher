import psutil
from sense_hat import SenseHat

sense = SenseHat()

humidity = sense.get_humidity()
pressure = sense.get_pressure()
temperature = sense.get_temperature()

message = f'Temp:{temperature:.2f}C, P:{pressure:.2f}hPa, H:{humidity:.1f}%'
sense.show_message(message, text_colour=(0, 127, 0), scroll_speed=0.1)