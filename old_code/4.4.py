#4.4习题 生成一个包含50个随机整数的列表，然后删除其中的奇数（从后往前删）。
from random import randint
s=[randint(0,1000) for i in range(50)]
print('原列表（50个）：\n',s)
l=len(s)-1
for i in range(l,0,-1):
    if s[i]%2==1:
        del s[i]
l=len(s)
print('剩余个数：%3d'%l)
print(s)
input()
