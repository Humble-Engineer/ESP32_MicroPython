'''
该程序作用是让四位数码管按顺序让所有位置显示0~9，时间间隔为0.2s
在线文档：https://docs.geeksman.com/esp32/MicroPython/07.esp32-micropython-4-digits-7seg.html
'''

import time
from machine import Pin


# 定义位选线引脚对象
seg_1 = Pin(5, Pin.OUT)
seg_2 = Pin(18, Pin.OUT)
seg_3 = Pin(19, Pin.OUT)
seg_4 = Pin(21, Pin.OUT)
# 定义位选线列表
seg_list = [seg_1, seg_2, seg_3, seg_4]

# 定义段选线引脚对象
a = Pin(32, Pin.OUT)
b = Pin(25, Pin.OUT)
c = Pin(27, Pin.OUT)
d = Pin(12, Pin.OUT)
e = Pin(13, Pin.OUT)
f = Pin(33, Pin.OUT)
g = Pin(26, Pin.OUT)
dp = Pin(14, Pin.OUT)


# 定义段选线列表
led_list = [a, b, c, d, e, f, g, dp]

# 共阴极数码管不同数字对应的逻辑电平
number_dict = {
    #  [a, b, c, d, e, f, g, dp]
    0: [1, 1, 1, 1, 1, 1, 0, 0],
    1: [0, 1, 1, 0, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1, 0],
    3: [1, 1, 1, 1, 0, 0, 1, 0],
    4: [0, 1, 1, 0, 0, 1, 1, 0],
    5: [1, 0, 1, 1, 0, 1, 1, 0],
    6: [1, 0, 1, 1, 1, 1, 1, 0],
    7: [1, 1, 1, 0, 0, 0, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1, 0],
    9: [1, 1, 1, 1, 0, 1, 1, 0],
}


# 清屏函数
def clear():
    # 初始化位选端
    for seg in seg_list:
        seg.on()

    # 初始化段选端
    for led in led_list:
        led.off()


def display_number(order, number):
    # 定义当前数字对应的逻辑电平列表
    logic_list = number_dict.get(number)
    
    if logic_list and 0 <= order < 4:
        # 清屏
        clear()
        # 指定要显示的位置，把电平拉低
        seg_list[order].off()
        # 显示数字
        for i in range(len(logic_list)):
            led_list[i].value(logic_list[i])


if __name__ == '__main__':
    # 让第 3 位显示数字 1
#     display_number(2, 1)
    for i in range(4):
        for j in range(10):
            display_number(i, j)
            time.sleep(0.2)


