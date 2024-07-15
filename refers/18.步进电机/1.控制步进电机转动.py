'''
该程序作用是驱动步进电机转动指定步数
在线文档：https://docs.geeksman.com/esp32/MicroPython/21.esp32-micropython-step-motor.html
'''
import time
from machine import Pin


# 定义管教对象
a = Pin(13, Pin.OUT)
b = Pin(12, Pin.OUT)
c = Pin(14, Pin.OUT)
d = Pin(27, Pin.OUT)

# 定义延时
delay_time = 2


# print('单四拍模式')
# for i in range(step):
#     a.value(1)
#     b.value(0)
#     c.value(0)
#     d.value(0)
#     time.sleep_ms(delay_time)
#     
#     a.value(0)
#     b.value(1)
#     c.value(0)
#     d.value(0)
#     time.sleep_ms(delay_time)
#     
#     a.value(0)
#     b.value(0)
#     c.value(1)
#     d.value(0)
#     time.sleep_ms(delay_time)
#     
#     a.value(0)
#     b.value(0)
#     c.value(0)
#     d.value(1)
#     time.sleep_ms(delay_time)

# print('双四拍模式')
# for i in range(256):
#     a.value(1)
#     b.value(1)
#     c.value(0)
#     d.value(0)
#     time.sleep_ms(delay_time)
#     
#     a.value(0)
#     b.value(1)
#     c.value(1)
#     d.value(0)
#     time.sleep_ms(delay_time)
#     
#     a.value(0)
#     b.value(0)
#     c.value(1)
#     d.value(1)
#     time.sleep_ms(delay_time)
#     
#     a.value(1)
#     b.value(0)
#     c.value(0)
#     d.value(1)
#     time.sleep_ms(delay_time)

# print('双四拍模式反转')
# for i in range(256):
#     a.value(1)
#     b.value(1)
#     c.value(0)
#     d.value(0)
#     time.sleep_ms(delay_time)
#     
#     a.value(1)
#     b.value(0)
#     c.value(0)
#     d.value(1)
#     time.sleep_ms(delay_time)
#     
#     a.value(0)
#     b.value(0)
#     c.value(1)
#     d.value(1)
#     time.sleep_ms(delay_time)
#     
#     a.value(0)
#     b.value(1)
#     c.value(1)
#     d.value(0)
#     time.sleep_ms(delay_time)

print('八拍模式')
for i in range(256):
    a.value(1)
    b.value(0)
    c.value(0)
    d.value(0)
    time.sleep_ms(delay_time)
    
    a.value(1)
    b.value(1)
    c.value(0)
    d.value(0)
    time.sleep_ms(delay_time)
    
    a.value(0)
    b.value(1)
    c.value(0)
    d.value(0)
    time.sleep_ms(delay_time)
    
    a.value(0)
    b.value(1)
    c.value(1)
    d.value(0)
    time.sleep_ms(delay_time)
    
    a.value(0)
    b.value(0)
    c.value(1)
    d.value(0)
    time.sleep_ms(delay_time)
    
    a.value(0)
    b.value(0)
    c.value(1)
    d.value(1)
    time.sleep_ms(delay_time)
    
    a.value(0)
    b.value(0)
    c.value(0)
    d.value(1)
    time.sleep_ms(delay_time)
    
    a.value(1)
    b.value(0)
    c.value(0)
    d.value(1)
    time.sleep_ms(delay_time)
    

# 清除所有状态
a.value(0)
b.value(0)
c.value(0)
d.value(0)

    