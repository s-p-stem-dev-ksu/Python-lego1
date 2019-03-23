from ev3dev2.led import Leds
import time
lights = Leds()
while True:
  lights.set_color("LEFT", "RED")
  lights.set_color("RIGHT", "RED")
  time.sleep(1)
  lights.set_color("LEFT", "AMBER")
  lights.set_color("RIGHT", "AMBER")
  time.sleep(1)
  lights.set_color("LEFT", "GREEN")
  lights.set_color("RIGHT", "GREEN")
  time.sleep(1)
