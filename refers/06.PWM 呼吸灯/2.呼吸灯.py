'''
该程序作用是使用按键实现开关灯效果
在线文档：https://docs.geeksman.com/esp32/MicroPython/09.esp32-micropython-pwm.html
'''
import time
from machine import Pin, PWM


# 定义 PWM 对象
led = PWM(Pin(12, Pin.OUT), freq=1000)

while True:
    
    # 由暗到亮
    for i in range(1024):
        led.duty(i)
        time.sleep_ms(1)

    # 由亮到灭
    for i in range(1023, 0, -1):
        led.duty(i)
        time.sleep_ms(1)




