#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
import random

# Initialize the hub and motor
ev3 = EV3Brick()
motor_a = Motor(Port.A)

ev3.speaker.set_volume(100)
print("Initiating Chaos Mode...")

# Run this loop 20 times (or change to 'while True:' for infinite madness)
for _ in range(20):
    # 1. Pick a "really fast" speed between -1000 and 1000
    # Negative values automatically handle the "randomly backwards" part
    crazy_speed = random.randint(-1000, 1000)
    
    # 2. Pick a random duration for this burst (200ms to 1.5 seconds)
    duration = random.randint(200, 1500)
    
    # 3. Play a stupid random beep
    # Random frequency between 100Hz (low growl) and 2000Hz (high squeak)
    ev3.speaker.beep(frequency=random.randint(100, 2000), duration=100)
    
    print("Zipping at:", crazy_speed)
    motor_a.run(crazy_speed)
    
    # Wait for the duration of the burst
    wait(duration)

# Stop the madness
motor_a.stop()
ev3.speaker.say("System meltdown averted")
print("Done!")