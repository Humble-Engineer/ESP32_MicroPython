'''
该程序作用是循环遍历所有 LED, 检测一下是否所有的 LED 都可以正常工
在线文档：https://docs.geeksman.com/esp32/MicroPython/23.esp32-micropython-led-matrix.html
'''
import time
from machine import Pin


# 定义行引脚对象
row_1 = Pin(13, Pin.OUT)
row_2 = Pin(25, Pin.OUT)
row_3 = Pin(2, Pin.OUT)
row_4 = Pin(27, Pin.OUT)
row_5 = Pin(23, Pin.OUT)
row_6 = Pin(4, Pin.OUT)
row_7 = Pin(22, Pin.OUT)
row_8 = Pin(18, Pin.OUT)

# 定义行对象列表
row_list = [row_1, row_2, row_3, row_4, row_5, row_6, row_7
            , row_8]

# 定义列引脚对象
col_1 = Pin(26, Pin.OUT)
col_2 = Pin(21, Pin.OUT)
col_3 = Pin(19, Pin.OUT)
col_4 = Pin(12, Pin.OUT)
col_5 = Pin(5, Pin.OUT)
col_6 = Pin(14, Pin.OUT)
col_7 = Pin(33, Pin.OUT)
col_8 = Pin(32, Pin.OUT)

# 定义列对象列表
col_list = [col_1, col_2, col_3, col_4, col_5, col_6, col_7
            , col_8]


# 初始化所有行为高电平
for row in row_list:
    row.on()
    
# 初始化所有列为低电平
for col in col_list:
    col.off()


while True:
    # 嵌套循环遍历所有位置
    for row in row_list:
        # 把该行设置为低电平
        row.off()
        for col in col_list:
            # 把该列设置为高电平
            col.on()
            time.sleep(0.1)
            col.off()
        row.on()
            


