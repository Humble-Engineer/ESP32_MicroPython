'''
该程序作用是使用按键实现开关灯效果
在线文档：https://docs.geeksman.com/esp32/MicroPython/08.esp32-micropython-button.html
'''
import time
from machine import Pin


# 定义按键输入引脚
pin_button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# 定义 LED 输出引脚
pin_led = Pin(2, Pin.OUT)

# 记录LED是否被修改过的状态
status = 0

while True:
    if pin_button.value() == 1:
        # 按键消抖
        time.sleep_ms(80)
        
        # 延时结束后，继续判断状态 
        if pin_button.value() == 1 and status == 0:
            pin_led.value(not pin_led.value())
            status = 1
        elif pin_button.value() == 0:
            status = 0
            
        
        
        
        
        
        
        

        