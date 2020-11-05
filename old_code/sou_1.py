import urllib.request
from bs4 import BeautifulSoup
import tkinter as tk
import re


root=tk.Tk()
root.title('检索')
frame0 = tk.Frame(root)
frame1 = tk.Frame(root)


def sou(key):
	a=key
	a=a.encode('utf-8')
	a=str(a)
	a=a[2:-1]
	a=a.split('\\x')
	a='%'.join(a)
	for i in a:
		a=a.upper()
	web={}
	url='https://baike.baidu.com/item/'+a
	req=urllib.request.Request(url)
	req.add_header('Referer','http://fanyi.youdao.com')
	req.add_header('User-Agent','ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400')
	response=urllib.request.urlopen(req)
	html=response.read()
	soup=BeautifulSoup(html,"html.parser")
	if '您所访问的页面不存在' in str(soup):
		print('搜索的关键词未收录')

	for i in soup.find_all(href=re.compile('item')):
		web[i.text]='https://baike.baidu.com'+i['href']
	dz='.\\'+key+r'.txt'
	#print(i.text,'->',''.join(['https://baike.baidu.com',i['href']]))
	with open(dz,'w+',encoding='utf-8') as f:
		for j in web.keys() :
				con=j+'->'+web[j]+'\n'
				f.write(con)
	

def get():
	var.set(e1.get())
	print(sou(var.get()))


var = tk.StringVar()
var.set('')
e1=tk.Entry(frame0)
e1.grid(padx=10,pady=5)
e1.delete (0,tk.END)
e1.insert (0,'在此输入进行搜索……')
tb=tk.Button(frame0,text='检索',command=get)
tb.grid(padx=10,pady=5)


frame0.grid(row=0,column=0,padx=5,pady=6)
frame1.grid(row=1,column=0,padx=5,pady=6)
root.mainloop()
