import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

led = 12 # GPIO pin number is 12 and name is GPIO18

GPIO.setup(led, GPIO.OUT, initial = 0) # Setup LED and set it initially to OFF

while(True):
        GPIO.output(led, GPIO.HIGH) # Set LED to ON
        time.sleep(2) # Wait for 2 seconds

        GPIO.output(led, GPIO.LOW) # Set LED to OFF
        time.sleep(2)
