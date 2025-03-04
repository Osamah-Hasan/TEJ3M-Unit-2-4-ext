"""
Created by: Osamah
Created on: FEB 2025
Created for: TEJ3M-Unit 2-04 RGB light loop
"""

import board
import digitalio
import time

blink_time = 1

# Set up the LED pin (change 'board.GP15' to the correct pin for your board)
led_15 = digitalio.DigitalInOut(board.GP15)
led_14 = digitalio.DigitalInOut(board.GP14)
led_13 = digitalio.DigitalInOut(board.GP13)
led.direction = digitalio.Direction.OUTPUT

while True:
    led_15.value = True  # Turn LED on
    time.sleep(blink_time)

    led_15.value = False  # Turn LED off
    time.sleep(blink_time)

    led_14.value = True  # Turn LED on
    time.sleep(blink_time)

    led_14.value = False  # Turn LED off
    time.sleep(blink_time)