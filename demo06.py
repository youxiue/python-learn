# auth: youxiue
# createTime: 2021/1/23 16:13

answer = input('您是会员吗?y/n')
money = int(input('购物金额: '))

if answer == 'y':
    if money > 10000:
        print('打8折, 付款金额: ', money * 0.8)
    elif money > 5000:
        print('打9折, 付款金额为: ', money * 0.9)
    else:
        print('打9.5折, 付款金额为: ', money * 0.95)
else:
    print('不是会员, 付款金额: ', money)