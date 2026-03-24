#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick to control the screen and speaker
ev3 = EV3Brick()

# Initialize the motors on Ports B and C
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Setup the robot base with physical measurements (55.5mm wheels, 104mm width)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Set speed to 600 (fast but controlled) and acceleration to 1000 for snappy starts
robot.settings(600, 1000, 300, 600)

# Print the mission start to the screen
ev3.screen.print("Mission: Scout")

# Low frequency beep (440Hz) to signal the start of the program
ev3.speaker.beep(440, 500)

# Move forward 500mm to reach the scouting zone
robot.straight(500) 

# Update the screen to show we are entering the loop
ev3.screen.print("Entering Loop...")

# Loop the "peek" move 2 times to check both sides of the path
for i in range(2):
    # Turn 45 degrees to the right to look off-path
    robot.turn(45) 
    # Move forward 200mm while angled
    robot.straight(200) 
    # Turn -45 degrees (left) to face forward again
    robot.turn(-45) 

# Print the retreat status to the screen
ev3.screen.print("Retreating!")

# Drive backward 900mm (negative) to return to where we started
robot.straight(-900)

# Perform a final 360-degree turn
robot.turn(360)

# High frequency beep (1200Hz) to signal successful completion
ev3.speaker.beep(1200, 500)

# Clear the screen and print the final message
ev3.screen.clear()
ev3.screen.print("Home Safe!")