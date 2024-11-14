import requests,re
from lxml import etree

def extract_numbers(s):
    # 使用正则表达式提取所有数字
    pattern = r'\d+'  # 匹配一个或多个数字
    numbers = re.findall(pattern, s)
    return numbers

url:str = "http://spiderbuf.cn/playground/n01"
header:dict = {"referer": "http://spiderbuf.cn/list/2",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}
element:dict = {}


req = requests.get(url=url,headers=header)
text = etree.HTML(req.text)
for i in text.xpath("/html/body/main/div[2]/div[2]/div/div"):
    li = i.xpath("./*/text()")
    element[f"{li[0]}"] = {"排名": extract_numbers(li[1])[0],"企业估值(亿元)": extract_numbers(li[2])[0],"CEO": li[3],"行业": li[4]}

print(element)