## @file mainpage.py
# @author Jonathan Cedarquist, Tim Jain, Philip Pang
# @mainpage Lab 1: Gray Area
# @section intro_sec Introduction
# This exercise involved writing classes in order to run a motor and measure where it is
# by using an encoder. Without further ado, let's get spinning! 
# @section ss_Motor Motor Control
# The motors used for this lab exercise utilize the L6206 H-bridge motor
# driver. It is used to control the 2 DC motors, controls the torque and the direction
#   of the motor. It also acts as a safeguard so that the current does not short out the
#   motor. The block diagram for this IC is shown below.  
# @image html motor_control.JPG Figure 1: H-Bridge [1]
# The motor is connected to output pins OUT1A and OUT2A. The Nucleo L476-RG controls
# pins ENA, INA and IN2A. When controlling a single motor, the wires must be connected
# to the proper CPU pin and they are connected to a single timer on two seperate channels.
# The ENA pin must be enabled in order to enable the motor. The signals of INA and
# IN2A must be opposite of each other in order for the motor to spin. To reverse
# directions, the signals for each pin are reversed. The pin configuration with 
# the appropriate timer and channels are given as such. The orange and the green wires
# were for the motor power.
# @image html pins_motors.JPG Figure 2:Pin Diagram [1]
# The motor is driven by a MotorDriver class, which sets the velocity via
# pulse width modulation percentage. This is also known as a duty cycle.
# In this assignment, our main file uses the MotorDriver to spin the motor
# slowly until it has spun one full rotation, or 2 pi radians. 
# @section ss_Encoder Encoder Reading
# The encoders were used to track the position of the motor as it was spinning.
# It measures the motor's rotations in units of ticks of the encoder. These
# encoders are quadrature optical encoders. The STM32 has timers that can 
# read the pulses of the encoder in order to count distance and direction of motion.
# Gray code is used with two channels of the encoder. A timing diagram is shown
# below. The state of the encoder can be represented as (A,B). The encoder moving
# from (0,0) to (0,1) indicates that the motor is rotating counterclockwise,
# and a movement from (0,1) to (0,0) indicates that the motor is rotating 
# clockwise. 
# @image html enc_diag.JPG Figure 3: Encoder Timing Diagram [1]
# The EncoderDriver works by measuring the delta, or difference, between the 
# current reading and previous reading. This process is shown thanks to a 
# drawing from ME 305 Lecturer Charlie Refvem. It is important to incorporate
# this technique to receive accurate readings. The encoder measures in ticks,
# but in order to make sense of it to measure the motors speed in revolutions 
# per minute, the encoder reading must be converted. This is done by multiplying
# the nominal reading by the CPR value and the gear ratio of the motor since 
# the encoder is directly attached to the motor. 
# @image html charlie_encoder.JPG Figure 4:Charlie Refvem Encoder Delta Diagram [2]
# @section ss_main Main Script 
# The main script interfaces the MotorDriver and EncoderDriver together. 
# We have not yet implemented a task algorithm, but the motor is simply set 
# to a slow duty cycle and spins until it has gone one revolution, as the 
# encoder reading reaches 2 pi radians. 
# @section ss_ref References
# [1] Ridgeley, John, ME 405 Lab #1 Gray Area, W22Lab1.html, January 13, 2021
# \n
# [2] Refvem, Charlie, ME 305 Lecture #20, February 20, 2022
