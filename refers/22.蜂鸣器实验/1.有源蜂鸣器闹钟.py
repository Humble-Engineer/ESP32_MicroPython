'''
该程序作用是使用蜂鸣器与按键实现闹钟功能
在线文档：https://docs.geeksman.com/esp32/MicroPython/25.esp32-micropython-buzzer.html
'''
import time
from machine import Pin, Timer


# 定义控制引脚对象
button = Pin(13, Pin.IN, Pin.PULL_UP)
active_buzzer = Pin(22, Pin.OUT)


# 定义 Button 的外部中断
def button_irq(button_obj):
    time.sleep_ms(10)
    if not button.value():
        active_buzzer.off()

# 定义定时器中断回调函数
def timer_irq(timer_obj):
    active_buzzer.value(1)
    

# 定义定时器
timer = Timer(0)
# 初始化定时器，设置闹钟开启时间
timer.init(period=5000, mode=Timer.ONE_SHOT, callback=timer_irq)
# 设置button 外部中断，打断时钟
button.irq(button_irq, Pin.IRQ_FALLING)