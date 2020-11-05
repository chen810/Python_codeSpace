print('这是一个因式分解的程序！')
while True:
    try:
        x=int(input('输入一个数：'))
        if 0<x:
            break
        else:
            print('输入有误请重新输入!')
            continue
    except:
        print('输入有误请重新输入!')
k=len(str(x))
kf=10**k
s=[2,3]
for i in range(3,kf):
	k=0
	if (i%6==1)|(i%6==5):
		for j in range(2,int(i**0.5)+1):
			if i%j==0:
				k=-1
				break
		if k==0:
			s.append(i)
l=len(s)
print(x,'=1',end='')
while x!=1:
    for i in range(l):
        if x%s[i]==0:
            print('×',s[i],end='')
            x/=s[i]
            break
input('\n')
