from machine import Pin
import time

button1 =Pin(1, Pin.IN, Pin.PULL_DOWN)
button2 =Pin(2, Pin.IN, Pin.PULL_DOWN)
led1 = Pin(3,Pin.OUT)
led2 =Pin(4,Pin.OUT)

while True:
    if button1.value()==1:
        led1.value(1)
        led2.value(0)
    if button2.value()==1:
        led1.value(0)
        led2.value(1)

    time.sleep(0.1)
            
    