
from machine import Pin, I2C
import time,utime

#AD0=0 -> addr=0x68
#AD0=1 -> addr=0x69
MPU6050_I2C_ADDR = 0x69
GYRO_RANGE = 250  # 陀螺仪量程设置为±250度/s
ACCEL_RANGE = 2   # 加速度计量程设置为±2g
GRAVITY = 9.81    # 重力加速度，单位 m/s²

'''
陀螺仪（Gyroscope）：          加速度计（Accelerometer）：

量程设置寄存器地址：0x1B        量程设置寄存器地址：0x1C
00: ±250 度/秒                 00: ±2g
01: ±500 度/秒                 01: ±4g
10: ±1000 度/秒                10: ±8g
11: ±2000 度/秒                11: ±16g
'''


def init_mpu6050():
    i2c.writeto_mem(MPU6050_I2C_ADDR, 0x6B, b'\x00')  # 将电源管理寄存器设置为0，唤醒MPU6050
    i2c.writeto_mem(MPU6050_I2C_ADDR, 0x1B, bytes([GYRO_RANGE // 500]))  # 设置陀螺仪量程
    i2c.writeto_mem(MPU6050_I2C_ADDR, 0x1C, bytes([ACCEL_RANGE // 4]))  # 设置加速度计量程，修正此处

def read_sensor_data(reg_addr):
    data = i2c.readfrom_mem(MPU6050_I2C_ADDR, reg_addr, 2)
    value = (data[0] << 8) | data[1]
    
    # 将数据转换为有符号整数
    value = value if value < 32768 else value - 65536
    return value

def convert_gyro_data(raw_data):
    return raw_data * (GYRO_RANGE / 32767)

def convert_accel_data(raw_data):
    return raw_data * (ACCEL_RANGE / 32767) * GRAVITY

def read_gyro_data():
    gyro_x = convert_gyro_data(read_sensor_data(0x43))
    gyro_y = convert_gyro_data(read_sensor_data(0x45))
    gyro_z = convert_gyro_data(read_sensor_data(0x47))
    return gyro_x, gyro_y, gyro_z

def read_accel_data():
    accel_x = convert_accel_data(read_sensor_data(0x3B))
    accel_y = convert_accel_data(read_sensor_data(0x3D))
    accel_z = convert_accel_data(read_sensor_data(0x3F))
    return accel_x, accel_y, accel_z

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=1000000)

init_mpu6050()

# 存储系统误差
gyro_error  = [0,0,0]
accel_error = [0,0,0]

print("IMU开始校准...")

#取前100次的结果计算累计误差
for i in range(100):
    for j in range(3):
        
        #读取imu数据
        gyro_data = read_gyro_data()
        accel_data = read_accel_data()
        #读数积累起来
        gyro_error[j]  += gyro_data[j]
        accel_error[j] += accel_data[j]
        
#计算平均误差
for j in range(3):
    
    gyro_error[j]  = gyro_error[j]/100
    accel_error[j] = accel_error[j]/100

#设置默认z轴加速度为g，其余量均为0
accel_error[2] -= GRAVITY

print("IMU校准完成...")

#航向角存储变量（单位：度）
yaw = 0.0

while True:
    
    #记录每次循环开始时的系统时间
    t0 = utime.ticks_ms()
    
    #更新数据
    gyro_data = read_gyro_data()
    accel_data = read_accel_data()

    #减去误差，计算z轴角速度(°/s)和加速度(m/s^2)
    data_gyro = gyro_data[2] - gyro_error[2]
    data_accel = accel_data[2] - accel_error[2]
    
    #略微延迟，防止计算量过大
    time.sleep(0.1)
    
    #计算dt,用于积分
    delta_t = utime.ticks_ms()-t0
    #对角速度近似积分获得航向角
    yaw += data_gyro*delta_t/1000
    print(yaw)

