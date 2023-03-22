from machine import Pin
from time import sleep

led = Pin(5, Pin.OUT)
button = Pin(4, Pin.IN)

while True:
  led.value(button.value())
  sleep(0.1)



import machine
import time

button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
  print("Button state", button.value())
  time.sleep(0.1)