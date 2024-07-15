'''
该程序的作用是使用 PS2 摇杆模块控制舵机
在线文档：https://docs.geeksman.com/esp32/MicroPython/22.esp32-micropython-ps2.html
'''
import time
from machine import Pin, ADC, PWM


# 定义摇杆引脚
ps2_x = ADC(Pin(15), atten=ADC.ATTN_11DB)
ps2_y = ADC(Pin(2), atten=ADC.ATTN_11DB)
ps2_button = Pin(4, Pin.IN)

# 定义舵机控制引脚
my_servo = PWM(Pin(13), freq=50)


while True:
    # 读取 X 轴模拟信号
    x_value = ps2_x.read()
    
    # 在一个周期内(20ms), 0.5ms -> 0°, 2.4ms -> 180°
    # 0.5/20 * 1024
    servo_angle = x_value/4095 *(2.4-0.5)/20 *1024 + 0.5/20 * 1024
    
    # duty 方法控制舵机转动，0-1023, 0°-> 0.5/20 * 1024;
    # 180° -> 2.4/20*1024;
    my_servo.duty(int(servo_angle))
    
    time.sleep(0.1)
    
    