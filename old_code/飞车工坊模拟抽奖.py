from random import random,choice
from sys import exit
otherthings=('蔚蓝之空3天','蔚蓝之空7天','劳德曼3天','劳德曼7天','科技点400个',\
	     '科技点500个','科技点600个','金币400个','金币800个','星星闪烁飘焰3天',\
	     '星星闪烁胎印3天','黑白节拍套装7天','酷意街头套装7天')
hexinthings=('迅捷流星永久','迅捷流星7天')
dzjd=[{'成功': (0, 0.4), '失败': (0.4, 1)}, {'成功': (0, 0.2), '失败': (0.2, 1)},\
      {'成功': (0, 0.125), '失败': (0.125, 1)}, {'成功': (0, 0.07), '失败': (0.07, 1)},\
      {'成功': (0, 0.055), '失败': (0.055, 1)}, {'成功': (0, 0.045), '失败': (0.045, 1)},\
      {'成功': (0, 0.04), '失败': (0.04, 1)}, {'成功': (0, 0.035), '失败': (0.035, 1)}, \
      {'成功': (0, 0.02), '失败': (0.02, 1)}, {'成功': (0, 0.01), '失败': (0.01, 1)}]
def jiegezi(x,t):
	dushu1=random()   #第一个数字
	for k,v in x[t].items():     #t为格数，当解锁成功时格数+1
		if v[0]<dushu1<v[1]:
			return k

def acar(x,y):
	dushu2=random()   #第二个数字
	if 0<dushu2<0.035:
		return choice(x)
	else:
		return choice(y)

def cishu(n,t,l):
	jieguo=[]
	tongji=dict()
	for i in range(n):
		jieguo1=jiegezi(dzjd,t)
		if (jieguo1=='成功')&(t<10):
			t+=1
			
		jieguo2=acar(hexinthings,otherthings)
		if t==10:
			jieguo2='迅捷流星永久'
			t+=1
		jieguo.append((jieguo1,jieguo2))
		tongji[jieguo2]=tongji.get(jieguo2,0)+1
		if jieguo2=='迅捷流星永久':
			l=1
			break
	print('本次'+str(n)+'连抽结果为：')
	for j in jieguo:
		print('强化'+j[0]+'！获得了：'+j[1])
	print('\n解锁到了第'+str(t)+'格！',end=' ')
	print('共获得物品有：')
	for k in tongji.items():
		print(k[0]+'×'+str(k[1]))
	return t,l

time=0
lock=0
while True:
	
	while True:
		try:
		
			n=int(input('请输入抽奖次数：'))
			break
		except:
			print('输入错误',end=',')
			continue
		
	
	time,lock=cishu(n,time,lock)
	if lock==1:
		print('恭喜抽中迅捷流星永久！')
	print('请选择下一步操作！',end=' ')
	while True:
		try:
			how=str(input('重置(C)，继续(Y)，退出(N):\n'))
			if how not in ['c','C','y','Y','n','N']:
				raise TypeError
			break
		except :
			print('输入有误重新输入！')
			continue
	if how == 'c' or how == 'C':
		print('已重置',end='！')
		time=0
		lock=0
		continue
	elif how == 'y' or how == 'Y':
		print('继续抽奖',end='！')
		continue
	break


    

