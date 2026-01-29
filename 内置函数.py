# youxiue
# createTime: 2026/1/19

# 内置函数

# 进制函数
a = 12
print(bin(a)) # 0b1100 二进制
print(oct(a)) # 0o14 八进制
print(hex(a)) # 0xc 十六进制

# 计算函数 sum, min ,max, pow
a = 10
b = 3
print(pow(a, b)) # 1000 , a的b次方
print(a ** b) # 1000， 这种写法也是 a的b次方

lst = [232,52, 1234, 98, 10, 943]
print(sum(lst)) # 2569
print(min(lst)) # 10
print(max(lst)) # 1234


# format  b: 二进制, o: 八进制, x: 十六进制, d: 十进制
a = 16
print(format(a, 'b')) # 10000
print(format(a, '08b')) # 00010000  08b表示由0填充，长度为8
print(format(a, 'o')) # 20
print(format(a, 'x')) # 10



 # ord  获取字符的ASCII码, python的内存中使用的事unicode编码
print(ord("中")) # 20013
 # chr 把某一个ASCII码转换成字符
print(chr(20013)) # 中


# all  判断所有元素是否都为真
print(all([1, "123", "肯德基"])) # True
# any 判断是否有元素为真
print(any([1, "123", "肯德基"])) # True
print(any([0, "", False])) # False

# enumerate 枚举
for index, item in enumerate(["张三", "王五", "赵六"]): 
  print(index, item)


# hash 计算hash值
print(hash("hello"))
# dir 查看对象, 获取对象属性和方法
print(dir("hello"))


# zip 可以把多个可迭代内容进行合并形成元组
nameLst = ["张三", "王五", "赵六"]
ageLst = [18, 19, 20]
jobLst = ["程序员", "老师", "学生"]

for people in zip(nameLst, ageLst, jobLst): # 迭代多个列表
  print(people)
  
  
# locals() 获取当前作用域的变量
a = 10
print(locals()) # 此时locals被写在了全局作用域范围内,此时看到的就是全局作用域中的内容, 会有a: 20 已经前面的people等定义的变量信息

def func():
  a = 20
  print(locals()) # 此时locals被写在了局部作用域范围内,此时看到的就是局部作用域中的内容,  只有{'a': 20}

func()

# globals() 获取全局作用域的变量
def func():
  a = 30
  print(globals()) # globals看到的是全局作用域中的内容

func()

# sort  排序
lst = [182, 932, 12, 0, 8232, 95, 23, 1, 203]

print(sorted(lst)) # [0, 1, 12, 23, 95, 182, 203, 932, 8232] 从小到大
print(sorted(lst, reverse=True)) # [8232, 932, 203, 182, 95, 23, 12, 1, 0] 从大到小

# sorted() 自定义排序规则
lst = ['孙悟空', '大光头', '老A', '蒙奇*D*路飞','一叽咕','纳鲁多']
# 自定义排序规则函数: 根据长度排序
def func(name):
  return len(name)

print(sorted(lst, key=func))

# 简化
print(sorted(lst, key= lambda x: len(x)))

lst = [
  {'name': '张三','age': 56, 'salary': 8000},
  {'name': '王五','age': 19, 'salary': 5000},
  {'name': '赵六','age': 35, 'salary': 10000 },
  {'name': '李七','age': 25, 'salary': 7000}
]

# 根据年龄排序
print(sorted(lst, key= lambda x: x['age']))
# 根据工资降序
print(sorted(lst, key= lambda x: x['salary'], reverse=True))


# filter 筛选过滤
lst = ["张三丰", '灭绝师太', '金轮法王',  '张无忌', '神雕大侠']
f = filter(lambda x: x.startswith('张'), lst)
print(list(f)) # ['张三丰', '张无忌']
f = filter(lambda x: not x.startswith('张'), lst)
print(list(f))


# map 映射
lst = [1, 2, 3, 4, 5]

r = map(lambda x: x * 2, lst)
print(list(r)) # [2, 4, 6, 8, 10]