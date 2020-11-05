url='https://yys.163.com'
import re
import urllib.request
req=urllib.request.Request(url)
req.add_header('Referer','https://yys.163.com')
req.add_header('User-Agent','ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400')
response=urllib.request.urlopen(req)
html=response.read()
