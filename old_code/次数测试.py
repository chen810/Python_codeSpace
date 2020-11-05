import time
problemsize=[1000000,2000000,4000000,10000000,100000000]
print ('%12s%26s'%('problemsize','seconds'))
for i in problemsize:
    num=0
    t=i
    #start of the programme
    while i >0:
        i = i // 2
        num+=1
    #stop of the programme
    print ('%12s%26d'%(t,num))

