

from time import sleep,sleep_ms,sleep_us
from machine import Timer

#导入ldr.py中的LDR类
from modules.ldr import LDR
#设置模拟量读取引脚，定时器id和触发间隔（ms）
ldr = LDR(pin=34)

#导入motor.py中的MOTOR类
from modules.motor import MOTOR
#实例化一个电机对象（注意速度引脚PWM占用的定时器id）
motor = MOTOR(spd=33,ena=25,dir=26)

#导入stepper.py中的STEPPER类
from modules.stepper import STEPPER
#实例化一个步进电机对象
stepper = STEPPER(ena=4,dir=2,pul=15)


#导入sd.py中的SD类
from modules.sd import SD
#初始化sd卡的SPI总线
sd = SD(miso=13,mosi=12,sck=14,cs=27)


# 在screen.py模块中导入TjcUart这个类
from modules.screen import TjcUart
#实例化对象（设置使用的串口以及数据帧格式）
tjc_uart = TjcUart(id=2,baudrate=115200,tx=17,rx=16,
           begin='|',end='~',num_pos='#',num_neg='$')

#导入oled.py中的OLED类
from modules.oled import OLED
#配置oled显示器
oled = OLED(scl=18,sda=19,timer=(3,1000),
            
            top='ATP detecter',
            top_site=(15,0),
            
            sub1='Flash times:',
            sub1_site=(16,20),
            
            sub2="Last order:",
            sub2_site=(20,40),
            
            data1="",
            data1_site =(55,30),
            
            data2="",
            data2_site =(0,50))


#定时器回调函数
def timer_fun(tim):
    #读取光敏电阻，计算光强
    ldr.calculate()
    #print(ldr.voltage)
    
    #如果sd卡的写入许可打开的话（受串口命令控制）
    if sd.licence == True:
        #向SD卡写入数据
        sd.write('data.txt',str(ldr.voltage))
        #向绘图控件s0的第1、2个通道分别写入数据
        tjc_uart.send("add s0.id,0,"+str(int(40*ldr.voltage)))

#设置定时器编号
tim = Timer(1)
#启用定时器
tim.init(period=100,mode=Timer.PERIODIC,callback=timer_fun)

#启用OLED显示器
oled.start()
#串口屏跳转到主要界面
tjc_uart.send("page main")

while 1:

    #接收初始信息
    org_recv = tjc_uart.receive()
    #获取初始信息的解码
    cmd_recv = tjc_uart.decode(org_recv)
    
    #如果接收到的字符非空
    if cmd_recv != None:
        
        #打印解码信息
        print("串口屏命令:",end='')
        print(cmd_recv,end='\n')
        
        #显示到OLED上
        oled.data2 = str(cmd_recv[0])+','+str(cmd_recv[1])
        
        #依照字符串判断指令类型,执行对应操作
        
        #离心电机设置转速
        if cmd_recv[0] == "Motor_Speed":
            #将后面的数值作为速度写入
            motor.speed(cmd_recv[1])
            
        #离心电机急停设置
        elif cmd_recv[0] == "Motor_Run":
            if cmd_recv[1] == 1:
                motor.run()
            else:
                motor.stop()
        
        #离心电机方向设置
        elif cmd_recv[0] == "Motor_Dir":
            
            if cmd_recv[1] == 0:
                motor.anticlockwise()
                
            elif cmd_recv[1] == 1:
                motor.clockwise()
                
            else:
                print("离心电机未知指令！",end='\n')
                pass
        
        #步进电机方向设置
        elif cmd_recv[0] == "Stepper_Dir":
    
            if cmd_recv[1] == 0:
                
                #禁用OLED显示器（启用oled刷新会导致运动不连续）
                oled.stop()
                #步进电机执行运动
                stepper.location(rol=11,spd=260,dir="anticlock")
                #重新启用OLED显示器
                oled.start()
                
            elif cmd_recv[1] == 1:
                
                #禁用OLED显示器（启用oled刷新会导致运动不连续）
                oled.stop()
                #步进电机执行运动
                stepper.location(rol=11,spd=260,dir="clockwise")
                #重新启用OLED显示器
                oled.start()
                
            else:
                print("步进电机未知指令！",end='\n')
                pass
        
        #SD卡写入设置
        elif cmd_recv[0] == "Sd_Cmd":
            
            if cmd_recv[1] == 0:
                sd.licence = False
                print("停止向SD写入数据...",end='\n')
                
            elif cmd_recv[1] == 1:
                sd.licence = True
                print("开始向SD写入数据...",end='\n')
                
            elif cmd_recv[1] == 2:
                sd.clear('data.txt')
                print("清空SD中原有文件...",end='\n')
                
            else:
                print("SD卡未知指令！",end='\n')
                pass
        
        #如果字符串指令类型不存在则报错
        else :
            print("此指令无对应操作！",end='\n')
    
    #接收到空字符，表示串口空闲状态
    else :
        sleep_ms(100)
        pass





