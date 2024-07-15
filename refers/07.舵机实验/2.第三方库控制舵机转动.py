'''
该程序作用是使用 PWM 模块控制舵机转动
在线文档：https://docs.geeksman.com/esp32/MicroPython/10.esp32-micropython-servo.html
'''
import time
from machine import Pin
from libs.servo import Servo


# 定义舵机控制对象
my_servo = Servo(Pin(13), max_us=2500)


# 程序入口
if __name__ == '__main__':
    while True:
        my_servo.write_angle(0)
        time.sleep(0.5)
        my_servo.write_angle(45)
        time.sleep(0.5)
        my_servo.write_angle(90)
        time.sleep(0.5)
        my_servo.write_angle(135)
        time.sleep(0.5)
        my_servo.write_angle(180)
        time.sleep(0.5)



