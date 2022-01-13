import pyb
import utime

class MotorDriver:
    '''! 
    This class implements a motor driver for an ME405 kit. 
    '''

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        '''! 
        Creates a motor driver by initializing GPIO
        pins and turning the motor off for safety. 
        @param en_pin Pin object for motor sleep
        @param in1pin Pin object for motor input
        @param in2pin Pin object for motor input
        @param timer An int designating which timer to use
        '''
        print ('Creating a motor driver')
        
        pin1 = pyb.Pin (in1pin, pyb.Pin.OUT_PP)
        pin2 = pyb.Pin (in2pin, pyb.Pin.OUT_PP)
        self.en_pin = pyb.Pin (en_pin, pyb.Pin.OUT_PP)

        tim = pyb.Timer (timer, freq=20000)
        self.ch1 = tim.channel (1, pyb.Timer.PWM, pin=pin1)
        self.ch2 = tim.channel (2, pyb.Timer.PWM, pin=pin2)
        

    def set_duty_cycle (self, level):
        '''!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        '''
        print ('Setting duty cycle to ' + str (level))
        
        if level > 0:
            if level > 100:
                self.ch1.pulse_width_percent(100)
            else:
                self.ch1.pulse_width_percent(level)  
            self.ch2.pulse_width_percent(0)
        elif level < 0:
            if level < -100:
                self.ch2.pulse_width_percent(100)
            else:
                self.ch2.pulse_width_percent(-level)
            self.ch1.pulse_width_percent(0)
        else:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(0)

        
    def enable(self):
        '''!
        This method enables the motor by setting the
        sleep pin to high
        '''
        self.en_pin.high()
        
    def disable(self):
        '''!
        This method disables the motor by setting the
        sleep pin to low
        '''
        self.en_pin.low()
        
if __name__ == "__main__":
    
    motor1 = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    
    motor1.enable()
    motor1.set_duty_cycle(50)
    utime.sleep(3)
    motor1.set_duty_cycle(-50)
    utime.sleep(3)
    motor1.set_duty_cycle(-150)
    utime.sleep(3)
    motor1.set_duty_cycle(0)
    motor1.disable()