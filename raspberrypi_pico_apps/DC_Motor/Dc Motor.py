from machine import Pin
import time

In1=Pin(8,Pin.OUT)
In2=Pin(7,Pin.OUT)

def move_forward():
    In1.high()
    In2.low() 
def move_backward():
    In1.low()
    In2.high()
def stop():
    In1.low()
    In2.low()
    
while True:
    move_forward()
    time.sleep(0.5)
    stop()
    time.sleep(1)
    
    move_backward()
    time.sleep(0.5)
    stop()
    time.sleep(1)