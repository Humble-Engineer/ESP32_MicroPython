'''
该程序说明：使一颗 LED 闪烁
在线文档：https://docs.geeksman.com/esp32/MicroPython/04.esp32-micropython-LED.html
'''

import time
from machine import Pin


# 声明 Pin12 引脚对象
pin_12 = Pin(12, Pin.OUT)

# 循环语句
while True:
    pin_12.on()
    time.sleep(0.5)
    pin_12.off()
    time.sleep(0.5)