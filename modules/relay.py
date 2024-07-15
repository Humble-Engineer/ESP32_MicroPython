from machine import Pin
from time import sleep

#默认继电器高电平触发
#工作电路电源正极接公共端（COM）
#用电器正极自常开触点处（NO）引出

class RELAY:
    
    def __init__(self,pin):
        
        self.pin = pin
    
    def set(self,state):
        
        self = Pin(self.pin,Pin.OUT)

        if state == "on":
            
            self.value(1)
            
        else :
            
            self.value(0)
            
            
if __name__ == "__main__":
    
    from time import sleep

    relay_stepper = RELAY(32)

    relay_stepper.set("on")
    sleep(2)
    relay_stepper.set("off")
