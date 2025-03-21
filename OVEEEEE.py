# Write your code here :-)
from machine import Pin, ADC
import time

# Define the light sensor and LED pins
light_sensor = ADC(Pin(26))  # Light sensor on ADC pin
led = Pin(21, Pin.OUT)       # LED on GPIO15

# Set a threshold for darkness (adjust based on testing)
THRESHOLD = 20000  # Adjust based on sensor readings

while True:
    light_value = light_sensor.read_u16()  # Read sensor value (0-65535)
    print("Light Sensor Value:", light_value)  # Print for debugging

    if light_value < THRESHOLD:
        led.value(0)  # Turn LED on (darkness detected)
        print("LED ON")
    else:
        led.value(1)  # Turn LED off (light detected)
        print("LED OFF")

    time.sleep(0.5)  # Small delay
