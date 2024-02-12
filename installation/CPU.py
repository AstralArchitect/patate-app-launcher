import psutil
from sense_hat import SenseHat

sense = SenseHat()

cpu_usage = psutil.cpu_percent()
memory_usage = psutil.virtual_memory().percent
message = f'CPU:{cpu_usage:.1f}%, Mem:{memory_usage:.1f}%'
sense.show_message(message, text_colour=(0, 127, 0), scroll_speed=0.1)