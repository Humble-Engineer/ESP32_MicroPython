from machine import Pin, PWM
import time
import math

class Servo:
    def __init__(self, pin, min_pulse=500, max_pulse=2500, freq=50):
        self.pin = pin
        self.min_pulse = min_pulse  # 最小脉冲宽度，单位为微秒
        self.max_pulse = max_pulse  # 最大脉冲宽度，单位为微秒
        self.freq = freq            # PWM频率，单位为Hz
        self.pwm = PWM(Pin(pin), freq=self.freq)  # 初始化PWM
        self.angle = 0

    def set_angle(self, angle):
        if not 0 <= angle <= 180:
            raise ValueError("Angle must be between 0 and 180 degrees")

        # 计算脉冲宽度
        pulse = self.min_pulse + (angle / 180) * (self.max_pulse - self.min_pulse)
        # 计算占空比
        duty_cycle = (pulse / 1000000) * self.freq  # 微秒转换为秒，然后乘以频率得到占空比

        # 设置PWM占空比
        self.pwm.duty_u16(int(duty_cycle * 65535))
        self.angle = angle

    def release(self):
        # 释放PWM资源
        self.pwm.deinit()

# 使用示例
if __name__ == "__main__":
    # 假设舵机连接到GPIO 2
    servo = Servo(pin=32)

    try:
        # 将舵机设置到90度
        servo.set_angle(90)
        time.sleep(2)  # 保持2秒

        # 将舵机设置到0度
        servo.set_angle(0)
        time.sleep(2)  # 保持2秒

        # 将舵机设置到180度
        servo.set_angle(180)
        time.sleep(2)  # 保持2秒
    finally:
        # 释放资源
        servo.release()