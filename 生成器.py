# youxiue
# createTime: 2026/1/19

'''
生成器 : 本质就是一个迭代器
生成器是一个返回迭代器的函数, 返回一个 yield 关键字定义的生成器对象 

创建生成器的方式
    1. 生成器函数
    2. 生成器表达式
    
生成器函数
    生成器函数执行的时候, 并不会执行函数, 而是返回一个迭代器对象
    
    yield: 只要函数中出现了yield，他就是一个生成器函数
        作用: 可以分段的执行函数中的内容, 通过 __next__() 可以执行到下一个yield的位置
        
生成器表达式 
    (表达式 for 变量 in 迭代对象)
    一次性的

'''

def func():
  print(123)
  yield 1 # yield 也有返回的意思, 会返回一个迭代器对象

ret = func()
print(ret.__next__()) # 1 yield只有执行next方法后才会返回结果

def func():
  print(123)
  yield 1
  print(456)
  yield 2
  print(789)
  
ret = func()
print(ret.__next__()) # 123 1
print(ret.__next__()) # 456 2


def order():
  lst = []
  for i in range(10000):
    lst.append(f"衣服{i}")
    if len(lst) == 50:
      yield lst
      # 下一次拿数据
      lst = []

gen = order()
print(gen.__next__())
print(next(gen))


# 生成器表达式
gen = (i for i in range(10))
print(gen.__next__())
for item in gen:
  print(item)

lst = list(gen)
print(lst) #  []  这里是空, 迭代器对象只能被使用一次