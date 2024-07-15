'''
该程序作用是连接 Wifi
在线文档：https://docs.geeksman.com/esp32/MicroPython/17.esp32-micropython-wifi.html
'''
import time
import network


# 定义 WIFI 的账号密码
ssid = 'GeeksMan'
password = '123456qq.'

# 创建 WIFI 连接对象
wlan = network.WLAN(network.STA_IF)

# 激活接口
wlan.active(True)

# 断开之前的链接
wlan.disconnect()

# 扫描允许访问的 WIFI
print('扫描周围信号源：', wlan.scan())

# 连接 WIFI
print("正在连接 WiFi", end="")
wlan.connect(ssid, password)

# 判断是否连接成功
while not wlan.isconnected():
    print('.', end='')
    time.sleep(0.1)

# 连接成功打印信息
print('\n连接成功！')





