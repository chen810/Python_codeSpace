# p2_1.py
"""---第一个小游戏---"""
temp = input("不妨猜一下小甲鱼心里现在想的是哪个数字：")
guess = int(temp)
if guess == 8:
    print("你是小甲鱼心里的蛔虫吗？！")
    print("哼，猜中也没有奖励！")
else:
    print("猜错啦，小甲鱼现在心里想的是8！")
print("游戏结束，不玩啦^-^")
input("按回车键退出……")
