import machine,esp32, time
from machine import Pin


pin_13 = Pin(13, mode = Pin.IN)
#level 参数可以是: WAKEUP_ANY_HIGH 或 WAKEUP_ALL_LOW
esp32.wake_on_ext0(pin=pin_13, level=esp32.WAKEUP_ALL_LOW)


print('两秒钟后进入睡眠模式')
time.sleep(2)
print('Sleep Mode On')
# 这里不加延迟的话打印到一半就进入睡眠模式了
time.sleep_ms(100)

# Light Sleep 模式
# machine.lightsleep()        
# print('解除 Light Sleep 模式')

# Deep Sleep 模式
machine.deepsleep()
print('解除 Deep Sleep 模式')




