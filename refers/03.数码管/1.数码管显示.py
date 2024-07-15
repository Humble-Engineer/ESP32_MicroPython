'''
该程序作用是让一位数码管显示数字 0~9
在线文档：https://docs.geeksman.com/esp32/MicroPython/06.esp32-micropython-7segment.html
'''

import time
from machine import Pin


# 定义不同段选线对应的引脚对象
a = Pin(4, Pin.OUT)
b = Pin(5, Pin.OUT)
c = Pin(19, Pin.OUT)
d = Pin(21, Pin.OUT)
e = Pin(22, Pin.OUT)
f = Pin(2, Pin.OUT)
g = Pin(15, Pin.OUT)
dp = Pin(18, Pin.OUT)

# 存放所有的段选线对象
led_list = [a, b, c, d, e, f, g, dp]

# 对所有引脚初始化
for led in led_list:
    led.value(1)

# 显示数字 1
# b.value(0)
# c.value(0)

# 显示数字 2
# a.value(0)
# b.value(0)
# g.value(0)
# e.value(0)
# d.value(0)

# 把所有的数字对应的逻辑电平存入字典中，顺序为abcdefgdp
number_dict = {
    0: [0, 0, 0, 0, 0, 0, 1, 1],
    1: [1, 0, 0, 1, 1, 1, 1, 1],
    2: [0, 0, 1, 0, 0, 1, 0, 1],
    3: [0, 0, 0, 0, 1, 1, 0, 1],
    4: [1, 0, 0, 1, 1, 0, 0, 1],
    5: [0, 1, 0, 0, 1, 0, 0, 1],
    6: [0, 1, 0, 0, 0, 0, 0, 1],
    7: [0, 0, 0, 1, 1, 1, 1, 1],
    8: [0, 0, 0, 0, 0, 0, 0, 1],
    9: [0, 0, 0, 0, 1, 0, 0, 1],
}

def display_number(number):
    # 逻辑电平列表
    logic_list = number_dict.get(number)

    if logic_list:
        for i in range(len(logic_list)):
            led_list[i].value(logic_list[i])


# display_number(4)

for i in range(10):
    display_number(i)
    time.sleep(0.5)
