import urllib.request
import urllib.parse
import json
#url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

#第一种加head的方法
'''
head={}
head['Referer']='http://fanyi.youdao.com'
head['User-Agent']='ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400'
'''
data={}
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['cilent']='fanyideskweb'
data['salt']= '15643960069128'
data['sign']='9772be250c8cef926726b4e304fc3d6a'
data['i']=input('输入翻译内容:')
data['doctype']='json'
data['version']='2.1'
data['action']= 'FY_BY_CLICKBUTTION'
data['typoResult']='false'
data['keyfrom']='fanyi.web'
data=urllib.parse.urlencode(data).encode('utf-8')

#第二种加head的方法
req=urllib.request.Request(url,data)
req.add_header('Referer','http://fanyi.youdao.com')
req.add_header('User-Agent','ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400')

#第一种方法加head加下方语句
#req=urllib.request.Request(url,data,head)
response=urllib.request.urlopen(req)
html=response.read().decode('utf-8')
t=json.loads(html)
print(t['translateResult'][0][0]['tgt'])
input()
