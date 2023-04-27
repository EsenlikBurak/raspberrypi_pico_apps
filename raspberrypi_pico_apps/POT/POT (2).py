from machine import ADC, Pin,PWM
from time import sleep

led1 = PWM(Pin(2))
#Include the LED pin we use PWM here for to use controlable signals
# with potantiometer we will change hz of the LED's
led2 = PWM(Pin(3))
led3 = PWM(Pin(4))
led4 = PWM(Pin(5))
led5 = PWM(Pin(6))
led6 = PWM(Pin(7))
led7 = PWM(Pin(8))
led8 = PWM(Pin(9))
potentiometer = ADC(28)

led1.freq(1000)#Set the frequency
led2.freq(1000)
led3.freq(1000)
led4.freq(1000)
led5.freq(1000)
led6.freq(1000)
led7.freq(1000)
led8.freq(1000)

while True:
    value = potentiometer.read_u16()#Get the values
    print(value)#Print value on the shell
    led1.duty_u16(value)#Turn the LED ON and OFF
    led2.duty_u16(value)
    led3.duty_u16(value)
    led4.duty_u16(value)
    led5.duty_u16(value)
    led6.duty_u16(value)
    led7.duty_u16(value)
    led8.duty_u16(value)
    sleep(0.2)#Set the delay time