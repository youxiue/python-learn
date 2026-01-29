# youxiue
# createTime: 2026/1/19

'''
迭代器

特性:
    1. 只能向前,不能反复
    2. 特别节省内存
    3. 惰性机制

获取迭代器的方法有：
    1. iter()  内置函数可以直接拿到迭代器
    2. __iter__() 方法

从迭代器中获取数据的方法:
    1. next() 函数
    2. __next__() 方法

for 循环里面是一定要拿迭代器的, 不可迭代的东西不能用迭代器
    统一了不同数据类型的循环工作
    
迭代器本身也是可迭代的

'''
it = iter("hello python")
print(next(it)) # h
print(next(it)) # e


it = "konodioda".__iter__()
print(it.__next__()) # k
print(next(it)) # o

while True:
    try:
        print(next(it))
    except StopIteration:
        break

for i in "konodioda":
    print(i)
    
it = iter([1, 2, 3, 4, 5])

for i in it:
    print(i)