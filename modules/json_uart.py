import ujson
from machine import UART
import time

from collections import OrderedDict

class JSON_UART:
    
    def __init__(self, id, baud, tx, rx):
        
        # 储存串口的固有属性
        self.id = id
        self.baud = baud
        self.tx = tx
        self.rx = rx
        
        # 串口初始化
        self.uart = UART(self.id, baudrate=self.baud, tx=self.tx, rx=self.rx, bits=8)
    
        # 设置发送数据及其顺序（不设置就按内置的某一特定顺序）
        self.sand_data = OrderedDict([('id', str(id)), ('baud', str(baud)),
                                      ('tx', str(tx)), ('rx', str(rx)),
                                      ('state', "abnormal")  ])
        # 接收数据的存储变量
        self.recv_data = ''
        
    # 发送数据
    def send(self,data):
        
        # 将数据转换为JSON格式
        json_data = ujson.dumps(data)
        # 发送JSON数据
        self.uart.write(json_data + '\n')

    # 接收数据
    def recv(self):
        
        received_data = b''  # 使用字节串来存储接收到的数据
        storing_data = False  # 标志是否开始存储数据，用‘{’来激活

        while self.uart.any():
            char = self.uart.read(1)  # 先试着读取一个字符
            
            if char == b'{':  # 如果是json格式的起始字符“{”
                received_data += b'{' # 储存下来“{”
                storing_data = True   # 遇到 "{" 后开始存储数据
            
            elif storing_data:    # 如果已经开始存储字符了
                if char == b'}':  # 与末尾字符“}”比较，判断是否应该结束读取，开始解析
                    try:
                        # 尝试解析JSON数据
                        json_data = ujson.loads(received_data.decode())
                        return json_data
                    except Exception as e:
                        print("Error decoding JSON:", e)
                        return None
                elif char: # 不是结尾字符“}”就继续读取
                    received_data += char  # 将字符添加到接收到的数据中
                    
        return None

    # 执行json数据对应的操作
    def execute(self,data):
        if   data['order'] == "run":
            print("run:",data['value'])
        elif data['order'] == "stop":
            print("stop:",data['value'])
        else:
            print("default case")
        
# 配置串口
serial = JSON_UART(1,baud=115200,tx=21,rx=19)  # 根据硬件配置进行调整

# 修改或添加发送数据键值对
serial.sand_data['state'] = 'normal'
serial.sand_data['massage'] = 'Json uart initialized!'

serial.send(serial.sand_data)
print("Send data:", serial.sand_data)

while 1:
    # 等待一段时间，模拟其他操作
    time.sleep(0.1)
    # 接收数据(读取一个数据包，其余留在串口缓存区)
    serial.recv_data = serial.recv()
    # 处理接收到的数据
    if serial.recv_data != None :
        # 打印接收到的json数据
        print("Recv data:", serial.recv_data)
        # 执行json数据对应的操作
        serial.execute(serial.recv_data)
        