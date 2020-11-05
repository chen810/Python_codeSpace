#py6_5.py
def recursion(n):
    result = n
    for i in range(1,n):
        result *=i
    return result
number = int(input('请输入一个整数：'))
result= recursion(number)
print("%d的阶乘是：%d"%(number,result))
input("回车退出")
