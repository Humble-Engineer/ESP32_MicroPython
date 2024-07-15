import os
from machine import Pin, SoftSPI


from modules.drivers.sdcard import SDCard

# 接线说明:
# MISO -> GPTO 19
# MOSI -> GPIO 23
# SCK -> GPIO 18
# CS -> GPIO 5


class SD:
    
    #变量写在这里
    create_times = 0
    #定时器写入许可（需配合定时器使用）
    licence = False
    
    def __init__(self,miso,mosi,sck,cs):
        
        self.miso = miso
        self.mosi = mosi
        self.sck  = sck
        self.cs   = cs
        
        self.spi = SoftSPI(-1, miso=Pin(miso), mosi=Pin(mosi), sck=Pin(sck))
        self = SDCard(self.spi, Pin(cs))
        
        #self.licence = False
        
        #挂载sd卡
        self.vfs=os.VfsFat(self)
        os.mount(self.vfs,'/sd')
        print('SD卡储存模块挂载完成！',end='\n')
        
    def view(self):
        
        #读取当前根目录下的文件
        #print('当前根目录下的文件:{}'.format(os.listdir()))
        
        #跳转到sd文件夹下
        os.chdir('sd')
        
        #读取SD卡目录下的文件
        print('SD卡中的文件:{}'.format(os.listdir()))
        

    
    def write(self,filename,data):
        
        #生成需要写入的路径
        path = "/sd/" + filename
        
        #打开路径'w'表示覆盖写入，'a'表示追加写入
        with open(path,"a") as f:
            f.write(data+"\n")
            
    def clear(self,filename):
        
        #生成需要写入的路径
        path = "/sd/" + filename
        
        #打开路径'w'表示覆盖写入，'a'表示追加写入
        with open(path,"w") as f:
            f.write("")
            
if __name__ == "__main__":
    
    #初始化sd卡的SPI总线
    sd = SD(miso=13,mosi=12,sck=14,cs=27)
    #查看sd卡中根目录下的文件
    sd.view()

    #向'文件名'写入'内容'，没有此文件名会自动生成
    sd.write('test0.txt','hello world!')
    sd.write('test1.txt',str(114514))
    sd.write('test2.txt',str(3.14159))

