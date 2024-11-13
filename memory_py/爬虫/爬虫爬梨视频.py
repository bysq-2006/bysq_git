import requests,re
from lxml import etree
#17.52
id:str = "1707010"
url:str = f"https://www.pearvideo.com/video_{id}"
video_url:str = f"https://www.pearvideo.com/videoStatus.jsp?contId={id}&mrd=0.997710812834139"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
           "referer":id
           }
element:list = []

req = requests.get(url=video_url,headers=headers)

s = req.json()["systemTime"]
end_url = req.json()["videoInfo"]["videos"]["srcUrl"]

end_url = end_url.replace(s,f"cont-{id}")
print(end_url)