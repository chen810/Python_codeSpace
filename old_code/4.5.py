'''生成一个包含20个随机整数的列表，然
后对其下标为偶数的部分进行排序，奇数
下标不变（使用切片）'''
from random import sample
a=sample(range(1000),20)
print('原列表：\n',a)
a[::2]=sorted(a[::2])
print('处理后列表：\n',a)
input()
