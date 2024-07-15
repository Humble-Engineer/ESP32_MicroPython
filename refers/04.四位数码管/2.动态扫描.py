'''
该程序作用是让四位数码管显示数字
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

# 四位数码管显示函数
def display_4_number(number):
    # 格式化数字
    if number <= 9999:
#         # 获取第四位
#         seg_4_number = number % 10
#         number //= 10	# number = number // 10
#         print(seg_4_number)
#         
#         # 获取第 3 位
#         seg_3_number = number % 10
#         number //= 10	# number = number // 10
#         print(seg_3_number)
#         
#         # 获取第 2 位
#         seg_2_number = number % 10
#         number //= 10	# number = number // 10
#         print(seg_2_number)
#         
#         # 获取第 1 位
#         seg_1_number = number % 10
#         number //= 10	# number = number // 10
#         print(seg_1_number)
#         
#         number_list = [seg_1_number, seg_2_number, seg_3_number, seg_4_number]
        
        # 初始化每个位置对应数字的列表
        number_list = []
        # 使用循环获取数字列表
        for i in range(4):
            number_list.insert(0, number % 10)
            number //= 10
#         print(number_list)
        
        # 显示数字
        for i in range(4):
            display_number(i, number_list[i])
            time.sleep_ms(5)
    
    
    
if __name__ == '__main__':
    while True:
        display_4_number(5489)