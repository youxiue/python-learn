# youxiue
# createTime : 2026/1/20

'''
匿名函数

lambda表达式
语法: 变量 = lambda 参数1,参数2....: 表达式




'''

def func( a, b):
  return a + b

print(func(1, 2))

# 改成lambda表达式
fn = lambda a, b: a + b
print(fn(1, 2))
