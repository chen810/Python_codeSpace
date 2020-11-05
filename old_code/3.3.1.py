s=[20,44,48,55,62,66,74,88,93,99]
t=int(input('input the nummber:'))
def Findint(t):
    '''find the num in s'''
    left=0
    right=len(s)-1
    while left <= right:
        mid=(left+right)//2
        if t==s[mid]:
            print('left%-3d=%3d,right%-3d=%3d'%(left,s[left],right,s[right]))
            print('mid is %3d,it index is %3d'%(s[mid],mid))
            return 0
        elif t>s[mid]:
            print('left%-3d=%3d,right%-3d=%3d'%(left,s[left],right,s[right]))
            left=mid+1
        else:
            print('left%-3d=%3d,right%-3d=%3d'%(left,s[left],right,s[right]))
            right=mid-1
    if left >right:
        print('not in s')


if __name__ =='__main__':
    x=Findint(t)
    input()
