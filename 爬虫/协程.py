import asyncio
async def task1():
    print("task1 start")
    await asyncio.sleep(2)
    print("task1 end")
    
async def task2():
    print("task2 start")
    await asyncio.sleep(4)
    print("task2 end")
    
async def task3():
    print("task3 start")
    await asyncio.sleep(3)
    print("task3 end")
    
    
async def main():
    # 创建任务对象
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    t3 = asyncio.create_task(task3())
    
    tasks = [t1, t2, t3]
    await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    
# if __name__ == "__main__":
#     asyncio.run(main())

# 应用

async def download(url):
  print("开始下载：", url)
  await asyncio.sleep(2)
  print("下载完成：", url)
  
async def main():
  urls = [
    "www.baidu.com",
    "www.taobao.com",
    "www.jd.com",
    "www.suning.com",
    "www.tmall.com"
  ]
  
  tasks = []
  
  for url in urls:
    task = asyncio.create_task(download(url))
    tasks.append(task)
    
  await asyncio.wait(tasks)
  
if __name__ == "__main__":
  asyncio.run(main())