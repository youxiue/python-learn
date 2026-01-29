# youxiue
# createTime: 2026/1/22

'''
线程

Process(target=函数, name=进程名, args=(参数))

start() 启动进程， 并执行任务
run()  只是执行任务， 不会启动进程
terminate() 杀死进程

'''

from time import sleep
from multiprocessing import Process
import os

def task1():
  while True:
    sleep(1)
    print('task 111111111111...', os.getpid(),  '-----', os.getppid())
    
def task2():
  while True:
    sleep(1)
    print('task 222222222222...', os.getpid(),  '-----', os.getppid())
    

if __name__ == '__main__':
  print(os.getpid())
  # 创建进程
  p1 = Process(target=task1, name="任务1")
  p1.start()
  print(p1.name)
  # 创建进程
  p2 = Process(target=task2, name="任务2")
  p2.start()
  print(p2.name)
  