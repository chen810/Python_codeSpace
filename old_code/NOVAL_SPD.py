import requests
from bs4 import BeautifulSoup
import re
import pymssql


def get_page_info(page_num, lock=True, out_control=False):
    URL_l = 'http://book.zongheng.com/store/c0/c0/b0/u0/p'
    URL_r = '/v9/s9/t0/u0/i0/ALL.html'
    html = requests.get(URL_l + str(page_num) + URL_r)
    html_body = html.text
    html_soup = BeautifulSoup(html_body, 'lxml')
    my_need = html_soup.select('.main_con li')
    for i in my_need:
        all_info = i.find_all(name='span')
        category = re.sub('[\[\]]', '', all_info[0].a.string.strip()) # 类别
        title = all_info[1].a.string.strip() # 书名
        try:
            Contract_status = re.sub('[\[\]]', '', all_info[1].em.string.strip())  # 签约状态
        except:
            Contract_status = "未签约"
        Serial_state = all_info[3].string.strip()  # 连载状态
        sum_of_words = all_info[4].string.strip()  # 总字数
        author = all_info[5].a.string.strip()  # 作者
        latest_time = all_info[6].string.strip()  # 最后一次更新时间
        if(lock is True):
            print('{0},{1},{2},{3},{4},{5},{6}'.format(category, title, Contract_status, Serial_state,
                                                         sum_of_words, author, latest_time))
        if (out_control is True):
            yield "'{0}','{1}','{2}','{3}','{4}','{5}','{6}'".format(category, title, Contract_status, Serial_state,
                                                                     sum_of_words, author, latest_time)


# pages = int(input("输入一共获取的页数："))
pages = 801
db_link = pymssql.connect('MYPC\SQLEXPRESS','sa','sa','BookShop')
cur = db_link.cursor()
for i in range(273, pages):
    all_items = get_page_info(page_num=i, lock=False, out_control=True)
    for i in all_items:
        cur.execute("INSERT INTO Zongheng(category, title, Contract_status, Serial_state,sum_of_words, author, latest_time) VALUES({0})".format(i))
        db_link.commit()
db_link.close()