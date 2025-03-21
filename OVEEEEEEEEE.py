# Write your code here :-)
from machine import Pin, ADC
import time

# Define the light sensor pin
light_sensor = ADC(Pin(26))  # Adjust pin number based on your setup

while True:
    light_value = light_sensor.read_u16()  # Read sensor value (0-65535)
    print("Light Sensor Value:", light_value)  # Print for debugging

    time.sleep(0.5)  # Small delay to avoid too frequent readings
