# 导入运行必要的标准库
from machine import Pin,ADC

class LDR:
    
    def __init__(self,pin):
        
        # 按参数库中的预设要求配置引脚
        self.adc = ADC(Pin(pin))

        self.GAMMA = 0.7
        self.RL10 = 50
        
        self.lux = 0
        self.voltage = 0
        
    
        print("光敏电阻初始化完成！",end='\n')

    # 回调函数
    def calculate(self):

        anologValue = self.adc.read()
        voltage = anologValue/4096.0*5
        resistance = 2000*voltage/(1-voltage/5)
        lux = pow(self.RL10*1e3*pow(10,self.GAMMA)/resistance,(1/self.GAMMA))
            
        self.lux = lux
        self.voltage = voltage

        #print(self.lux)
        #print(self.voltage)

if __name__ == "__main__":
    
    from time import sleep
    
    #设置模拟量读取引脚，定时器id和触发间隔（ms）
    ldr = LDR(pin=34)

    while 1:
        ldr.calculate()
        print(ldr.voltage)
        sleep(1)
    
