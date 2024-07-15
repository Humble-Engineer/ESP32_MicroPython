'''
该程序作用是使用 PWM 模块控制舵机转动
在线文档：https://docs.geeksman.com/esp32/MicroPython/10.esp32-micropython-servo.html
'''
import time
from machine import Pin, PWM


# 定义 PWM 控制对象
my_servo = PWM(Pin(13))

# 定义舵机频率
my_servo.freq(50)

# 使用不同的占空比方法控制转动角度

# duty(), 0-1023
# 转动到 0°， 1023 * 0.5 / 20
my_servo.duty(int(1023*0.5/20))
time.sleep(1)

# duty_u16(), 0 - 65535
# 转动到 90°， 65535 * 1.5 / 20
my_servo.duty_u16(int(65535 * 1.5 / 20))


