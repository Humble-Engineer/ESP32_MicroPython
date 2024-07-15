'''
该程序作用是创建热点
在线文档：https://docs.geeksman.com/esp32/MicroPython/17.esp32-micropython-wifi.html
'''
import network


# 创建热点对象
ap = network.WLAN(network.AP_IF)

# 激活热点
ap.active(True)

# 配置热点名称
ap.config(essid='ESP32')
