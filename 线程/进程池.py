# youxiue
# createTime: 2026/1/26

'''
线程池

Pool.apply_async(函数, args=(参数,))  # 非阻塞方式执行任务
Pool.apply(函数, args=(参数,))        # 阻塞方式执行任务
Pool.close() # 关闭线程池， 关闭后不能再添加任务
Pool.join() # 等待所有子线程结束


非阻塞模式： 全部添加到线程池中， 线程池会自动分配任务给子线程执行， 主进程不会等待子线程执行完成， 会继续往下执行代码 （多个任务同时执行）
阻塞模式： 每添加一个任务， 主进程就会等待子线程执行完成后， 才添加下一个任务  （任务一个一个的执行）
'''
from multiprocessing import Pool, Process
from random import random
import time

def task(name):
  print('%s is working...' % name)
  start = time.time()
  time.sleep(random() * 2)
  end = time.time()
  print('%s is done, cost %.2f' % (name, end - start))
  return (name, end - start)

container = []
def callback(res):
  # 这里会拿到子进程返回的结果
  # print('callback:', res)
  container.append(res)
  

if __name__ == '__main__':
  # 创建线程池
  pool = Pool(5)
  
  for i in range(10):
    # 非阻塞方式执行任务
    # pool.apply_async(task, args=('task %s' % i,), callback=callback)
    # 阻塞方式执行任务， 没有回调函数
    pool.apply(task, args=('task %s' % i,))
    
  pool.close()
  pool.join()
  
  for c in container:
    print(c)
  
  print('over.....')
  