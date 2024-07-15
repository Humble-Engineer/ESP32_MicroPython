'''
该程序作用是使用定时器和永真循环实现 LED 亮灭的效果
在线文档：https://docs.geeksman.com/esp32/MicroPython/16.esp32-micropython-timer.html
'''
import time
from machine import Pin, Timer


# 定义 LED 控制引脚对象
led_1 = Pin(2, Pin.OUT)
led_2 = Pin(4, Pin.OUT)


# 定义定时器对象
timer = Timer(0)

# 定义定时器中断回调函数
def timer_irq(timer_obj):
    led_1.value(not led_1.value())
    
# 初始化定时器对象
timer.init(mode=Timer.PERIODIC, period=1000, callback=timer_irq)

while True:
    led_2.value(not led_2.value())
    time.sleep(1.5)