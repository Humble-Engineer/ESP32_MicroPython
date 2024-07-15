'''
该程序作用是让 LED 依次点亮后依次熄灭
在线文档：https://docs.geeksman.com/esp32/MicroPython/05.esp32-micropython-water-lamp.html
'''

import time
from machine import Pin

# # 定义所有的 LED 控制引脚
# led_1 = Pin(13, Pin.OUT)
# led_2 = Pin(12, Pin.OUT)
# led_3 = Pin(14, Pin.OUT)
# led_4 = Pin(27, Pin.OUT)
# led_5 = Pin(26, Pin.OUT)
# 
# # 定义 LED 对象列表
# led_pin_list = [led_1, led_2, led_3, led_4, led_5]

# 定义 GPIO 引脚对象
pin_index_list = [13, 12, 14, 27, 26]

# 定义 LED 管脚对象列表
led_pin_list = []

# 添加 LED 引脚对象
for i in pin_index_list:
    led_pin_list.append(Pin(i, Pin.OUT))

# print(led_pin_list)

# 初始化所有引脚对象
for led_pin in led_pin_list:
    led_pin.off()


while True:
    # 逐个改变 LED 状态
    for led_pin in led_pin_list:
        led_pin.value(not led_pin.value())
        # 延时 0.05s
        time.sleep(0.05)



