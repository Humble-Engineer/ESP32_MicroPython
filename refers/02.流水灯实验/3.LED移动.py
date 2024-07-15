'''
该程序作用是实现 LED 的移动
在线文档：https://docs.geeksman.com/esp32/MicroPython/05.esp32-micropython-water-lamp.html
'''

import time
from machine import Pin

# 定义 LED 控制引脚
pin_index_list = [13, 12, 14, 27, 26]

# 定义 led_pin_list 列表，保存 LED 管脚配置对象
led_pin_list = []

# 循环给 led_pin_list 列表添加对象
for i in pin_index_list:
    led_pin_list.append(Pin(i, Pin.OUT))

# 获取 LED_Pin_list 的长度
num = len(led_pin_list)

# LED全熄灭
for led_pin in led_pin_list:
    led_pin.value(0)

while True:

    for i in range(num):
        # LED逐个点亮
        led_pin_list[i].value(1)
        # 如果这颗 LED 是第一个，则需要改变最后一颗 LED 的状态
        if i == 0:
            led_pin_list[num - 1].value(0)
        # 如果这颗 LED 不是第一个，则需要改变它之前一颗 LED 的状态
        else:
            led_pin_list[i - 1].value(0)

        # 延时 0.2 秒
        time.sleep(0.1)