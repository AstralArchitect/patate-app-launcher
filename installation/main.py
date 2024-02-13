from sense_hat import SenseHat

sense = SenseHat()

message = "Vous n'avez rien installe."
sense.show_message(message, text_colour=(127, 127, 0), scroll_speed=0.1)
sense.clear()
