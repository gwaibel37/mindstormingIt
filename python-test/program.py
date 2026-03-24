print("Hello World!")

robot_name = "Roberto Driodette"
speed = 360
duration = 1200
temperature = 0.0
is_running = False

print("Robot Name: " + robot_name + "\n")
print("Speed: " + str(speed) + "\n")
print("Temperature: " + str(temperature) + "\n")
print("Is Running: " + str(is_running) + "\n")

speed += 180
print("New Speed: " + str(speed) + "\n")
totalWheelRtation = speed * (duration / 1000)
print("Total Wheel Rotation: " + str(totalWheelRtation) + "\n") 

half_speed = speed / 2
print("Half Speed: " + str(half_speed) + "\n")

modulo = 10 % 3
print("Modulo Operator: " + str(modulo) + " (remainder of 10 divided by 3)\n")

print(f"This is a formatted string with a variable: {half_speed}\n")

for i in range(0, 6):
    print(f"Loop iteration #{i + 1}")
print("Loop Finished!\n")