import urllib.request
from bs4 import BeautifulSoup
import re
url='https://www.ip.cn'  #加入url
req=urllib.request.Request(url) #添加头防止网页禁止访问
req.add_header('Referer','http://fanyi.youdao.com')
req.add_header('User-Agent','ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400')

response=urllib.request.urlopen(req)  #打开网页
html=response.read().decode('utf-8')#读取网页并将utf-8编码解码
soup=BeautifulSoup(html,"html.parser")#解析内容
need=re.search(r'\d+.\d+.\d+.\d+',str(soup))
print(need.group())


