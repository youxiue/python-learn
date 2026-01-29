# -*- coding: utf-8 -*-
# youxiue
# createTime: 2021/1/17 22:13

# 输入函数 input()
present = input('你喜欢谁?')
print(present, type(present))

# 从键盘区录入两个整数, 并计算和
a = input('请输入第一个数：') # 2
b = input('请输入第二个数：') # 3
print(type(a), type(b))
print(a + b) # 23 # 不能直接相加, 需要进行类型转换
print(int(a) + int(b)) # 5

c = int(input('请输入第一个数：')) # 2
d = int(input('请输入第二个数：')) # 3
print(c + d) # 5 