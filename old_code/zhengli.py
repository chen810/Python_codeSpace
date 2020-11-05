import re
import os
from shutil import copyfile,move,copytree

dz_ori = r'C:\Users\WOOO\Desktop\123'
dz_aim = r'C:\Users\WOOO\Desktop\456'


def change_local(origin_dz, aim_dz):
    count_n = 1
    list_item = os.listdir(origin_dz)
    for pic in list_item:
        if pic[-4:-3] == '.':
            print("name:{0}".format(pic))
            try:
                name = pic[-3:-2] + str(count_n) + pic[-4:]
                move(origin_dz + '\\' + pic, aim_dz + '\\' + name)
                count_n += 1
                print("ok")
            except:
                print("error")
        elif pic[-5:-4] == '.':
            print("name:{0}".format(pic))
            try:
                name = pic[-4:-2] + str(count_n) + pic[-5:]
                move(origin_dz + '\\' + pic, aim_dz + '\\' + name)
                count_n += 1
                print("ok")
            except:
                print("error")
        else:
            print("something is wrong!")


def A2B(org, bak):
    a = os.listdir(org)
    if len(a) != 0 :
        for i in a:
            if os.path.isdir(org+'\\'+i):
                if i in os.listdir(bak):
                    print("检测到文件夹{0}，已备份向内查看".format(org+'\\'+i))
                    A2B(org+'\\'+i,bak+'\\'+i)
                else:
                    print("检测到文件夹{0}，未备份整体复制".format(org+'\\'+i))
                    copytree(org+'\\'+i,bak+'\\'+i)
            else:
                if i not in os.listdir(bak):
                    print("检测到文件{0}，未备份进行复制".format(org+'\\'+i))
                    copyfile(org+'\\'+i,bak+'\\'+i)
                else:
                    print("检测到文件{0}，已备份".format(org+'\\'+i))


def clear(path):
    a = os.listdir(path)
    if len(a)==0:
        print("文件夹{0}为空".format(path))
        os.rmdir(path)
        print("删除成功")
    else:
        for items in a:
            item = os.listdir(path + '\\' + items)
            if len(item) == 0:
                print("文件夹{0}为空".format(path + '\\' + items))
                try:
                    os.rmdir(path + '\\' + items)
                    print("删除成功")
                except:
                    print("删除失败")



def mv_pic(origin_dz, aim_dz, pic_c=1):
    item_in = os.listdir(origin_dz)
    for info_item in item_in:
        if os.path.isdir(origin_dz+"\\"+info_item):
            mv_pic(origin_dz+"\\"+info_item, aim_dz)
        else:
            if (info_item[-3:] in ["jpg","gif","png"]) or (info_item[-4:] in ["jpeg"]):
                try:
                    print("PIC was found-->name:{0}".format(info_item))
                    name = str(pic_c) + info_item
                    move(origin_dz + '\\' + info_item, aim_dz + '\\' + name)
                    pic_c += 1
                    print("↑↑↑↑↑↑↑↑↑↑↑↑↑-->OK")
                except:
                    print("↑↑↑↑↑↑↑↑↑↑↑↑↑-->ERROR")
'''移动图片'''


try:
    mv_pic(dz_ori,dz_aim)
except:
    print("异常终止")


