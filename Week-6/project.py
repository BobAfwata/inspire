import machine
import time
#from machine import Pin
#from time import sleep

rtc = machine.RTC()
#setting time
rtc.datetime((2023, 3, 16, 11, 2, 0, 0, 0)) # set a specific date and
                                             # time, eg. 2017/8/23 1:12:48


red_led =    machine.Pin(12, machine.Pin.OUT)
blue_led =   machine.Pin(13, machine.Pin.OUT)
yellow_led = machine.Pin(14, machine.Pin.OUT)

#ldr code

light_sensor = machine.ADC(machine.Pin(28))     # create ADC object on ADC pin
 

#button = Pin(4, Pin.IN)
red_button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP) 
blue_button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP) 
yellow_button = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP) 

#connected button to 3.3v
while True:
  light_value = light_sensor.read_u16()
  print("Light Intensity :",light_value)
  print("\n\n")
  print("Date ",rtc.now()) 
  print("\n\n")
  # get date and time)
  button_state = button.value()
  print("Button state", button_state) #high / low
  red_led.value(button_state)
  blue_led.value(button_state)
  yellow_led.value(button_state)


    
