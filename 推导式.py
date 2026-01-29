# youxiue
# createTime: 2026/1/19

'''
推导式

列表推导式: [表达式 for 变量 in 迭代对象 if 条件]
集合推导式: {表达式 for 变量 in 迭代对象 if 条件}
字典推导式: {key:value for key,value in 迭代对象 if 条件}

没有元组推导式!!!
(表达式 for 变量 in 迭代对象) 是生成器表达式, 不是元组推导式
'''


lst = [i * 10 for i in range(1, 10) if i % 2 == 0]
print(lst) # [20, 40, 60, 80]

s = {i * 10 for i in range(1, 10) if i % 2 == 0}
print(s) # {40, 80, 20, 60}

lst = ['张三', '李四', '王五']
dic = {i:lst[i] for i in range(len(lst))}
print(dic)  # {0: '张三', 1: '李四', 2: '王五'}
