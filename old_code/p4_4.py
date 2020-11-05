#p4_4.py
bingo = '小甲鱼是帅哥'
answer = input('请输入小甲鱼最想听的一句话:')
while True:           #循环体
    if answer == bingo:
        break              #当条件成立时，跳出循环。
    answer = input('抱歉，错了，请重新输入（答案正确才能退出游戏）:')
print('哎呦，帅哦~')
print('您真是小甲鱼肚子里的蛔虫啊^-^')
input("按回车键退出……")
