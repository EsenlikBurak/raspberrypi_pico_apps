from machine import Pin, PWM
import time
from machine import ADC


# LEDs
led1 = PWM(Pin(0))
led2 = PWM(Pin(1))
led3 = PWM(Pin(2))
buzzer = Pin(27, Pin.OUT)
button = Pin(3, Pin.IN, Pin.PULL_DOWN)  #Internal pull-up
potentiometer = ADC(28)
ldr = ADC(Pin(26))
motor_pin1 = Pin(14, Pin.OUT)
motor_pin2 = Pin(15, Pin.OUT)

segA = Pin(22, Pin.OUT)
segB = Pin(21, Pin.OUT)
segC = Pin(20, Pin.OUT)
segD = Pin(19, Pin.OUT)
segE = Pin(18, Pin.OUT)
segF = Pin(17, Pin.OUT)
segG = Pin(16, Pin.OUT)

led1.freq(1000)#Set the frequency
led2.freq(1000)
led3.freq(1000)
State=0 



while True:
    value = potentiometer.read_u16()#Get the values
    #print(value)#Print value on the shell
    led1.duty_u16(value)#Turn the LED ON and OFF
    led2.duty_u16(value)
    led3.duty_u16(value)

    ldrValue = ldr.read_u16()
    print(ldrValue)

    if ldrValue >20000:
        segA.value(0)
        segB.value(0)
        segC.value(0)
        segD.value(0)
        segE.value(0)
        segF.value(0)
        segG.value(1)
    else:
        segA.value(1)
        segB.value(0)
        segC.value(0)
        segD.value(1)
        segE.value(1)
        segF.value(1)
        segG.value(1)

    if button.value() == 1:
        buzzer.value(1)
        time.sleep(1)
    else:
        buzzer.value(0)

    if button.value() == 1:  
           motor_pin1.high()
           motor_pin2.low()
    else:    
           motor_pin1.low()
           motor_pin2.high()
  

    