'''
该程序作用是使用面向对象的方法让一位数码管显示数字 0~9
在线文档：https://docs.geeksman.com/esp32/MicroPython/06.esp32-micropython-7segment.html
'''

import time
from common.seg import Seg


if __name__ == '__main__':
    # 创建共阳极数码管对象
    seg_object = Seg(a=4, b= 5, c=19, d=21, e=22, f=2, g=15, dp=18)
    
    # 显示 0 - 9
    for i in range(10):
        seg_object.display_number(i)
        time.sleep(0.5)
