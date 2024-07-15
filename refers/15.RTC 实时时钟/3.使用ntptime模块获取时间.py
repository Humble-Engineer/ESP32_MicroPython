'''
该程序作用是使用 ntptime 模块获取时间
在线文档：https://docs.geeksman.com/esp32/MicroPython/17.esp32-micropython-rtc.html
'''
import ntptime
from machine import RTC
from common.wifi import wifi_connect


# 定义 RTC 对象
rtc = RTC()

# 连接 Wifi
ssid = 'GeeksMan'
password = '123456qq.'

wifi_connect(ssid, password)

# 从 NTP 服务器获取时间
ntptime.settime()

date_time = rtc.datetime()

print(f'显示北京时间：{date_time[0]}-{date_time[1]}-{date_time[2]} {date_time[4] + 8}:{date_time[5]}:{date_time[6]}')
