'''
该程序作用是使用无源蜂鸣器与 6 个按键实现电子琴效果，并弹奏小星星
在线文档：https://docs.geeksman.com/esp32/MicroPython/25.esp32-micropython-buzzer.html
'''
import time
from machine import Pin, PWM


# 定义音符对应的频率
tone_list = [262, 294,330, 350, 393, 441, 495]


# 定义无源蜂鸣器 PWM 控制对象
pos_buzzer = PWM(Pin(23, Pin.OUT))

# 定义按键对象
button_1 = Pin(25, Pin.IN, Pin.PULL_UP)
button_2 = Pin(26, Pin.IN, Pin.PULL_UP)
button_3 = Pin(27, Pin.IN, Pin.PULL_UP)
button_4 = Pin(14, Pin.IN, Pin.PULL_UP)
button_5 = Pin(12, Pin.IN, Pin.PULL_UP)
button_6 = Pin(13, Pin.IN, Pin.PULL_UP)
button_list = [button_1, button_2, button_3, button_4,
               button_5, button_6]

# 初始化音符频率
tone = 0


while True:
    pos_buzzer.duty(1000)
    for tone in tone_list:
        pos_buzzer.freq(tone)
        time.sleep(1)
    # 检测哪个按键触发
#     for i in range(len(button_list)):
#         if not button_list[i].value():
#             tone = tone_list[i]
#     
#     # 蜂鸣器发声
#     if tone:
#         pos_buzzer.duty(1000)
#         pos_buzzer.freq(tone)
#     else:
#         pos_buzzer.duty(0)
#     
#     tone = 0
#     time.sleep_ms(10)
