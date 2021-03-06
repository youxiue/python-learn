# youxiue
# createTime: 2021/4/02 14:59

'''
元组
    python 的内置数据结构之一,  是不可变序列

可变序列与不可变序列
    不可变序列: 字符串, 元组
        没有增 删 改 的操作
    可变序列: 列表, 字典
        可以对序列 增 删 改, 对象地址不发生改变


'''

''' 创建方式一, () '''
tup = ('hello', 'world')
print(tup)  # ('hello', 'world')
print(type(tup))  # <class 'tuple'>

# 省略小括号
t = 'wo' , 'ai', 'ni'
print(t)
print(type(t))

# 只有一个元素的时候 必须要加上逗号 , 
t = ('wo')
print(t) # wo 
print(type(t)) # <class 'str'>
t = ('wo',)
print(t) # ('wo',)
print(type(t)) # <class 'tuple'>



''' 创建方式二, 使用内置函数 tuple() '''
tup1 = tuple(('oh', 'my', 'god'))
print(tup1)
print(type(tup1))

''' 空元组的创建方式 '''
t1 = ()
t2 = tuple()
print('空元组', t1, t2) # 空元组 () ()



'''
为什么要将元组设计成 不可变序列
    因为在多任务环境下, 同时操作不可变序列对象 不需要加锁

注意事项: 元组中存储的是对象的引用
    a. 如果元组中对象本身是不可变对象, 则不能再引用其他对象
    b. 如果元组中的对象是可变对象, 则可变对象的引用不允许改变, 但被引用对象的数据可以改变
'''
t = (4 , ['jojo', 'dio'] , 'hello')
print(t, type(t), id(t) )
print(t[0], type(t[0]), id(t[0])) # 4 <class 'int'> 2510813227408
print(t[1], type(t[1]), id(t[1])) # ['jojo', 'dio'] <class 'list'> 2510819974528
print(t[2], type(t[2]), id(t[2])) # hello <class 'str'> 2510819956912

# t[0] = 3 # TypeError: 'tuple' object does not support item assignment
# t[1] = 100 # TypeError: 'tuple' object does not support item assignment 'tuple'对象不支持项赋值
t[1].append(100) # 向列表中添加元素
print(t, id(t)) # id 未发生变化
print(t[1], id(t[1])) # id 未发生变化
