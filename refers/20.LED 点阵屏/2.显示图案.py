'''
该程序作用是在点阵屏上显示图案
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


# 定义图案的逻辑列表
hex_list = [0x00,0x66,0xFF,0xFF,0xFF,0x7E,0x3C,0x18]

# 定义逻辑值列表
logic_list = []

# 格式化逻辑列表
for hex in hex_list:
    logic = bin(hex).replace('0b', '')
    
    # 补 0
    while len(logic) < 8:
        logic = '0' + logic
    logic_list.append(logic)
    
# 显示图像
while True:
    for i in range(8):        
        for j in range(8):
            col_list[j].value(int(logic_list[i][j]))
            
        row_list[i].value(0)
        time.sleep_ms(1)
        row_list[i].value(1)
    
    
    
    
    

