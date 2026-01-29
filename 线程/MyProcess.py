# youxiue
# createTime: 2026/1/26

'''
自定义进程
'''
from multiprocessing import Process
from time import sleep

class MyProcess(Process):
    def __init__(self, name):
        super().__init__(name=name)

    # 重写run方法
    def run(self):
      n = 1
      while True:
        sleep(1)
        print('%s is running: %d' % (self.name, n))
        n += 1
        
if __name__ == '__main__':
    p1 = MyProcess('p1')
    p1.start()
    p2 = MyProcess('p2')
    p2.start()
    


