from machine import Pin, PWM
import time

buzzerPIN = 16
buzzer = PWM(Pin(buzzerPIN))


while True:
    for i in range(700,800):
        buzzer.freq(i)
        time.sleep_ms(15)
    for i in range(800,700,-1):
        buzzer.freq(i)
        time.sleep_ms(15)