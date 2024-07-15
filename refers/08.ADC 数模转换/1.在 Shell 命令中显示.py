'''
该程序说明：在 Shell 中显示 ADC 的值
在线文档：https://docs.geeksman.com/esp32/MicroPython/11.esp32-micropython-adc.html
'''
import time
from machine import Pin, ADC


# 定义 ADC 对象
adc = ADC(Pin(26))

# 配置衰减器 11db
adc.atten(ADC.ATTN_11DB)

while True:
    print(f'adc: {adc.read()}')
    time.sleep(0.1)