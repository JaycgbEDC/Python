# 反反爬之防盗链（梨视频）
import requests


url = 'https://www.pearvideo.com/video_1689956'
contid = url.split('_')[-1]
req_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1689956&mrd=0.610084875526379'
headers = {
    'Referer': 'https://www.pearvideo.com/video_1689956'
}
response = requests.get(req_url, headers = headers)
systemTime = response.json()['systemTime']
get_src = response.json()['videoInfo']['videos']['srcUrl']
real_src = get_src.replace(systemTime, f'cont-{contid}')
with open(r'Study\crawler and data_visualization\learn\crawl\video.mp4', 'wb') as fp:
    fp.write(requests.get(real_src).content)
    print('done!')