import os
x=[filename for filename in os.listdir ('.') if filename.endswith(('.mp4','.mp3'))]
k=len(x)
for i in range(k):
    print(x[i],end='\n')
y=input()
