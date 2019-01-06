#!/usr/bin/python3
import time
import pyb

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
def wait_pin_change(pin):
    cur_value = pin.value()
    while active < 20:
        if pin.value() != cur_value:
            active += 1
        else:
            active = 0
        pyb.delay(1)

def led_thing():
    print("Did the LED thing just now...")

#GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 21 to be an input pin and set initial value to be pulled low (off)
#GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pin_x1 = pyb.Pin('21', pyb.Pin.IN, pyb.Pin.PULL_UP)
while True:
    wait_pin_change(pin_x1)
#    pyb.LED(4).toggle()
    led_thing()

#GPIO.add_event_detect(21,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 FALLING edge
#GPIO.add_event_detect(26,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 FALLING edge
#GPIO.add_event_detect(19,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 FALLING edge
#GPIO.add_event_detect(20,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 FALLING edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

#GPIO.cleanup() # Clean up
