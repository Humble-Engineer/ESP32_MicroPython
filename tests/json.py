import ujson

# Python对象转换为JSON格式的字符串
data = {'name':'John',
        'age':30,
        'city':'New York',
        'hubby':'football'}

# 将键值对转换为JSON格式的字符串
json_string = ujson.dumps(data)
print(json_string)

# JSON格式的字符串转换为Python对象
loaded_data = ujson.loads(json_string)
print(loaded_data)




# 通过键获取值
name_value = data['name']
age_value = data['age']
city_value = data['city']
hubby_value = data['hubby']

print("Name:", name_value)
print("Age:", age_value)
print("City:", city_value)
print("Hubby:", hubby_value)




# 修改特定键对应的值
data['age'] = 31
data['city'] = 'San Francisco'
# 也可以添加新的键值对
data['gender'] = 'Man'

print("modified:",data)
