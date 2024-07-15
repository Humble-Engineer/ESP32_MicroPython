'''
该程序作用是使用 SPI / SoftSPI 在 OLED 屏幕上显示可以用按键控制的菜单
在线文档：https://docs.geeksman.com/esp32/MicroPython/13.esp32-micropython-spi-oled.html
'''
import time
from machine import Pin, SoftSPI
from libs.ssd1306 import SSD1306_SPI


# 定义 SoftSPI 对象
spi = SoftSPI(sck=Pin(18), mosi=Pin(13), miso=Pin(19))

# 定义 SSD1306 SPI 控制对象
oled = SSD1306_SPI(width=128, height=64, spi=spi,
                   dc=Pin(2), res=Pin(15), cs=Pin(4))

# 定义 按键输入引脚对象，并配置上拉电阻
button_up = Pin(12, Pin.IN, Pin.PULL_UP)
button_down = Pin(14, Pin.IN, Pin.PULL_UP)


# 定义菜单选项
menu_items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
# 记录当前位置的值
current_item = 0


def display_menu(index):
    oled.fill(0)
    oled.text('Menu', 0, 0)
    oled.text('-' * 20, 0, 10)
    for i in range(len(menu_items)):
        if i == index:
            oled.text('> ' + menu_items[i], 0, 20 + i * 10)
        else:
            oled.text(menu_items[i], 0, 20 + i * 10)
    oled.show()
    
# 初始化显示屏幕状态
display_menu(current_item)

while True:
    if not button_up.value():
        current_item = (current_item + 1) % len(menu_items)
        display_menu(current_item)
    if not button_down.value():
        current_item = (current_item - 1) % len(menu_items)
        display_menu(current_item)
    time.sleep(0.1)
        

