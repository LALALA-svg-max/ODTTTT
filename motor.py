# Write your code here :-)
from machine import Pin, PWM
from time import sleep

# Setup servo on GPIO 15
servo = PWM(Pin(2))
servo.freq(50)

# Setup button on GPIO 14 (Pulled HIGH, so LOW when pressed)
button = Pin(26, Pin.IN, Pin.PULL_UP)

def set_angle(angle):
    """Convert angle (0-180) to duty cycle (2000-8000)."""
    duty = int((angle / 180) * 6000 + 2000)
    servo.duty_u16(duty)

print("Press the button to move the servo!")

while True:
    if button.value() == 0:  # Button pressed (LOW)
        print("Button pressed! Moving servo...")
        set_angle(90)  # Move to 90°
        sleep(3)  # Stay for 3 seconds
        print("Returning to 0°")
        set_angle(0)  # Move back to 0°

        # Wait until button is released (avoid repeated triggers)
        while button.value() == 0:
            sleep(0.1)

        sleep(0.2)  # Small delay to prevent accidental multiple presses
# Write your code here :-)
