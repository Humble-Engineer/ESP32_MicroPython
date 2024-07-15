from machine import PWM,Pin
from time import sleep

class MOTOR:
    
    def __init__(self,spd,dir,ena):
        
        #储存速度引脚作为属性
        self.spd_pin = spd
        #储存方向引脚作为属性
        self.dir_pin = dir
        #储存急停引脚作为属性
        self.ena_pin  = ena
        
        #默认转速为0(单位:转/每分钟)
        self.spd_value = 0
        #低电平(False)表示逆时针旋转
        self.dir_value = True
        #低电平(False)表示急停
        self.ena_value  = True
        
        #初始化两个IO口用于控制方向和急停
        self.dir = Pin(self.dir_pin,Pin.OUT)
        self.ena = Pin(self.ena_pin,Pin.OUT)
        
        #写入默认状态
        self.dir.value(self.dir_value)
        self.ena.value(self.ena_value)
        
        #设置默认PWM频率
        self.freq = 1000
        #基于默认转速计算PWM波的占空比
        self.duty = 0
        
        #PWM对象初始化(注意此通道的PWM占用的定时器)
        self.pwm = PWM(Pin(self.spd_pin),freq=self.freq,duty=self.duty)
        
        print("离心电机初始化完成！",end='\n')
        
    def speed(self,spd):

        if spd < 0:
            spd = 0
            
        elif spd > 1980:
            spd = 1980

        self.spd_value = spd
        self.duty = int(1023*self.spd_value/1980)
        
        self.pwm.duty(self.duty)
        
    def clockwise(self):
        
        self.dir_value = True
        self.dir.value(self.dir_value)
            
    def anticlockwise(self):
        
        self.dir_value = False
        self.dir.value(self.dir_value)
        
    def run(self):
        
        self.ena_value = True
        self.ena.value(1)
        sleep(1)
        
    def stop(self):
        
        self.ena_value = False
        self.ena.value(0)
        sleep(1)



