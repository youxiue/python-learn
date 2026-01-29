# youxiue
# createTime: 2026/1/28

'''
处理防盗链

'''
import requests
domain = 'https://www.pearvideo.com/video_1804920'
contId = domain.split('_')[-1]

url = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.2977838150009563'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
    # 添加防盗链
    'Referer': domain
}
resp = requests.get(url, headers=headers)
data = resp.json()
print(data)
systemTime = data['systemTime']
video_url = data['videoInfo']['videos']['srcUrl']
print(video_url) # https://video.pearvideo.com/mp4/short/20260128/1769588958805-16071658-hd.mp4
# 实际播放链接： https://video.pearvideo.com/mp4/short/20260128/cont-1804920-16071658-hd.mp4
video_url = video_url.replace(systemTime, f'cont-{contId}')
print(video_url)

