import urllib.request

from bs4 import BeautifulSoup

a = input('输入搜索内容：')
a = a.encode('utf-8')
a = str(a)
a = a[2:-1]
a = a.split('\\x')
a = '%'.join(a)
for i in a:
    a = a.upper()
web = {}
url = 'https://baike.baidu.com/item/' + a
req = urllib.request.Request(url)
req.add_header('Referer', 'http://fanyi.youdao.com')
req.add_header('User-Agent',
               'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400')
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "html.parser")
if '您所访问的页面不存在' in str(soup):
    print('搜索的关键词未收录')
import re

for i in soup.find_all(href=re.compile('item')):
    web[i.text] = 'https://baike.baidu.com' + i['href']
# print(i.text,'->',''.join(['https://baike.baidu.com',i['href']]))
for j in web.keys():
    print(j, '->', web[j])
