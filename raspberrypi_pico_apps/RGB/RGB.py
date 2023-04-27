from machine import Pin 
import utime
led_red =Pin(1,Pin.OUT)
led_green =Pin(2,Pin.OUT)
led_blue =Pin(3,Pin.OUT)


while True:
    led_red.value(0)
    led_green.value(0)
    led_blue.value(0)


    led_red.value(0)
    led_green.value(1)
    led_blue.value(1)
    utime.sleep(1)

    led_red.value(1)
    led_green.value(0)
    led_blue.value(1)
    utime.sleep(1)

    led_red.value(1)
    led_green.value(1)
    led_blue.value(0)
    utime.sleep(1)