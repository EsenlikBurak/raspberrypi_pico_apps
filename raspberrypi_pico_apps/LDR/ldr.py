
from machine import Pin,ADC
import time

led=Pin(1,Pin.OUT)
ldr_pin = ADC(26)
while True:
     Value=ldr_pin.read_u16()
     print(Value)
     time.sleep(0.5)
     if (Value>60000):
         led.on()
     else:
         led.off()
     time.sleep
