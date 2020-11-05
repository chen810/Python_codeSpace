import csv
import re

dz1 = r'C:\Users\MISS\Desktop\weibo1.txt'
dz2 = r'C:\Users\MISS\Desktop\1.csv'

with open(dz1, 'r', encoding='utf-8') as fp:
    text = fp.read()

p = re.compile('博主：(.+?)\n微博传送门：(.+?)\n他的最新微博传送门：(.+?)\n时间：(.+?)\n=', re.S)
pp = re.findall(p, text)

with open(dz2, 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['博主', '空间传送门', '最新发布的博文', '发布时间'])
    for i in pp:
        writer.writerow(list(i))


