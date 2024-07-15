import machine
import time

# 定义ADC引脚
adc = machine.ADC(machine.Pin(34))

# 电池额定电压
rated_voltage = 5

# 电阻值
resistance = 1000

# 读取电压值并转换为电池电压
def read_voltage():
    adc_value = adc.read()
    voltage = adc_value / 4095 * 3.3
    battery_voltage = voltage / (resistance / (1000 * rated_voltage))
    return battery_voltage

# 计算电池剩余电量
def calc_battery_level(battery_voltage):
    max_voltage = 1.6 * rated_voltage
    min_voltage = 1.0 * rated_voltage
    battery_level = (battery_voltage - min_voltage) / (max_voltage - min_voltage) * 100
    return battery_level

# 循环读取电池电压并计算电池剩余电量
while True:
    battery_voltage = read_voltage()
    battery_level = calc_battery_level(battery_voltage)
    print("Battery voltage: {:.2f}V, battery level: {:.0f}%".format(battery_voltage, battery_level))
    time.sleep(1)
