'''
该程序作用是把连接 WiFi 的代码封装成函数，开机自连 WiFi
在线文档：https://docs.geeksman.com/esp32/MicroPython/17.esp32-micropython-wifi.html
'''
from common.wifi import wifi_connect


# 定义 WIFI 的账号密码
ssid = 'GeeksMan'
password = '123456qq.'

# 连接 WiFi
wifi_connect(ssid, password)