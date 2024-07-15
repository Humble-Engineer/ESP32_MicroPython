from machine import Pin,PWM
from time import sleep,sleep_ms,sleep_us

class STEPPER:
    
    def __init__(self,ena,dir,pul):
        
        #蓝线使能
        self.ena_pin = ena
        #绿线方向
        self.dir_pin = dir
        #黄线脉冲
        self.pul_pin = pul
        
        self.ena = Pin(ena,Pin.OUT,0)
        self.dir = Pin(dir,Pin.OUT,0)
        
        #低电平使能
        self.ena.value(0)
        #顺时针转动
        self.dir.value(0)
        
        self.freq = 500
        self.duty = 100
        
        #构造一个pwm发生器，但是把占空比设置为零，先不启动
        self.pwm = PWM(Pin(self.pul_pin),freq=self.freq,duty=0)
        
        
        print("步进电机初始化完成！",end='\n')
        
    def speed_rmp(self,spd,dir):
        
        #根据输入的转向判断方向控制引脚的电平
        if dir == "clockwise":
            self.dir.value(1)
        else:
            self.dir.value(0)
        
        #构造pwm发生器，设置基本参数
        self.pwm = PWM(Pin(self.pul_pin),freq=self.freq,duty=self.duty)
        
        #计算该转速（rpm）下的频率
        self.freq = int(200*spd/60)
        #将频率参数写入到pwm发生器
        self.pwm.freq(self.freq)
        
    def location(self,rol,spd,dir):
        
        #先取消在脉冲引脚上的pwm输出
        self.pwm.deinit()
        
        #构造脉冲发生引脚为输出
        PUL = Pin(self.pul_pin,Pin.OUT,0)
        
        #根据输入的转向判断方向控制引脚的电平
        if dir == "clockwise":
            self.dir.value(1)
        else:
            self.dir.value(0)
        
        #计算每个脉冲的间隔时间（us）
        time_us = int(3*10**5/spd)

        for i in range(rol):
            for i in range(200):
                PUL.value(0)
                sleep_us(time_us)
                PUL.value(1)
    
    #电机旋转
    def start(self):
        
        self.ena.value(0)
    
    #电机停止
    def stop(self):
        
        self.ena.value(1)
        

if __name__ == "__main__":
    
    from time import sleep,sleep_ms,sleep_us
    
    #实例化一个步进电机对象
    stepper = STEPPER(ena=4,dir=2,pul=15)

    for i in range(1):
        
        #以300rmp的速度按逆时针方向旋转10圈
        stepper.location(rol=11,spd=260,dir="anticlock")
        sleep(2)

        #以300rmp的速度按顺时针方向旋转10圈
        stepper.location(rol=11,spd=260,dir="clockwise")
        sleep(2)
    
