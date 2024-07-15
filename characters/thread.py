import _thread
import machine
import time

# 全局退出标志
exit_flag = True

# 线程1: 控制LED闪烁
def blink_led(kwargs):
    pin = kwargs.get('pin', 2)  # 默认引脚号为2
    period = kwargs.get('period', 1)  # 默认周期为1秒

    # 设置LED引脚
    led = machine.Pin(pin, machine.Pin.OUT)
    while exit_flag:
        led.value(not led.value())  # 切换LED状态
        time.sleep(period)  # 等待一段时间

# 线程2: 在屏幕上打印信息
def print_info(kwargs):
    period = kwargs.get('period', 1)  # 默认周期为1秒

    while exit_flag:
        print("线程2正在运行...")
        time.sleep(period)  # 每指定秒数打印一次

# 使用kwargs启动线程的辅助函数
def start_thread(target, kwargs):
    _thread.start_new_thread(target, (kwargs,))


# 创建并启动LED闪烁线程，使用kwargs传递参数
start_thread(blink_led, {'pin': 25, 'period': 1})

# 创建并启动打印信息线程，使用kwargs传递参数
start_thread(print_info, {'period': 5})

# 主线程继续执行其他任务或进入无限循环
try:
    while True:
        time.sleep(10)
        
except KeyboardInterrupt:
    exit_flag = False
    print("程序被用户中断...")