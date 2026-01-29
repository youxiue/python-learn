# youxiue
# createTime: 2026/1/22

from time import sleep
from multiprocessing import Process
import os

'''
多进程对于全局变量的访问，在每一个全局变量里面都放一个m变量，保证每个进程访问变量互不干扰
'''


m = 1 # 不可变类型
list = []


def task1(s, name):
  global m
  while True:
    sleep(s)
    m += 1
    list.append(str(m) + 'task1')
    # print('task 111111111111...', os.getpid(),  '-----', os.getppid(), name)
    print('task 1: ', m, list)
    
def task2(s,name):
  global m
  while True:
    sleep(s)
    m += 1
    list.append(str(m) + 'task2')
    # print('task 222222222222...', os.getpid(),  '-----', os.getppid(), name)
    print('task 2----------: ', m, list)
    

if __name__ == '__main__':
  print(os.getpid())
  p1 = Process(target=task1, name="任务1", args=(1, '任务1'))
  p1.start()
  print(p1.name)
  p2 = Process(target=task2, name="任务2", args=(2, '任务2'))
  p2.start()
  print(p2.name)
  
  while True:
    sleep(1)
    m += 1
    list.append(str(m) + 'main')
    print('main ---------------------: ', m, list)
  
  