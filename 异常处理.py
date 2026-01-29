# youxiue
# createTime: 2026/1/21

'''
异常处理

try:
    可能会出错的代码
except Exception as e:
    出错后的处理代码
finally:
    无论是否出错, 都会执行的代码

'''

try: 
  print(my_name)
except NameError as e:
  print(e)
finally:
  pass
  


try:
    a = int(input("请输入数字:"))
    b = int(input("请输入数字:"))
    print(a/b)
except NameError as e:
    print("未命名异常：" , e)
except ZeroDivisionError as e:
    print("被除数为0异常：" , e)
except Exception as e:
    print("其他异常：" , e)
finally:
    print("程序结束")