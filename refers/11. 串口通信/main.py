'''
该程序作用是使用实现与 PC 端串口助手进行数据收发
在线文档：https://docs.geeksman.com/esp32/MicroPython/14.esp32-micropython-uart.html
'''
from machine import UART


# 定义 UART 控制对象
uart = UART(2, 115200)


# 发送数据到串口工具中
uart.write('Hello')


while True:
    if uart.any():
        text = uart.read(20)
        print(text)