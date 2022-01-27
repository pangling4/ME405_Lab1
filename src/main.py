"""!
@file main.py
This file contains code that lights up the LED at pinA0 on the
NUCLEO-L476RG. The pattern executed is a sawtooth wave, where
LED’s brightness slowly increase from 0 to maximum over 5
seconds, then go back to 0 and repeat the process indefinitely.

@author Jonathan Cederquist, Tim Jain, Philip Pang
@date   13-Jan-2022
"""s

import pyb
import utime
import EncoderDriver
import MotorDriver

if __name__ == "__main__":
    encoder1 = EncoderDriver.EncoderDriver(pyb.Pin(pyb.Pin.cpu.C6), pyb.Pin(pyb.Pin.cpu.C7), 8)
    motor1 = MotorDriver.MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)
    time = utime.ticks_ms()
    
    motor1.enable()
    encoder1.update()
    motor1.set_duty_cycle(-20)
    
    while True:
        encoder1.update()
        if encoder1.read() >= 6.2831:
            motor1.disable()
            break
    

#ENCODER DRIVER
#while utime.ticks_ms() < (time + 10000):
#     while True:
#         encoder1.update()
#         if (utime.ticks_ms() > (time + 500)):
#             print("\ntimer counter:", encoder1.timer.counter())
#             print("\nencoder driver", encoder1.read())
#             time += 500
        
        

# 
# # Test Code
# if __name__ == "__main__":
#     # Sets period for sawtooth wave as 5 seconds
#     led_setup()
#     start = utime.ticks_ms()
#     period = 5000
#     while True:
#         # elapsed time is computed as a multiple of the period
#         elapsed = utime.ticks_diff(utime.ticks_ms(), start)/period
#         # brightness is calculated as a percentage of the...
#         # ...period using elapsed time
#         bright = 100 * (elapsed % 1)
#         led_brightness(bright)
