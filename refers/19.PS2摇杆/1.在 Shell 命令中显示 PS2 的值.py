'''
该程序说明：在 Shell 中显示 ADC 的值
在线文档：https://docs.geeksman.com/esp32/MicroPython/22.esp32-micropython-ps2.html
'''
import time
from machine import Pin, ADC


# 定义摇杆引脚
ps2_x = ADC(Pin(15), atten=ADC.ATTN_11DB)
ps2_y = ADC(Pin(2), atten=ADC.ATTN_11DB)
ps2_button = Pin(4, Pin.IN)


while True:
    print(f'x:{ps2_x.read()},y:{ps2_y.read()},z:{ps2_button.value()}')
    time.sleep(0.1)