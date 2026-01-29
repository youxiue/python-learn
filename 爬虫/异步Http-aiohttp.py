'''
爬虫.异步Http-aiohttp 的 Docstring
pip install aiohttp
'''

import asyncio
import aiohttp

urls = [
  'http://img.netbian.com/file/2026/0121/1907095mxNK.jpg',
  'http://img.netbian.com/file/2026/0120/190112vTfM9.jpg',
  'http://img.netbian.com/file/2026/0120/231154wfLGc.jpg',
  'http://img.netbian.com/file/2026/0120/211011mmz6K.jpg',
]


async def download(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      content = await resp.read()
      filename = url.split('/')[-1]
      filename = 'file/' + filename
      with open(filename, 'wb') as f:
        # f.write(await resp.read())
        f.write(content)


async def main():
  tasks = []
  for url in urls:
    task = asyncio.create_task(download(url))
    tasks.append(task)
  await asyncio.wait(tasks)
  
if __name__ == "__main__":
  asyncio.run(main())