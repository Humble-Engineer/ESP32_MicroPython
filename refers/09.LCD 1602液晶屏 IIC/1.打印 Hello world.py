'''
该程序作用是使用 SoftI2C 在 LCD 屏幕上显示 Hello World
在线文档：https://docs.geeksman.com/esp32/MicroPython/12.esp32-micropython-lcd1602.html
'''
from machine import Pin, SoftI2C
from libs.i2c_lcd import I2cLcd


# 定义硬件 I2C 控制对象
i2c = SoftI2C(sda=Pin(13), scl=Pin(14), freq=100000)


# 获取 I2C 设备地址
address = i2c.scan()[0]


# 定义 I2cLcd 对象
i2c_lcd = I2cLcd(i2c, address, 2, 16)


# 打印 Hello world
i2c_lcd.putstr("Hello, world!")