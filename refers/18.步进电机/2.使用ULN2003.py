'''
该程序作用是使用第三方模块驱动步进电机转动指定角度
在线文档：https://docs.geeksman.com/esp32/MicroPython/21.esp32-micropython-step-motor.html
'''
from machine import Pin
from libs.uln2003 import Uln2003


motor = Uln2003(pin1=Pin(13), pin2=Pin(12), pin3=Pin(14),
                pin4=Pin(27), delay=2)

# 转动 180°
motor.angle(180, -1)