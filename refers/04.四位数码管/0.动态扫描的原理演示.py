'''
该程序作用是为了演示动态扫描的原理，让大家对动态扫描有更清晰的认识。
在线文档：https://docs.geeksman.com/
'''

import time
from machine import Pin


# 定义位选线引脚对象
seg_1 = Pin(5, Pin.OUT)
seg_2 = Pin(18, Pin.OUT)
seg_3 = Pin(19, Pin.OUT)
seg_4 = Pin(21, Pin.OUT)

seg_list = [seg_1, seg_2, seg_3, seg_4]

# 定义段选线对象
a = Pin(32, Pin.OUT)
b = Pin(25, Pin.OUT)
c = Pin(27, Pin.OUT)
d = Pin(12, Pin.OUT)
e = Pin(13, Pin.OUT)
f = Pin(33, Pin.OUT)
g = Pin(26, Pin.OUT)
dp = Pin(14, Pin.OUT)

# 将对应的引脚对象存储到列表
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


# 显示数字的函数
def display_number(number):
    # 逻辑电平列表
    logic_list = number_dict.get(number)

    if logic_list:
        for i in range(len(logic_list)):
            led_list[i].value(logic_list[i])

        
# 清空位选线函数
def clear_seg():
    # 清空所有的位选线，将所有位选线设置为高电平
    for seg in seg_list:
        seg.on()

# 清空段选线函数
def clear_led():
    # 清空所有的段选线，将所有段选线设置为低电平
    for led in led_list:
        led.on()

# 清空函数
def clear():
    clear_seg()
    clear_led()


if __name__ == '__main__':
    # 清空显示内容
    clear()
    
    # 延时时间，初始为 355ms
    count = 355
        
    while True:
        # seg_1 显示数字 1
        clear_seg()
        seg_1.off()
        display_number(1)
        time.sleep_ms(count)
    
        # seg_2 显示数字 2
        clear_seg()
        seg_2.off()
        display_number(2)
        time.sleep_ms(count)
        
        # seg_3 显示数字 3
        clear_seg()
        seg_3.off()
        display_number(3)
        time.sleep_ms(count)
    
        # seg_4 显示数字 4
        clear_seg()
        seg_4.off()
        display_number(4)
        time.sleep_ms(count)
        
        # 逐渐缩短延时时间
        if count > 10:
            if count > 110:
                count -= 50
            else:
                count -= 10




