'''
该程序作用是使用继电器模块控制 LED 闪烁
在线文档：https://docs.geeksman.com/esp32/MicroPython/24.esp32-micropython-relay.html
'''
import time
from machine import Pin


# 配置 GPIO 输出引脚
relay_pin = Pin(15, Pin.OUT)


# 打开继电器
def relay_on():
    relay_pin.value(1)


# 关闭继电器
def relay_off():
    relay_pin.value(0)


# 闪烁灯
def blink():
    relay_on()
    time.sleep(0.5)
    relay_off()
    time.sleep(0.5)


while True:
    blink()