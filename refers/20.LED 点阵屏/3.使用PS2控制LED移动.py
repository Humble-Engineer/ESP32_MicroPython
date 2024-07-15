'''
该程序作用是使用 PS2 控制 LED 移动小游戏
在线文档：https://docs.geeksman.com/esp32/MicroPython/23.esp32-micropython-led-matrix.html
'''
import time
from machine import Pin, ADC


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


# 定义摇杆引脚对象
ps2_x = ADC(Pin(15), atten=ADC.ATTN_11DB)
ps2_y = ADC(Pin(35), atten=ADC.ATTN_11DB)
ps2_button = Pin(34, Pin.IN)


# 初始化 LED 对象位置
led_pos = [4, 3]

# 容忍范围
tol = 300

while True:
    
    # 清除 LED 状态
    row_list[led_pos[0]].value(1)
    col_list[led_pos[1]].value(0)
    
    x_value = ps2_x.read()
    y_value = ps2_y.read()
    
    print(f'x: {x_value}, y: {y_value}')
    
    # 检测 X 轴状态
    if x_value > 4095 / 2 + tol and led_pos[0] > 0:
        led_pos[0] -= 1
    elif x_value < 4095 / 2 - tol and led_pos[0] < 7:
        led_pos[0] += 1
        
    # 检测 Y 轴状态
    if y_value > 4095 / 2 + tol and led_pos[1] < 7:
        led_pos[1] += 1
    elif y_value < 4095 / 2 - tol and led_pos[1] > 0:
        led_pos[1] -= 1
    
    # 显示 LED
    row_list[led_pos[0]].value(0)
    col_list[led_pos[1]].value(1)
    
    time.sleep_ms(500)
    
    
    
    
    
    
    

