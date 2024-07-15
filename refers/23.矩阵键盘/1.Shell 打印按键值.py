'''
该程序作用是使用行列扫描法检测按键状态并打印在 Shell 中
在线文档：https://docs.geeksman.com/esp32/MicroPython/26.esp32-micropython-keyboard.html
'''
import time
from machine import Pin


# 定义行输入引脚对象
row_pins = [Pin(19, Pin.IN, Pin.PULL_UP),
            Pin(18, Pin.IN, Pin.PULL_UP),
            Pin(5, Pin.IN, Pin.PULL_UP),
            Pin(17, Pin.IN, Pin.PULL_UP),]

# 定义列输出引脚对象
col_pins = [Pin(16, Pin.OUT),
            Pin(4, Pin.OUT),
            Pin(2, Pin.OUT),
            Pin(15, Pin.OUT),]


# 定义检测按键函数
def read_keypad():
    keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D'],
    ]
    
    # 行列扫描法检测按键
    for j, col_pin in enumerate(col_pins):
        # 将当前列设置为低电平
        col_pin.off()
        # 检测行引脚状态
        for i, row_pin in enumerate(row_pins):
            if row_pin.value() == 0:
                # 将当前列恢复为高电平
                col_pin.on()
                # 返回按下的按键
                return keys[i][j]
        # 将当前列恢复为高电平
        col_pin.on()


while True:
    key = read_keypad()
    
    if key is not None:
        print('按下的按键:', key)
        
    # 延时 0.1s
    time.sleep(0.1)