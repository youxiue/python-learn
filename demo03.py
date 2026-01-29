# auth: youxiue
# createTime: 2021/1/23 16:13

print(1 + 1)
print(2 - 1)
print(2 * 3)
print(1 / 2)  # 除法运算 0.5
print(11 // 2)  # 整除运算 5
print(11 % 2)  # 取余运算 1
print(2 ** 2)  # 表示的是2的2次方   4
print(2 ** 3)  # 表示的是2的3次方   8

print(9 // 4)  # 2
print(-9 // -4)  # 2
# 一正一负的整数公式, 向下取整
print(9 // -4)  # -3
print(-9 // 4)  # -3

# 公式,
# 余数 + 除数 * 商  = 被除数
# 余数 = 被除数- 除数 * 商
print(9 % -4)  # 9-(-4)*(-3) = 9-12 = -3
print(-9 % 4)  # -9-(4)*(-3) = -9+12 = 3

# -----------------------------赋值运算符--------------------------------------
# 赋值运算符 =
a = 3 + 4
print(a)
# 执行顺序 右 -> 左
# 支持链式赋值
a = b = c = 20
print(a, id(a), b, id(b), c, id(c)) # id相同
# 支持参数赋值
a += 30  # a = a + 30
print(a)
a -= 30  # a = a - 30
print(a)
a *= 2  # a = a * 2
print(a, type(a))  # 40 int
a /= 2  # a = a / 2
print(a, type(a))  # 20.0 float
a /= 3  # a = a / 3
print(a, type(a)) #  6.666666666666667 <class 'float'>
a //= 2  # a = a // 2
print(a) # 3.0

# 支持系列解包赋值, 要求左右个数相同.
a, b, c = 20, 30, 40
print(a, id(a), b, id(b), c, id(c))
# 应用场景, 交换两个变量的值
a, b = b, a
print(a, b)  # 30 20

# -----------------------------比较运算符--------------------------------------

a, b = 20, 30
print('a>b吗?', a > b)  # False
print('a>=b吗?', a >= b)  # False
print('a<b吗?', a < b)  # True
print('a<=b吗?', a <= b)  # True
print('a==b吗?', a == b)  # False
print('a!=b吗?', a != b)  # True

'''
    == 比较的是值, 
    比较对象的标识id 使用 is
    相等  is
    不相等  is not
'''
a, b, c = 10, 10, 20
print(a == b)  # True
print(a is b)  # True
print(a is c)  # False
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(list1 == list2)  # True
print(list1 is list2)  # False
print(list1 is not list2)  # True

# -----------------------------布尔运算符--------------------------------------
'''
    并且(&&) and
    或者(||) or
    取反(!)  not
'''
a, b = 1, 2
print(a == 1 and b == 2)  # True
print(a != 1 or b <= 2)  # True
print(not (a != 1 or b <= 2))  # False

s = 'hello world'
print('w' in s)  # True
print('a' in s)  # False
print('w' not in s)  # False
print('a' not in s)  # True

# -----------------------------位运算符--------------------------------------
'''
    按位与 &   对应数位都是1, 结果数位才是1, 否则为0 (全为1, 才是1)
    按位或 |   对应数位都是0, 结果数位才是0, 否则为1 (只要有一个为1, 即为1)
    右移位运算符 <<   高位溢出舍弃, 低位补0 (右移1位,相当于乘2)
    左移位运算符 >>   低位溢出舍弃, 高位补0 (左移1位,相当于除2)
'''
print(4 & 8)  # 0
print(4 | 8)  # 12
print(4<<1)  # 右移1位  8
print(4<<2)  # 右移2位 16
print(4>>1)  # 左移1位  2
print(4>>2)  # 左移2位  1


'''
    运算符优先级
    算术运算符 > 位运算符 > 比较运算符 > 布尔运算符 > 赋值运算符
'''
