'''
该程序作用是使用 SPI / SoftSPI 在 OLED 屏幕上显示 Hello World
在线文档：https://docs.geeksman.com/esp32/MicroPython/13.esp32-micropython-spi-oled.html
'''
from machine import Pin, SoftSPI
from libs.ssd1306 import SSD1306_SPI


# 定义对应的管脚对象
spi = SoftSPI(sck=Pin(18), mosi=Pin(13), miso=Pin(19))

# 创建 OLED 对象
oled = SSD1306_SPI(width=128, height=64, spi=spi, dc=Pin(2),
                   res=Pin(15), cs=Pin(4))

# 清屏
oled.fill(0)

# 画点
# oled.pixel(30, 30, 1)
# oled.pixel(30, 31, 1)
# oled.pixel(30, 32, 1)
# oled.pixel(30, 33, 1)
# oled.pixel(30, 34, 1)
# oled.pixel(30, 35, 1)

# 画方块

# for x in range(30, 61):
#     for y in range(30, 61):
#         oled.pixel(x, y, 1)

# 打印 Hello world 在屏幕上
oled.text('Hello, world!', 10, 38)

# 显示内容
oled.show()