'''
该程序作用是使用外部中断控制按键输入
在线文档：https://docs.geeksman.com/esp32/MicroPython/15.esp32-micropython-interrupt.html
'''
import time
from machine import Pin


# 定义 PIN 引脚对象
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)


# 定义外部中断函数
def button_irq(button):
    # 按键消抖
    time.sleep_ms(10)
    if button.value() == 1:
        led.value(not led.value())
        
        
# 绑定中断函数
button.irq(button_irq, Pin.IRQ_RISING)