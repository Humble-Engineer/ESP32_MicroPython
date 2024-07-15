'''
该程序作用是在 LCD1602 屏幕上显示实时时间
在线文档：https://docs.geeksman.com/esp32/MicroPython/17.esp32-micropython-rtc.html
'''
import time
from machine import Pin, RTC, SoftI2C, Timer
from libs.i2c_lcd import I2cLcd


# 定义 SoftI2C 对象，
i2c = SoftI2C(sda=Pin(14), scl=Pin(13), freq=100000)


# 获取从机地址
print(f'LCD 设备列表：{i2c.scan()}')
address = i2c.scan()[0]

# 定义 I2cLcd 对象
lcd = I2cLcd(i2c, address, 2, 16)


# 定义 RTC 控制对象
rtc = RTC()

# 定义星期字符串列表
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


# 定义定时器中断函数
def timer_irq(timer_obj):
    date_time = rtc.datetime()
    lcd.clear()
    lcd.putstr('%d-%02d-%02d   %s\n' % (date_time[0], date_time[1],
                                     date_time[2], week[date_time[3]],))
    lcd.putstr('        %02d:%02d:%02d' % (date_time[4], date_time[5],
                                   date_time[6]))

# 初始化定时器对象
timer = Timer(0)

timer.init(mode=Timer.PERIODIC, period=1000, callback=timer_irq)





