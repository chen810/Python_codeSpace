#p4_3.py
"""关于连续if的简化
{   if 条件：
      语句
    elif 条件：
      语句
    else：
      语句    }"""
score = int(input('请输入一个分数：'))
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 60:
    print('C')
elif 60 > score >= 0:
    print('D')
else:
    print('输入错误！')
input("按回车键退出……")
