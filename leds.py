from ev3dev2.led import Leds
import time
leds = Leds()
while True:
  leds.set_color("RIGHT", "RED")
  time.sleep(1)
  leds.set_color("RIGHT", "GREEN")
  time.sleep(1)
