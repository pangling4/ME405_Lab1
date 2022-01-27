''' @file       EncoderDriver.py
    @brief      Used to read from encoders attached to motors
    @details    Utilizes alternate functions from timer channels on pyb board to 
                read from attached encoders
    @author     Jonathan Cederquist
    @author     Tim Jain
    @author     Philip Pang
    @date       Last Modified 1/26/22
'''

import pyb
import utime

class EncoderDriver:
    '''! 
    This class implements an encoder driver for an ME405 kit. 
    '''
    
    def __init__ (self, in1pin, in2pin, timer):
        '''! 
        @brief          Creates an encoder driver object
        @details        Creates an encoder driver by initializing timers and channels with 
                        given pins and timer number
        @param in1pin   A pyb.Pin object corresponding to the encoder channel A 
        @param in2pin   A pyb.Pin object corresponding to the encoder channel B
        @param timer    The timer number corresponding to the encoder pins
        '''
        
        # Create timer and timer channels in encoder mode
        self.timer = pyb.Timer(timer, prescaler = 0, period = 65535)
        self.ch1 = self.timer.channel(1, pyb.Timer.ENC_AB, pin = in1pin)
        self.ch2 = self.timer.channel(2, pyb.Timer.ENC_AB, pin = in2pin)
        
        # Stores current encoder position in radians
        self.current_position = 0
        self.delta = 0
        

    def update(self):
        '''!
        @brief      Updates the position of the encoder 
        @details    Updates the position of the encoder using saved last value
                    Checks for a 'valid' delta and adjusts if needed, then adds
                    delta to previous position 
        '''

        prev_position = self.current_position % 65535
        self.delta = self.timer.counter() - prev_position
        
        # Validate and adjust delta
        if self.delta < -65535/2:
            self.delta += 65535
        elif self.delta > 65535/2:
            self.delta -= 65535
        
        # Update position
        self.current_position += self.delta
    
    def read (self):
        '''!
        @brief      Returns current position of encoder
        @details    Converts the current encoder position reading (in ticks)
                    to radians using the encoder CPR and gear ratio
        '''
        gearRatio = 16
        CPR = 256
        
        return self.current_position * 3.1415926535 / (gearRatio*CPR*2)
    

    def zero(self):
        '''!
        @brief      Zeros the encoder position
        '''
        
        self.current_position = 0
        self.delta = 0
        
        
if __name__ == "__main__":
    
    encoder1 = EncoderDriver(pyb.Pin(pyb.Pin.cpu.C6), pyb.Pin(pyb.Pin.cpu.C7), 8)
    time = utime.ticks_ms()
    
    #while utime.ticks_ms() < (time + 10000):
    while True:
        encoder1.update()
        if (utime.ticks_ms() > (time + 500)):
            print("\ntimer counter:", encoder1.timer.counter())
            print("\nencoder driver", encoder1.read())
            time += 500