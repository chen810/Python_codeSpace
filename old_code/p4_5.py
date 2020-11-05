#p4_5.py
for i in range(10):
    if i%2 != 0:
        print(i)
        continue         #若if成立则执行continue，再次执行循环语句，否则直接跳到下一行。
    i += 2
    print(i)
input("按回车键退出……")
