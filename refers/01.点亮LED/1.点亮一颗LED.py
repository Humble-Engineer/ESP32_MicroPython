'''
该程序说明：使用点亮一颗 LED
在线文档：https://docs.geeksman.com/esp32/MicroPython/04.esp32-micropython-LED.html
'''

from machine import Pin


# 声明一个引脚对象
pin_12 = Pin(15, Pin.OUT)

# 输出高电平
pin_12.value(1)