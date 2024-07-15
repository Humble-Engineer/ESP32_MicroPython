import machine
import time

class SR04:
    def __init__(self, trig_pin, echo_pin):
        self.trig_pin = machine.Pin(trig_pin, machine.Pin.OUT)
        self.echo_pin = machine.Pin(echo_pin, machine.Pin.IN)
        self.trig_pin.value(0)

    def distance(self):
        # 触发超声波发射
        self.trig_pin.value(1)
        time.sleep_us(10)  # 保持10微秒
        self.trig_pin.value(0)

        # 测量回声时间
        pulse_start = time.ticks_us()
        while self.echo_pin.value() == 0:
            pulse_start = time.ticks_us()
        pulse_end = time.ticks_us()
        while self.echo_pin.value() == 1:
            pulse_end = time.ticks_us()

        # 计算脉冲持续时间
        pulse_duration = pulse_end - pulse_start

        # 计算距离，声速在空气中约为343米/秒
        speed_of_sound = 343  # 米/秒
        distance = (pulse_duration * speed_of_sound) / 200000

        return distance

# 使用示例
if __name__ == "__main__":
    
    # 假设触发引脚连接到GPIO 12，回声引脚连接到GPIO 13
    ultrasonic = SR04(trig_pin=12, echo_pin=13)

    try:
        while True:
            dist = ultrasonic.distance()
            print("Distance: {:.2f} mm".format(dist * 100))  # 转换为毫米
            time.sleep(1)  # 每秒测量一次
    except KeyboardInterrupt:
        pass