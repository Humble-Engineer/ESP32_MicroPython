'''
该程序作用是使用面向对象的方法让四位数码管显示数字
在线文档：https://docs.geeksman.com/esp32/MicroPython/07.esp32-micropython-4-digits-7seg.html
'''

from common.four_digits_seg import Seg4Digit


if __name__ == '__main__':
    # 初始化 4 位数码管对象
    seg_object = Seg4Digit(seg_1=5, seg_2=18, seg_3=19, seg_4=21, a=32, b=25, c=27, d=12, e=13, f=33, g=26, dp=14)
    
    while True:
        seg_object.display_4_number(1234)