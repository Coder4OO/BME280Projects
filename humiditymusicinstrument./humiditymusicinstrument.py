#
# Example. Using I2C at P9, P10
#
from machine import I2C
from bme280_float import *
from utime import sleep
from machine import Pin, PWM
sda = Pin(0, Pin.OUT)
scl = Pin(1, Pin.OUT)
buzzer = PWM(Pin(28))
buzzer.duty_u16(1000)
i2c=I2C(id=0,sda=sda,scl=scl)
bme280 = BME280(i2c=i2c)
maxfreq = 3000
while True:
    print(bme280.values[2])
    humidity = float(bme280.values[2][0:len(bme280.values[2])-2])
    freq = maxfreq*humidity/100
    buzzer.freq(int(freq))
    sleep(0.25)
buzzer.duty_u16(0)
