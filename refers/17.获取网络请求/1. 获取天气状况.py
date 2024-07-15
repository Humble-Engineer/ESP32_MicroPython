'''
该程序作用是使用外部中断控制按键输入
在线文档：https://docs.geeksman.com/esp32/MicroPython/20.esp32-micropython-request.html
'''
import urequests


# 定义请求参数字典
request_params = {'city': '上海', 'key': 'a702b975fa48a063b1a57c938bafb47a'}
# 定义访问地址
url = f'http://apis.juhe.cn/simpleWeather/query?city={request_params["city"]}&key={request_params["key"]}'

# 发送请求,接收响应
response = urequests.get(url)

# print(response.text)
# print(response.json())
# print(type(response.json()))

# 获取数据
realtime = response.json()['result']['realtime']
temp = realtime['temperature']
info = realtime['info']
aqi = realtime['aqi']

print(f'温度：{temp}\n天气：{info}\n空气指数：{aqi}')

