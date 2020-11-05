# 这是一个用来执行文件储存的函数库





def my_mkdir(name, dz='F:\\', ignore=False):
    path_fix = re.compile('[*:><\'\"/|?]')
    name = re.sub(path_fix, '', name)
    if ignore is False:
        get_path = input('输入要存储的路径:')
    else:
        print('自动填充为默认')
        get_path = ''
    get_path = re.sub('：', ':', get_path)
    try:
        if get_path == '':
            # 判断是否使用默认存储路径，并在其路径下创建一个空文件夹。
            temporary_dz1 = dz+name
            if not os.path.exists(temporary_dz1):
                os.mkdir(temporary_dz1)
            print('路径已设置为:{0}'.format(temporary_dz1))
            return temporary_dz1
        elif not re.search(':', get_path[0:2]):
            temporary_dz2 = dz+get_path
            if not os.path.exists(temporary_dz2):
                os.mkdir(temporary_dz2)
                print('未加盘符故自动在F盘下创建此文件夹！！！')
                temporary_dz2_file = temporary_dz2+'\\'+name
                if not os.path.exists(temporary_dz2_file):
                    os.mkdir(temporary_dz2_file)
                print('路径已设置为:{0}'.format(temporary_dz2_file))
                return temporary_dz2_file
            else:
                print('已存在，故不创建文件夹。')
                temporary_dz3 = get_path+'\\'+name
                if not os.path.exists(temporary_dz3):
                    os.mkdir(temporary_dz3)
                print('路径已设置为:{0}'.format(temporary_dz3))
                return temporary_dz3
        elif re.search(path_fix, get_path[2:]):
            print('PATH格式错误！！！不可含有特殊字符！！！')
            my_mkdir(name, dz)
        else:
            if not os.path.exists(get_path):
                os.mkdir(get_path)
                print('不存在此文件夹，已自动创建一个！！！')
                temporary_dz4 = get_path + '\\' + name
                if not os.path.exists(temporary_dz4):
                    os.mkdir(temporary_dz4)
                print('路径已设置为:{0}'.format(temporary_dz4))
                return temporary_dz4
            else:
                print('已存在，故不创建文件夹。')
                temporary_dz5 = get_path+'\\'+name
                if not os.path.exists(temporary_dz5):
                    os.mkdir(temporary_dz5)
                return temporary_dz5
    except:
        print('发生了个错误，请查看路径是否符合规范！')
        my_mkdir(name, dz)


'''
my_mkdir(name, dz='D:\\')
这是一个创建文件夹的操作，首先选择创建位置，然后判断是否存在，后建立文件夹。
其中包括检测文件名是否规范。
name即为要创建的文件夹
'''


def http_swap(old_url, out_info=True):
    if old_url[0:5] == 'http:':
        new_url = 'https:'+old_url[5:]  # 判断是否为http类型的url
    elif old_url[0:6] == 'https:':
        new_url = 'http:'+old_url[6:]  # 判断是否为https类型的url
    else:
        # 让用户选择是否重新输入或者跳过这个url，返回一个空url。
        print('No HTTP or HTTPS was detected!!!')
        choice_url = input('若手动更改则输入新url，否则回车跳过。')
        if choice_url == '':
            return ''
        else:
            http_swap(choice_url)
    if out_info is True:
        print(new_url)
    elif out_info is False:
        pass
    else:
        pass
    return new_url


'''
# http_swap(old_url, out_info=True)
# old_url为需要转换的url，out_info为是否将结果打印在屏幕上。
# 参数需要以http:或者https:开头，此函数用于在http和https之间互相转换,返回值为一个链接。
# 若:     http_swap('http:web link') ----->https:web link
#         http_swap('https:web link') ----->http:web link
# '''