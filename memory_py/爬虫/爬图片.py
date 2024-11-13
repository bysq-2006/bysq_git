import requests,re,os
from bs4 import BeautifulSoup

url:str = "https://pic.netbian.com/index.html"
# 伪装请求头
headers:str = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
u_list:list = []
png_list:list = []

def is_valid_html_filename(filename: str) -> bool:
    # 使用正则表达式检查是否符合 "数字.html" 的格式
    pattern = r'^\d+\.html$'
    return bool(re.match(pattern, filename))

#	https://pic.netbian.com/
j = 0
for z in range(1,10,1):
    if z == 1:
        request = requests.get(url="https://pic.netbian.com/index.html",headers=headers)
    else:
        request = requests.get(url=f"https://pic.netbian.com/index_{z}.html",headers=headers)
    request.encoding = request.apparent_encoding
    req_bs4:str = BeautifulSoup(request.text,"html.parser")
    for i in req_bs4.findAll("li"):
        if is_valid_html_filename(i.a.get("href")[8:]):
            u_list.append("https://pic.netbian.com/" + i.a.get("href"))
    for url in u_list:
        request = requests.get(url=url,headers=headers)
        request.encoding = request.apparent_encoding
        req_bs4:str = BeautifulSoup(request.text,"html.parser")
        for i in req_bs4.findAll("div",{"class": "photo-pic"}):
            request = requests.get(url=("https://pic.netbian.com/" + i.find('img')['src']),headers=headers)
            file_name = f"D:\\bysq\\tupian\\{str(i.find('img')['src'][-12:])}.jpg"
            with open(file_name, 'wb') as file:
                file.write(request.content)
            print(j)
            j = j + 1