# p3_1.py
import random
secret = random.randint(1,10)
temp = input("不妨猜一下小甲鱼心里现在想的是哪个数字：")
guess = int(temp)
while guess != secret:
    temp=input("哎呀，猜错啦，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("哎呀，你是小甲鱼肚子里的蛔虫吗？！")
        print("哼，猜中也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了小了~~~")
print("游戏结束，不玩啦^-^")
input("按回车键退出……")
