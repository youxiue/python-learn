# youxiue
# createTime: 2021/4/02 14:59

# 字典

scores = {'张三': 100, '李四': 98, '王五': 23}

'''
遍历 输出  item 是 key值
'''
for item in scores:
    print(item, scores[item], scores.get(item))
'''
张三 100 100
李四 98 98
王五 23 23
'''


'''
key相同时  后面的会覆盖前面的
1. key 不会重复, value 可以重复
2. 字典中的元素是无序的
3. 字典中的key 必须是不可变对象
4. 字典也可以根据需要动态的伸缩
5. 字典会浪费比较大的内存, 是一种使用空间换时间的 数据结构
'''
d = {'name': 'jack', 'name': 'zhangsan'}
print(d)
key = 'age'
d[key] = 1000
print(d)
lst = [10, 20 , 30]
# d = {lst: 100} # TypeError: unhashable type: 'list'
# print(d)

'''
使用内置函数 zip() 创建
'''
items = ['fruits', 'books', 'others']
prices = [93, 91, 90.1]
shop = zip(items, prices)
print(shop) # <zip object at 0x000001AFC79CCB40>
print(list(shop)) # [('fruits', 93), ('books', 91), ('others', 90.1)]

shopDict = {item:price for item, price in zip(items, prices)}
print(shopDict) # {'fruits': 93, 'books': 91, 'others': 90.1} 

shopDict = {item.upper():price for item, price in zip(items, prices)} # upper() 变成大写
print(shopDict)  # {'FRUITS': 93, 'BOOKS': 91, 'OTHERS': 90.1} 

'''
当 两个列表 数量不一致的时候,  以 数量少的为准
'''
keys = ['a', 'b', 'c']
values = [1,2,3,4]
dicts = {key:value for key, value in zip(keys, values)} # upper() 变成大写
print(dicts) # {'a': 1, 'b': 2, 'c': 3} 

keys = ['a', 'b', 'c', 'd']
values = [1,2,3]
dicts = {key:value for key, value in zip(keys, values)}
print(dicts) # {'a': 1, 'b': 2, 'c': 3}