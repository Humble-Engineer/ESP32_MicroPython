'''
该程序作用是使用无源蜂鸣器自动播放小星星
在线文档：https://docs.geeksman.com/esp32/MicroPython/25.esp32-micropython-buzzer.html
'''
import time
from machine import Pin, PWM


# 定义音符对应的频率
tone_list = [262, 294,330, 350, 393, 441, 495]


# 定义无源蜂鸣器 PWM 控制对象
pos_buzzer = PWM(Pin(23, Pin.OUT))

# 乐谱列表
music = [1, 1, 5, 5, 6, 6, 5, 0,
         4, 4, 3, 3, 2, 2, 1, 0,
         5, 5, 4, 4, 3, 3, 2, 0,
         5, 5, 4, 4, 3, 3, 2, 0,
         1, 1, 5, 5, 6, 6, 5, 0,
         4, 4, 3, 3, 2, 2, 1, 0,]


# 自动播放
for i in music:
    pos_buzzer.duty(900)
    if i:
        pos_buzzer.freq(tone_list[i-1])
        time.sleep_ms(500)
        pos_buzzer.duty(0)
        time.sleep_ms(10)
        
# 占空比设置为0
pos_buzzer.duty(0)