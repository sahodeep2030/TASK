angles = [30, -15, 45, 200, 60, 90]

def valid_angle(angle):
    return 0 <= angle <= 180

valid_angles = list(filter(valid_angle, angles))

servo_commands = list(map(lambda x: x * 10, valid_angles))

print("Valid Angles:", valid_angles)
print("Servo Commands:", servo_commands)