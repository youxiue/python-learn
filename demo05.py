# auth: youxiue
# createTime: 2021/1/23 16:13

money = 10000  # 金额
s = int(input('请输入取款金额:'))  # 取款金额
# 判断金额是否充足
if money >= s:
    money -= s
    print('取款成功, 余额为: ', money)
else:
    print('取款失败')

scope = int(input('请输入分数:'))
if scope > 100:
    print('分数输入错误')
elif scope > 89:
    print('优秀')
elif scope > 79:
    print('良')
elif scope > 69:
    print('及格')
else:
    print('不及格')

