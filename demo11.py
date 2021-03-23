# youxiue
# createTime: 2021/1/23 21:02

# else
'''
 else 还可以与 while 和 for 循环搭配
 for 循环正常执行结束后, 即可执行else 里面的语句,
 如果for循环是 碰到break 跳出的循环 则不执行else方法体
'''

# for _ in range(3):
#     pwd = input('请输入密码')
#     if (pwd == '8888'):
#         print('密码正确')
#         break
#     else:
#         print('密码不正确')
# else:
#     print('对不起,三次密码均错误')

a = 0
while a < 3:
    len = input('你多大了?')
    if int(len) >= 18:
        print('符合标准')
        break
    else:
        print('不符合标准')
    a += 1
else:
    print('对不起, 你还小')
