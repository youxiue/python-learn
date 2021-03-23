# youxiue
# createTime: 2021/1/23 20:30

# 循环
'''
4步循环法
1. 初始化变量
2. 条件判断
3. 条件执行体
4. 改变变量
'''

# ------------------------------------------while 循环--------------------------------------
a = 1
while a < 10:
    print(a)
    a += 1

'''
计算0 到100 之间的偶数和
'''
a = 0
sum = 0
while a <= 100:
    # if a%2 == 0:
    # if not bool(a%2):
    if not a % 2:
        sum += a
    a += 1
print(sum)

# ------------------------------------------for-in 循环--------------------------------------
'''
in 表达从 (字符串,序列等) 中依次取值, 又称为遍历
for-in遍历的对象必须是可迭代对象

for 自定义的变量 in 可迭代的对象: 
    循环体
    
ps: 如果循环体内不需要访问自定义变量, 可以将自定义变量 替代为 下划线.
'''
for s in 'python':
    print(s)

for i in range(10):
    print(i)

for _ in range(3):
    print('人生苦短,我用python')

'''
计算0 到100 之间的偶数和
'''
sum = 0
for i in range(101):
    if not i % 2:
        sum += i
print(sum)

'''
输出 100到 999 之间的水仙花数
例: 153 = 1*1*1 + 5*5*5 + 3*3*3
'''
for i in range(100, 1000):
    ge = i%10
    shi = i%100//10
    bai = i//100
    # print(bai, shi ,ge)
    # if i == ge*ge*ge + shi*shi*shi + bai*bai*bai:
    if i == ge**3 + shi**3 + bai**3:
        print(i)


'''
break 跳出循环
'''
for _ in range(3):
    pwd = input('请输入密码')
    if(pwd == '8888'):
        print('密码正确')
        break
    else:
        print('密码不正确')
'''
continue 跳出本次循环
'''
for i in range(100):
    if i%3:
        continue
    print(i)




