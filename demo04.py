# auth: youxiue
# createTime: 2021/1/23 16:13

'''
 以下对象的布尔值为 False
 1. False
 2. 数值 0
 3. None
 4. 空字符串
 5. 空列表
 6. 空元组
 7. 空字典
 8. 空集合
'''
print(bool(False))

print(bool(0))
print(bool(0.0))

print(bool(None))

print(bool(''))
print(bool(""))

print(bool([]))
print(bool(list()))

print(bool(()))  # 空元组
print(bool(tuple()))  # 空元组

print(bool({}))  # 空字典
print(bool(dict()))  # 空字典

print(bool(set()))  # 空集合
'''
其他对象的布尔值均为True
'''