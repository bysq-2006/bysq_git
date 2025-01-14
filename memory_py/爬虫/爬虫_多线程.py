import requests,re,json
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
 
url:str = "http://www.xinfadi.com.cn/getPriceData.html"
header:dict = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
                ,"referer": "http://www.xinfadi.com.cn/priceDetail.html"}
all_element:list = []
 
# 发送POST请求并处理返回的价格数据
def req_post(page:int = 1):
    global all_element
    data:dict = {"limit": 20,"current": page}
 
    req = requests.post(url=url, headers=header, data=data)
    element = req.json()["list"]
    for i in element:
        all_element.append(i)
 
 
if __name__ == "__main__":
    # 创建线程池并提交多个请求以爬取数据
    with ThreadPoolExecutor(10) as t:
        for page in range(1,99,1):
            t.submit(req_post,page)
 
 
    # 将爬取的所有数据写入JSON文件
    with open('list.json', 'w') as f:
        json.dump(all_element, f)
