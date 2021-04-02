# youxiue
# createTime: 2021/1/24 14:59

# 字典
'''
字典
    python内置的数据结构之一, 以键值对的方式存储数据, 字典是一个无序的可变序列
'''

'''
使用{}创建
'''
scores = {'张三': 100, '李四': 98, '王五':23}
print(scores)
print(type(scores))

'''
使用 dict()创建
'''
student = dict(name='jojo', age=20)
print(student)

'''
空字典
'''
d = {}
print(d)


'''
取值 ['key']
'''
print(scores['张三'])
# print(scores['子路']) # KeyError: '子路'

'''
取值 get('key')
'''
print(scores.get('张三'))
print(scores.get('子路')) # None 不会报错
print(scores.get('宁秋', 99)) # 99   第二个参数是在查找key对应的值不存在时, 返回的默认值

'''
键的判断 
'''
print('张三' in scores) # True
print('张三' not in scores) # False
print('宁毅' in scores) # False

'''
删除键值对
'''
del scores['张三']
print('张三' in scores) # False


'''
添加键值对
'''
scores['陈留'] = 35
print(scores)

'''
修改键值对
'''
scores['陈留'] = 21
print(scores)

'''
获取所有的 key
'''
keys = scores.keys()
print(keys) # dict_keys(['李四', '王五', '陈留'])
print(type(keys)) # <class 'dict_keys'>
print(list(keys)) # ['李四', '王五', '陈留']

''' 
获取所有的 value
'''
values = scores.values() 
print(values) # dict_values([98, 23, 21]) 
print(type(values)) # <class 'dict_values'> 
print(list(values)) # [98, 23, 21]

'''
获取所有的键值对
'''
items = scores.items()
print(items) # dict_items([('李四', 98), ('王五', 23), ('陈留', 21)])
print(type(items)) # <class 'dict_items'>
print(list(items)) # [('李四', 98), ('王五', 23), ('陈留', 21)]  # 转换之后的元素是由元组组成的





# 清空字典
scores.clear()
print(scores) # {}