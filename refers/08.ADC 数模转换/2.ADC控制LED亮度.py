'''
该程序说明：使用 ADC 控制 LED 的亮度
在线文档：https://docs.geeksman.com/esp32/MicroPython/11.esp32-micropython-adc.html
'''
import time
from machine import Pin, PWM, ADC


# 定义 LED PWM 对象
led = PWM(Pin(13), freq=1000)

# 定义 ADC 对象
adc = ADC(Pin(26), atten=ADC.ATTN_11DB)


while True:
    led.duty_u16(adc.read_u16())
    print(f'{adc.read_u16()}')
    time.sleep(0.1)