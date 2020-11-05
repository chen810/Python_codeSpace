import time
problemsize=10000000
print ('%12s%26s'%('problemsize','seconds'))
for count in range(5):
    start=time.time ()
    #the start of the algorithm
    work=1
    for x in range(problemsize):
        work+=1
        work-=1
    #the end of the algorithm
    elapsed=time.time()-start
    print ('%12s%26.3f'%(problemsize,elapsed))
    problemsize*=2
