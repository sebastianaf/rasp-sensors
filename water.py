import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR_GPIO = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR_GPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
   global count
   if start_counter == 1:
      count = count+1

GPIO.add_event_detect(FLOW_SENSOR_GPIO, GPIO.FALLING, callback=countPulse)

while True:
    try:
        start_counter = 1
        time.sleep(0.125)
        start_counter = 0
        flow = (count / 0.849399)
        print("%.6f lts/min" % (flow))
        count = 0
        time.sleep(0.125)
    except KeyboardInterrupt:
        print('\nkeyboard interrupt!')
        GPIO.cleanup()
        sys.exit()

