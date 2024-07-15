from machine import Pin
from time import sleep

class LED:
    def __init__(self,pin):
        self.pin = pin
    
    def blink(self,time):

        self = Pin(self.pin,Pin.OUT)

        self.value(1)
        sleep(time)
        self.value(0)
        sleep(time)


if __name__ == "__main__":
    
    # 将led作为LED类的实例化对象，引脚为2号
    led = LED(2)

    # 调用LED类中的blink方法，时间间隔为1秒
    while 1:
        led.blink(0.5)
