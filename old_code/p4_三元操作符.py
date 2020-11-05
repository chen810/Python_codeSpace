#p4_三元操作符.py
"""
if x < y:
    small = x
else:
    small = y
可换为三元操作符
a = x if 条件 else y
"""
x = int(input('输入数字X：'))#获取x
y = int(input('输入数字Y：'))#获取y
small = x if x < y else y    #比较x与y
print("较小的是",small)      #输出小的一个数字
input("按回车键退出……")
