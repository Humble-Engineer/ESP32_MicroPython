'''
该程序说明：读写 SD 卡中的数据
在线文档：https://docs.geeksman.com/esp32/MicroPython/27.esp32-micropython-sd.html
'''
import os
from machine import Pin, SoftSPI
from libs.sdcard import SDCard


# 初始化 SD 卡对象
spi = SoftSPI(-1, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
sd = SDCard(spi, Pin(5))


# 挂载文件系统
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')

# 打印 SD 卡中的文件
print(f'文件列表：{os.listdir("/sd")}')

# 定义文件路径
file_path = '/sd/data.txt'

# 创建文件并写入数据
print("创建并写入数据")
with open(file_path, "w") as file:
    file.write("Hello, World!")
    
# 重新打印文件列表
print(f'文件列表：{os.listdir("/sd")}')


# 读取文件内容
print('读取文件内容')
with open(file_path, 'r') as file:
    content = file.read()
    print(content)

# 追加写入数据到现有文件中
print('追加写入数据')
with open(file_path, 'a') as file:
    file.write('追加写入数据')
    
# 读取文件内容
print('读取文件内容')
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
    
# 删除文件
print('删除文件')
os.remove(file_path)

# 重新打印文件列表
print(f'文件列表：{os.listdir("/sd")}')