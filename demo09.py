# youxiue
# createTime: 2021/1/23 20:13

'''
内置函数 range()
range() 用于生成一个整数序列, 返回值是一个迭代器对象
range函数的优点: 不管range对象表示的整数序列有多长, 所有range对象占用的内存空间都是相同的, 因为仅仅需要存储 start, stop, step
    只有当用到range 对象时, 才会去计算 序列中的相关元素.
'''



'''
range(stop),  默认从 0 开始, 步长为1, 到 stop(不包含) 结束
'''
r1 = range(10)
print(r1)
print(list(r1)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
range(start, stop) 从 start 开始, 步长为1 , 到stop(不包含) 结束
'''
r2 = range(5, 10)
print(r2)
print(list(r2)) # [5, 6, 7, 8, 9]

'''
range(start, stop, step) 从 start 开始, 步长为step , 到stop(不包含) 结束
'''
r3 = range(5, 10, 2)
print(r3)
print(list(r3)) # [5, 7, 9]

# in 与 not in 可以用来判断整数序列中 是否存在或不存在指定的整数.
print(10 in r3) # False
print(9 in r3) # True
print(8 not in r3) # True