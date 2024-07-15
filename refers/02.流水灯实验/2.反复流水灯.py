'''
该程序作用是实现反复流水灯
在线文档：https://docs.geeksman.com/esp32/MicroPython/05.esp32-micropython-water-lamp.html
'''

import time
from machine import Pin

# 定义 LED 控制引脚 D13、12、14、27、26
pin_index_list = [13, 12, 14, 27, 26]

# 定义 led_pin_list 列表，保存 LED 管脚配置对象
led_pin_list = []

# 循环给 led_pin_list 列表添加对象
for i in pin_index_list:
    led_pin_list.append(Pin(i, Pin.OUT))

# LED全熄灭
for led_pin in led_pin_list:
    led_pin.value(0)

while True:

    # LED逐个点亮
    for led_pin in led_pin_list:
        led_pin.value(1)
        time.sleep(0.1)

    # LED逐个熄灭
    for led_pin in reversed(led_pin_list):
        led_pin.value(0)
        time.sleep(0.1)