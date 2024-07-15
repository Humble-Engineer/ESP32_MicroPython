'''
该程序作用是使用行列扫描法检测按键, 实现密码校验功能
在线文档：https://docs.geeksman.com/esp32/MicroPython/26.esp32-micropython-keyboard.html
'''
import time
from machine import Pin, SoftI2C
from libs.i2c_lcd import I2cLcd


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

# 定义 I2C 控制对象
i2c = SoftI2C(sda=Pin(14), scl=Pin(27), freq=100000)

# 获取 I2C 设备地址
address = i2c.scan()[0]

# 定义 I2CLCD 对象
i2c_lcd = I2cLcd(i2c, address, 2, 16)


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

# 密码
password = '123456'
# 输入的密码
pwd_input = ''

# 第一行显示提示词
i2c_lcd.putstr('Enter Password:\n')

while True:
    key = read_keypad()
    
    if key is not None:
        # 重置屏幕内容
        i2c_lcd.clear()
        # 第一行显示提示词
        i2c_lcd.putstr('Enter Password:\n')
        if key == 'D' and pwd_input != '':
            pwd_input = pwd_input[:-1]
        elif key == '*':
            # 校验密码
            if pwd_input == password:
                i2c_lcd.putstr('Correct!')
            else:
                i2c_lcd.putstr('Wrong!')
            # 重置输入框
            pwd_input = ''
        # 非特殊案件打印在屏幕上
        elif key != 'D' and len(pwd_input) < 15:
            pwd_input += key
        
        # 打印密码
        i2c_lcd.putstr(pwd_input)
            
        
    # 延时 0.2s
    time.sleep(0.2)


