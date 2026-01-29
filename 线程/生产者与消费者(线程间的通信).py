# youxiue
# createTime: 2026/1/26

'''
线程.生产者与消费者(线程间的通信)

Python中的线程间通信主要通过共享变量和队列来实现。生产者线程负责生成数据并将其放入共享变量或队列中，而消费者线程则从共享变量或队列中获取数据进行处理。

Queue模块提供了线程安全的队列实现，包括先入先出队列（FIFO）、后入先出队列（LIFO）和优先级队列。
这些队列都实现了锁原语（可以理解为原子操作，即要么不做，要么就做完）， 可以安全地在多个线程间共享数据。


put()方法将数据放入队列中
get()方法从队列中获取数据
'''
import threading
import queue
import time
import random

def producer(q):
  i = 0
  while i < 10:
    num = random.randint(1, 100)
    q.put(num)
    print('生产者生产数据------------:', num)
    time.sleep(1)
    i += 1
  q.put(None) # 生产者结束后放入None作为结束标志
  q.task_done() # 任务完成
  print('生产者结束') 
  
  
def consumer(q):
  while True:
    num = q.get()
    if num is None: # 遇到结束标志，退出循环
      break
    print('消费者消费数据:', num)
    time.sleep(2)
  print('消费者结束')
  q.task_done()
  
if __name__ == '__main__':
  q = queue.Queue(5) # 创建一个队列对象
  p = threading.Thread(target=producer, args=(q,)) # 创建生产者线程
  c = threading.Thread(target=consumer, args=(q,)) # 创建消费者线程
  p.start() # 启动生产者线程
  c.start() # 启动消费者
  

