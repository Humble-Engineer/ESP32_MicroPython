'''
该程序作用是掌握 PWM 模块的应用
在线文档：https://docs.geeksman.com/esp32/MicroPython/09.esp32-micropython-pwm.html
'''
from machine import Pin, PWM


# PWM 对象
led = PWM(Pin(12, Pin.OUT), freq=1000, duty=200)

# 获取频率
print(led.freq())

# 设置频率
led.freq(5000)
print(led.freq())

# 获取占空比
print('获取占空比', led.duty())

# 设置占空比
led.duty(100)
print('获取占空比', led.duty())





