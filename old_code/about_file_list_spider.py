#爬取新视觉网站上的电影信息，以及存储对应URL

import requests
from bs4 import BeautifulSoup
import re
import pymssql
import os.path
import xlwt

url_base = r'https://www.yy6080.info'


# 根据类型和页数来获取URL的函数
# video_type参数：film-1 电视剧-2 动漫-3 综艺-4
def detail_url_get(url_base, video_type=1, page_start=1, page_sum=1):
    url_base2 = r'.html'
    for page_num in range(page_start,page_start+page_sum):
        source_url = url_base+'/list/?'+str(video_type)+'-'+str(page_num)+url_base2
        html = requests.get(source_url)
        html_body = html.text
        html_soup = BeautifulSoup(html_body, 'lxml')
        list_each_page = html_soup.select('li.col-md-5 div div h4 a')
        for i in list_each_page:
            #print(i['href'])
            yield "{0}".format(i['href'])


# 根据详情页的的url获取信息
def detail_info_get(url_suffix, url_before=url_base, output_control = False,dbs_control = False):
    ID = re.search('\?[0-9]+?\.',url_suffix).group()[1:-1]

    detail_url = url_before + url_suffix
    html = requests.get(detail_url)
    html_body = html.text
    html_soup = BeautifulSoup(html_body,'lxml')
    info_part = html_soup.find_all(name='p', attrs={'class': 'data'})

    #封面url
    try:
        img_url = html_soup.find_all(name='img',attrs={'class':'lazyload'})[0]['data-original']
    except:
        img_url = 'xxxxxxxxxxxxxxxxxxxxxxx'
    if img_url[:8] == '/tu.php?':
        img_url = url_before+img_url

    #电影标题
    title = html_soup.find_all(name='h1', attrs={'class': 'title'})[0].string

    #主演列表
    starring_info_list = BeautifulSoup(str(info_part[0]),'lxml').find_all('a')
    starring_list = ''
    for name in starring_info_list:
        tem = BeautifulSoup(str(name), 'lxml').text
        if tem != '':
            starring_list += '、' + tem
    starring_list = starring_list[1:]

    #导演
    director = BeautifulSoup(str(info_part[1]), 'lxml').find_all('a')
    directors = ''
    for name in director:
        tem = BeautifulSoup(str(name), 'lxml').text
        if tem != '':
            directors += '、' + tem
    if directors == '':
        directors = '未知'
    else:
        directors = directors[1:]

    #类型,地区，年份
    info_more = BeautifulSoup(str(info_part[2]), 'lxml').text
    try:
        film_type = re.search(r"类型：.+?地",info_more).group()[3:-1]
    except:
        film_type = '未知'
    try:
        film_local = re.search(r"地区：.+?年", info_more).group()[3:-1]
    except:
        film_local = '未知'
    try:
        film_year = re.search(r"年份：.+", info_more).group()[3:]
        if film_year == '0':
            film_year = '未知'
    except:
        film_year = '未知'

    #电影简介
    intro = html_soup.find(name='span', attrs={'class': 'detail-content'})
    info_intro = BeautifulSoup(str(intro), 'lxml').text

    #链接
    link_parts = html_soup.select('ul.stui-content__playlist li a')[0]
    link = url_before +str(link_parts['href'])

    if output_control:
        print(ID)   #编号
        print(img_url)  #封面地址
        print(title)    #标题
        print(starring_list)    #主演
        print(directors)    #导演
        print(film_type)    #类型
        print(film_local)   #地区
        print(film_year)    #年份
        print(info_intro)   #介绍
        print(link)     #视频链接
    elif dbs_control:
        # yield "'{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}'".format(ID,img_url,title,starring_list,directors
                                                                                   #,film_type,film_local,film_year,info_intro
                                                                                   #,link)
        yield [ID,img_url,title,starring_list,directors,film_type,film_local,film_year,info_intro,link]

'''
db_link = pymssql.connect('MYPC\SQLEXPRESS', 'sa', 'sa', 'BookShop')
print("连接成功！================")
cur = db_link.cursor()
for i in detail_url_get(url_base, page_start=118,page_sum=290):
    list_item = detail_info_get(i,dbs_control=True)
    for item in list_item:
        print(item)
        try:
            cur.execute("INSERT INTO Xinshijue_film(ID,cover_url,title,actors,director,type,region,year,introduce,link) VALUES({0})".format(str(item)))
            db_link.commit()
        except:
            continue;
db_link.close()
'''
path_my = os.getcwd()
book = xlwt.Workbook()
sheet = book.add_sheet('film')
row = 1
col = 0
while 1:
    try:
        user_num = input("输入获取数量：")
        break
    except:
        print('error')
sheet.write(0,0,'编号')
sheet.write(0,1,'封面链接')
sheet.write(0,2,'标题')
sheet.write(0,3,'主演')
sheet.write(0,4,'导演')
sheet.write(0,5,'类型')
sheet.write(0,6,'地区')
sheet.write(0,7,'时间')
sheet.write(0,8,'简介')
sheet.write(0,8,'视频链接')
for i in detail_url_get(url_base, page_start=118,page_sum=290):
    get_info_temp = detail_info_get(i,dbs_control=True)
    for item in get_info_temp:
        print(item)
        try:
            for each_info in get_info_temp:
                sheet.write(row,col,str(each_info))
            col = 0
        except:
            continue
book.save(path_my+'\\' + 'film_list')








