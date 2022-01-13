import pyb
import utime

class EncoderDriver:
    '''! 
    This class implements an encoder driver for an ME405 kit. 
    '''
    current_position = 0
    delta = 0
    
    def __init__ (self, in1pin, in2pin, timer):
        '''! 
        Creates an encoder driver by initializing GPIO
        pins and turning the motor off for safety. 
        @param en_pin (There will be several of these)
        '''
        self.timer = pyb.Timer(timer, prescaler = 256, period = 65535)
        ch1 = self.timer.channel(1, pyb.Timer.ENC_AB, pin = in1pin)
        ch1 = self.timer.channel(2, pyb.Timer.ENC_AB, pin = in2pin)
        

    def update(self):

        
        '''@brief       needs at least 2 values in each period
           @details     if >=2 values then delta can be accurately recorded
                        saved and then subtracted from last known value '''

        prev_position = self.current_position % 65535
        self.delta = self.timer.counter() - prev_position
        if self.delta < -65535/2:
            self.delta += 65535
        elif self.delta > 65535/2:
            self.delta -= 65535
        self.current_position += self.delta
    
    def read (self):
        '''!
 
        '''
        return self.current_position

        
    def zero(self):
        self.current_position = 0
        self.delta = 0
        
        
if __name__ == "__main__":
    
    encoder1 = EncoderDriver(pyb.Pin(pyb.Pin.cpu.C6), pyb.Pin(pyb.Pin.cpu.C7), 8)
    time = utime.ticks_ms()
    
    #while utime.ticks_ms() < (time + 10000):
    while True:
        encoder1.update()
        if (utime.ticks_ms() > (time + 500)):
            print("\nencoder:", encoder1.timer.counter())
            time += 500