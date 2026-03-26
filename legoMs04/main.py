#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize Motors and DriveBase
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Initialize the Ultrasonic Sensor
obstacle_sensor = UltrasonicSensor(Port.S4)

# --- MAX VOLUME CONFIGURATION ---
ev3.speaker.set_volume(100)
ev3.speaker.set_speech_options(voice='f1', pitch=90) 

# Main Loop
while True:
    distance = obstacle_sensor.distance()
    ev3.screen.draw_text(40, 50, "DIST: " + str(distance) + "mm")
    
    if distance < 300:  # If an obstacle is detected within 30 cm
        robot.drive(-75, 0)  # Slow down to 75 mm/s
        ev3.speaker.beep(frequency=1000, duration=100)
        wait_time = distance * 1.5 
        # Wait time is proportional to the distance, allowing more time for closer obstacles
        wait(wait_time) 
    elif distance < 80:
        ev3.speaker.beep(frequency=1000, duration=100)
        robot.stop()
        # Wait time is proportional to the distance, allowing more time for closer obstacles
        wait_time = distance * 1.75
        wait(wait_time)
    else:
        robot.drive(-100, 0)  # Drive forward at 100 mm/s

    wait(100)  # Wait for 100 ms before checking again