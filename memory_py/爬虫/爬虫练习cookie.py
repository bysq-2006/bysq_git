import requests
from lxml import etree

url:str = "http://spiderbuf.cn/playground/e01/login"
session = requests.session()
date = {"username":"admin",
        "password":123456}
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}
element:list = []

text = session.post(url=url,data=date,headers=headers).text
tree = etree.HTML(text)
for i in tree.xpath("/html/body/main/div[2]/table/tbody/tr"):
    top = i.xpath("./*[1]/text()")[0]
    rmb = i.xpath("./*[2]/text()")[0]
    xinxi = i.xpath("./*[3]/text()")[0]
    ceo = i.xpath("./*[4]/text()")[0]
    hangye = i.xpath("./*[5]/text()")[0]
    element.append({"排名":str(top),"企业估值(亿元)":str(rmb),"企业信息":str(xinxi),"CEO":str(ceo),"行业":str(hangye)})

print(element)