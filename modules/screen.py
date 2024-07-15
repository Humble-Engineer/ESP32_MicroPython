import binascii
from machine import UART
from time import sleep

class TjcUart:
    
    def __init__(self,id,baudrate,tx,rx,begin,end,num_pos,num_neg):
        
        #串口通信设置
        self.id   = id
        self.baud = baudrate
        self.tx   = tx
        self.rx   = rx
        
        #数据帧格式（帧头、帧尾、正数标志、负数标志）
        #除以上部分一般数据得到后转换为字符
        self.begin     = begin
        self.end       = end
        self.num_pos   = num_pos
        self.num_neg   = num_neg

        #实例化self.uart2进行通讯（tx接蓝线，rx接黄线）
        self.uart = UART(self.id, baudrate=self.baud, tx=self.tx, rx=self.rx)
        
        print("显示屏串口初始化完成！",end='\n')

    #发送字符串命令到串口
    def send(self,string):

        #写入串口屏指令
        self.uart.write(string)
        #发送帧尾
        code=[0xff,0xff,0xff]
        self.uart.write(bytes(code))
        
        #print("已发送串口屏命令：",end='')
        #print(string,end='\n')
        

    def receive(self):# 接收串口原始数据
        if self.uart.any():
            
            #一直读取，直到读取到帧头
            while self.uart.any():
                b = '' 
                head=str(binascii.hexlify(self.uart.read(1)))  #16进制表示方式的bytes数据，转换成字符串
                a=head
                for e in range(0, len(a)):  # 遍历字符串a
                    if e > 1 and e < 4:  # 去掉字符串无用的头尾（b'ff'）去掉b''，留下ff  
                        b = b + a[e]  # 当前b='ff'
                head=int(b,16)  # 将16进制表示的字符串，转换成hex数据  当前re[i]=0xFF
                
                if chr(head) == self.begin:
                    break
            
            #如果后面还有内容，说明是数据
            if self.uart.any():
                
                Len=self.uart.any()  # 串口缓存区内容长度
                re=[0]*Len  # 创建对应长度的列表
                for i in range(Len):  # 循环读取
                    b = '' 
                    re[i]=str(binascii.hexlify(self.uart.read(1)))  #16进制表示方式的bytes数据，转换成字符串
                    a=re[i]
                    for e in range(0, len(a)):  # 遍历字符串a
                        if e > 1 and e < 4:  # 去掉字符串无用的头尾（b'ff'）去掉b''，留下ff  
                            b = b + a[e]  # 当前b='ff'
                    re[i]=int(b,16)  # 将16进制表示的字符串，转换成hex数据  当前re[i]=0xFF


                    if chr(re[i]) == self.end:
                        cmd_len = i
                        re_new=[0]*(cmd_len)
                        for j in range(cmd_len):
                            re_new[j]=re[j]
                        break 
                 
                #print(re) #打印出接收到的数据
                return re_new  #此时的re数组存储的就是各字符的10进制ascii码
            
            #没有东西说明无有效数据
            else :
                print("此数据帧无有效数据！",end='\n')
                return None

    #接收到的数据解码
    def decode(self,msg):
        
        #如果读到了的话
        if msg != None:
            
            #打印出以10进制int类型表示的ascii码
            #print("原始数据:",end='')
            #print(msg)
            
            #用于储存是否读取到字符或数字
            str_flag=False
            num_flag=False
            
            #用于储存读取到字符和数字
            string = ""
            number = 0
            
            #解码并分离数据
            i=0
            while i<len(msg):
                
                #正整数标志位“#”，ASCII码为35
                if chr(msg[i]) == self.num_pos:
                    num_flag = True
                    #计算出这个整型的具体数值
                    number = 0
                    if msg[i+1] != None:
                        number += msg[i+1]
                    if msg[i+2] != None:
                        number += 2**8*msg[i+2]
                    if msg[i+3] != None:
                        number += 2**16*msg[i+3]
                    if msg[i+4] != None:
                        number += 2**32*msg[i+3]
                    #number = msg[i+1]+256*msg[i+2]+65536*msg[i+3]+4294967296*msg[i+4]
                    #跳过存储这个整型的4字节，接着读后面部分
                    i = i+4
                
                #负整数标志位“$”，ASCII码为36
                elif chr(msg[i]) == self.num_neg:
                    num_flag = True
                    #计算出这个整型的具体数值
                    number = 0
                    if msg[i+1] != None:
                        number += msg[i+1]
                    if msg[i+2] != None:
                        number += 2**8*msg[i+2]
                    if msg[i+3] != None:
                        number += 2**16*msg[i+3]
                    if msg[i+4] != None:
                        number += 2**32*msg[i+3]
                    #number = msg[i+1]+256*msg[i+2]+65536*msg[i+3]+4294967296*msg[i+4]
                    #将数字取反（因为是$作为标志符认为是负的）
                    number = -number
                    #跳过存储这个整型的4字节，接着读后面部分
                    i = i+4
                
                #其他就认为是字符，将它们连成字符串
                else:
                    str_flag = True
                    string += chr(msg[i])
                    
                i=i+1
            
            if str_flag:
                #print("解码字符:",end='')
                #print(string)
                pass
            
            if num_flag:
                #print("解码数字:",end='')
                #print(number)
                pass
            
            #返回字符串和参数   
            if str_flag and num_flag:
                #print("已返回字符串命令与参数！",end='\n')
                return string,number

            elif str_flag:
                #print("已返回字符串命令！",end='\n')
                return string,None
            
            elif num_flag:
                #print("已返回参数！",end='\n')
                return None,number
            
            else:
                print("未发现任何字符串命令与参数！",end='\n')
                return None,None



if __name__ == "__main__":
    
    #导入时间模块
    from time import sleep

    #实例化对象（设置使用的串口以及数据帧格式）
    tjc_uart = TjcUart(id=2,baudrate=115200,tx=17,rx=16,
               begin='|',end='~',num_pos='#',num_neg='$')

    #发送字符串命令,跳转到绘图界面
    tjc_uart.send("page draw")

    #循环发送绘图所需的点
    for j in range(4):
        for i in range(200):
            
            #向绘图控件s0的第1、2个通道分别写入数据
            tjc_uart.send("add s0.id,0,"+str(i))
            #tjc_uart.send("add s0.id,1,"+str(200-i))
            
            sleep(0.02)

    #发送字符串命令,跳转到测试界面
    tjc_uart.send("page test")

    while 1:

        #接收初始信息
        org_recv = tjc_uart.receive()
        #获取初始信息的解码
        cmd_recv = tjc_uart.decode(org_recv)
        
        #打印解码信息
        if cmd_recv != None:
            print(cmd_recv)

        sleep(2)





