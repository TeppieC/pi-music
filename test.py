import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(18, gpio.OUT)
print("LED ON")
gpio.output(18, gpio.HIGH)
time.sleep(1)
print("LED OFF")
gpio.output(18, gpio.LOW)