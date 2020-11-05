import requests
from urllib.parse import urlencode
from urllib.request import unquote
import re
import os

my_download_num = 0
base_url = 'https://image.baidu.com/search/acjson?'
base_url1 = 'https://pic.sogou.com/pics?'
dz_local = 'D:\\'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400',
}


def get_all_info(pages, name):
    name_pa = unquote(name)
    list_img_info = []
    params = {
        'query': name_pa,
        'mode': '1',
        'start': pages,
        'reqType': 'ajax',
        'reqFrom': 'result',
        'tn': '0'
    }
    url = base_url1+urlencode(params)
    html = requests.get(url, headers=headers)
    txt_img_html = html.json().get('items')
    # print(bool(txt_img_html[0]))
    if not txt_img_html[0]:
        return 'Over'
    for i in range(48):
        output_info = {}
        p = re.compile('[ *:><\'\"/|,?]')
        try:
            output_info['title'] = re.sub(p, '', txt_img_html[i]['markedTitle'])
            output_info['img_url'] = txt_img_html[i]['pic_url']
            if output_info['img_url'][-4: -3] == '.':
                output_info['suffix'] = output_info['img_url'][-3:]
            elif output_info['img_url'][-5: -4] == '.':
                output_info['suffix'] = output_info['img_url'][-4:]
            else:
                continue
            list_img_info.append(output_info)
        except KeyError:
            return 'Over'

    return list_img_info


def download_img(dict_img_info, name, dz):
    print(dict_img_info['img_url'])
    p = re.compile('https')
    try:
        img_html = requests.get(dict_img_info['img_url'])
    except:
        print('网址由https改为http')
        my_new_web = re.sub(p, 'http', dict_img_info['img_url'])
        img_html = requests.get(my_new_web)
    img_dz = dz+name+'\\'+dict_img_info['title']+'.'+dict_img_info['suffix']
    with open(img_dz, 'wb') as fp:
        fp.write(img_html.content)


def make_dir(name, dz=dz_local):
    p_file = re.compile('[*:><\'\"/|,?]')
    print('输入你要存储的文件夹路径，默认路径为D:\\(若默认则直接回车，不存在则会创建一个)')
    my_dz = input('PATH:')
    re.sub('：', ':', my_dz)
    if my_dz == '':
        if not os.path.exists(dz + name):
            os.mkdir(dz + name)
        print('您已选择默认路径！！！')
        return dz
    elif not re.search(':', my_dz[1:2]):
        my_dz = dz+my_dz
        if not os.path.exists(my_dz):
            os.mkdir(my_dz)
            print('未加盘符故自动在D盘下创建此文件夹！！！')
            if not os.path.exists(my_dz+'\\'+name):
                os.mkdir(my_dz+'\\'+name)
            return my_dz+'\\'
        else:
            print('已存在，故不创建文件夹。')
            if not os.path.exists(my_dz+'\\'+name):
                os.mkdir(my_dz+'\\'+name)
            return my_dz+'\\'
    elif re.search(p_file, my_dz[2:]):
        print('PATH格式错误！！！不可含有特殊字符！！！')
        make_dir(name)
    else:
        if not os.path.exists(my_dz):
            os.mkdir(my_dz)
            print('不存在此文件夹，已自动创建一个！！！')
            if not os.path.exists(my_dz+'\\'+name):
                os.mkdir(my_dz+'\\'+name)
            return my_dz+'\\'
        else:
            print('已存在，故不创建文件夹。')
            if not os.path.exists(my_dz+'\\'+name):
                os.mkdir(my_dz+'\\'+name)
            return my_dz + '\\'


def get_name():
    my_name = input('输入图片所属类型:')
    return my_name


def get_max_num():
    try:
        my_max_num = input('请输入大概获取多少张图片(推荐设定48的倍数,默认为10000000):')
        p = re.compile('[0-9]')
        num_list_max = re.findall(p, my_max_num)
        # print(bool(num_list_max ))
        if not num_list_max:
            return 10000000
        else:
            return int(''.join(num_list_max))
        # my_num = int(input('请输入大概获取多少张图片(推荐设定30的倍数,默认为10000000):'))
        # return my_num
    except TypeError:
        get_max_num()


def main_do(count_all=my_download_num, max_download_num=10000000):
    print('======图片来源于搜狗图片======')
    search = get_name()
    num_get_by_fun = get_max_num()
    if num_get_by_fun != '':
        max_download_num = num_get_by_fun
    new_dz = make_dir(name=search)
    for count_num in range(0, max_download_num, 48):
        print(count_num)
        transit = get_all_info(count_num, name=search)
        if transit == 'Over':
            break
        else:
            for k in transit:
                try:
                    download_img(k, name=search, dz=new_dz)
                    count_all += 1
                except:
                    continue
    print('所有图片已下载完成！\n实际下载数量为:%-10d' % count_all)


if __name__ == '__main__':
    main_do()
    '''
    try:
        main_do()
    except:
        print('发生错误请重试！')
'''


