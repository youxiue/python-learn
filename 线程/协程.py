# youxiue
# createTime: 2026/1/26

'''
协程： 微线程， 协程是线程的升级版，目的是为了更高效的利用CPU资源
协程

进程 > 线程 > 协程

可以使用第三方包 greenlet 已经封装了协程
'''

def task1():
    print('task1')
    yield
    print('task1 again')
    yield
    print('task1 end')

def task2():
    print('task2')
    yield
    print('task2 again')
    yield
    print('task2 end')
  
if __name__ == '__main__':
  t1 = task1()
  t2 = task2()
  
  while True:
      try:
          next(t1)
          next(t2)
      except:
          break


import time
from greenlet import greenlet

def f1():
    for i in range(5):
        print('f1:', i)
        gr2.switch()
        time.sleep(0.5)
    
def f2():
    for i in range(5):
        print('f2:', i)
        gr3.switch()
        time.sleep(0.5)
    
def f3():
    for i in range(5):
        print('f3:', i)
        gr1.switch()
        time.sleep(0.5)
    

if __name__ == '__main__':
    gr1 = greenlet(f1)
    gr2 = greenlet(f2)
    gr3 = greenlet(f3)
    gr1.switch()
    


    
    
    
