'''
共阳极数码管公共类
上传到 MicroPython 设备中的 common 文件夹下
'''
from machine import Pin



# 共阳极数码管公共类
class Seg:
    def __init__(self, a, b, c, d, e, f, g, dp):
        # 要求用户在调用的时候，填写段选的GPIO引脚
        self.a = Pin(a, Pin.OUT)
        self.b = Pin(b, Pin.OUT)
        self.c = Pin(c, Pin.OUT)
        self.d = Pin(d, Pin.OUT)
        self.e = Pin(e, Pin.OUT)
        self.f = Pin(f, Pin.OUT)
        self.g = Pin(g, Pin.OUT)
        self.dp = Pin(dp, Pin.OUT)
        
        # 存放所有的段选线对象
        self.led_list = [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.dp]
        
        # 把所有的数字对应的逻辑电平存入字典中，顺序为abcdefgdp
        self.number_dict = {
            0: [0, 0, 0, 0, 0, 0, 1, 1],
            1: [1, 0, 0, 1, 1, 1, 1, 1],
            2: [0, 0, 1, 0, 0, 1, 0, 1],
            3: [0, 0, 0, 0, 1, 1, 0, 1],
            4: [1, 0, 0, 1, 1, 0, 0, 1],
            5: [0, 1, 0, 0, 1, 0, 0, 1],
            6: [0, 1, 0, 0, 0, 0, 0, 1],
            7: [0, 0, 0, 1, 1, 1, 1, 1],
            8: [0, 0, 0, 0, 0, 0, 0, 1],
            9: [0, 0, 0, 0, 1, 0, 0, 1],
        }
        
        # 对所有引脚进行初始化
        self.clear()
        
        
    def clear(self):
        # 对所有引脚初始化
        for led in self.led_list:
            led.value(1)
        

    def display_number(self, number):
        # 逻辑电平列表
        logic_list = self.number_dict.get(number)

        if logic_list:
            for i in range(len(logic_list)):
                self.led_list[i].value(logic_list[i])
                    
                    
                    
                    
                    
                    
                    
                    

