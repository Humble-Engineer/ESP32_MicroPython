
from machine import Pin, SoftI2C, I2C, Timer

import time
import framebuf

# register definitions
SET_CONTRAST        = const(0x81)
SET_ENTIRE_ON       = const(0xa4)
SET_NORM_INV        = const(0xa6)
SET_DISP            = const(0xae)
SET_MEM_ADDR        = const(0x20)
SET_COL_ADDR        = const(0x21)
SET_PAGE_ADDR       = const(0x22)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP       = const(0xa0)
SET_MUX_RATIO       = const(0xa8)
SET_COM_OUT_DIR     = const(0xc0)
SET_DISP_OFFSET     = const(0xd3)
SET_COM_PIN_CFG     = const(0xda)
SET_DISP_CLK_DIV    = const(0xd5)
SET_PRECHARGE       = const(0xd9)
SET_VCOM_DESEL      = const(0xdb)
SET_CHARGE_PUMP     = const(0x8d)


class SSD1306:
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        # Note the subclass must initialize self.framebuf to a framebuffer.
        # This is necessary because the underlying data buffer is different
        # between I2C and SPI implementations (I2C needs an extra byte).
        self.poweron()
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00, # off
            # address setting
            SET_MEM_ADDR, 0x00, # horizontal
            # resolution and layout
            SET_DISP_START_LINE | 0x00,
            SET_SEG_REMAP | 0x01, # column addr 127 mapped to SEG0
            SET_MUX_RATIO, self.height - 1,
            SET_COM_OUT_DIR | 0x08, # scan from COM[N] to COM0
            SET_DISP_OFFSET, 0x00,
            SET_COM_PIN_CFG, 0x02 if self.height == 32 else 0x12,
            # timing and driving scheme
            SET_DISP_CLK_DIV, 0x80,
            SET_PRECHARGE, 0x22 if self.external_vcc else 0xf1,
            SET_VCOM_DESEL, 0x30, # 0.83*Vcc
            # display
            SET_CONTRAST, 0xff, # maximum
            SET_ENTIRE_ON, # output follows RAM contents
            SET_NORM_INV, # not inverted
            # charge pump
            SET_CHARGE_PUMP, 0x10 if self.external_vcc else 0x14,
            SET_DISP | 0x01): # on
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        x0 = 0
        x1 = self.width - 1
        if self.width == 64:
            # displays with width of 64 pixels are shifted by 32
            x0 += 32
            x1 += 32
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(x0)
        self.write_cmd(x1)
        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        self.write_framebuf()

    def fill(self, col):
        self.framebuf.fill(col)

    def pixel(self, x, y, col):
        self.framebuf.pixel(x, y, col)

    def scroll(self, dx, dy):
        self.framebuf.scroll(dx, dy)

    def text(self, string, x, y, col=1):
        self.framebuf.text(string, x, y, col)
        
class SSD1306_I2C(SSD1306):
    
    def __init__(self, width, height, i2c, addr=0x3c, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        # Add an extra byte to the data buffer to hold an I2C data/command byte
        # to use hardware-compatible I2C transactions.  A memoryview of the
        # buffer is used to mask this byte from the framebuffer operations
        # (without a major memory hit as memoryview doesn't copy to a separate
        # buffer).
        self.buffer = bytearray(((height // 8) * width) + 1)
        self.buffer[0] = 0x40  # Set first byte of data buffer to Co=0, D/C=1
        self.framebuf = framebuf.FrameBuffer1(memoryview(self.buffer)[1:], width, height)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80 # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_framebuf(self):
        # Blast out the frame buffer using a single I2C transaction to support
        # hardware I2C interfaces.
        self.i2c.writeto(self.addr, self.buffer)

    def poweron(self):
        pass
    
    
class OLED:
    
    def __init__(self,sda,scl,top,sub1,sub2,data1,data2,):
        
        #iic总线连接的单片机引脚
        self.scl = scl
        self.sda = sda
        
        self.i2c = I2C(1, scl=Pin(scl), sda=Pin(sda), freq=400000)
        
        #oled构造函数
        self.oled = SSD1306_I2C(128,64,self.i2c,addr=0x3c)
        
        #需要显示的总标题、子标题1和子标题2
        self.top_heading  = top
        self.sub_heading1 = sub1
        self.sub_heading2 = sub2
        
        #需要显示的两个数据
        self.data1 = data1
        self.data2 = data2
        
        #各个显示部分的位置（x,y）（单位：像素点）
        self.top_site   = [0,0]
        self.sub1_site  = [0,20]
        self.sub2_site  = [0,40]
        self.data1_site = [0,30]
        self.data2_site = [0,50]
        
        self.flash_time = 0
        
        print("OLED初始化完成！",end='\n')
        
        
    # 指定位置显示内容
    def display(self,string,x,y):
        self.oled.text(string,x,y)
        self.oled.show()

    # 清除屏幕显示
    def clear(self):
        self.oled.fill(0)
        
    # 屏幕显示
    def show(self):
        
        self.clear()
        
        #转换为字符串
        data1 = str(self.data1)
        data2 = str(self.data2)

        # 显示到特定位置
        self.display(self.top_heading,
                     int((128-8*len(self.top_heading))/2),
                     self.top_site[1])
        
        self.display(self.sub_heading1,
                     int((128-8*len(self.sub_heading1))/2),
                     self.sub1_site[1])
        
        self.display(self.sub_heading2,
                     int((128-8*len(self.sub_heading2))/2),
                     self.sub2_site[1])

        self.display(data1,
                     int((128-8*len(data1))/2),
                     self.data1_site[1])
        
        self.display(data2,
                     int((128-8*len(data2))/2),
                     self.data2_site[1],)
        
        
if __name__ == "__main__":
    
    try:
        
        #配置oled显示器
        oled = OLED(scl=22,sda=23,           
            top='OLED Monitor',    
            sub1='uart screen cmd:',
            sub2="system message:",
            data1="waitting...",
            data2="")
        #初始化完成提示
        oled.data2 = "oled ready!"
        oled.show()
    except:
        #没有插OLED就提示
        print("错误！未检测到OLED显示器...")

