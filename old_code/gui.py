import tkinter as tk

def cb():
	var.set('我是字符串var，我被调用了！！！')

root=tk.Tk()
root.title('这是一个测试界面')
frame0 = tk.Frame(root)
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)
frame6 = tk.Frame(root)
frame7 = tk.Frame(root)

#frame0
#photo=tk.PhotoImage(file=r'C:\Users\MISS\Desktop\aola\9.png')
#img=tk.Label(frame0,image=photo)
#img.pack(side=tk.RIGHT)

#frame1
var = tk.StringVar()
var.set('我是字符串var原来值！！！')
textL=tk.Label(frame1,textvariable=var,justify=tk.LEFT)
textL.pack(side=tk.TOP)
frame0.pack(padx=10,pady=10)
tb=tk.Button(frame1,text='我是按钮tb,点我改变数值！',command=cb)
tb.pack(side=tk.BOTTOM)

#frame2
group1=tk.LabelFrame(frame2,text='多选框',padx=10,pady=10)
group1.pack(padx=10,pady=10)
v=[]
vr=['V','one','two','three','four']
for i in vr:
    v.append(tk.IntVar())
    c=tk.Checkbutton(group1,text=i,variable=v[-1])
    c.pack(side=tk.LEFT,anchor=tk.N)


group2=tk.LabelFrame(frame2,text='单选框',padx=10,pady=10)
group2.pack(padx=10,pady=10)
q=tk.IntVar()
vr=['V','one','two','three','four']
tt=1
for i in vr:
    c=tk.Radiobutton(group2,text=i,variable=q,value=tt)
    c.pack(side=tk.LEFT,anchor=tk.N)
    tt+=1


#frame3
tk.Label(frame3,text='  账号：').grid(row=0)
tk.Label(frame3,text='  密码：').grid(row=1)
qq=dict(zip('abcdefgh',[str(i) for i in range(16)]))
def fanwei():
    
    t1=e1.get()
    t2=e2.get()
    if t2 == qq[t1] :
         print('ok')
         return True
    else:
         print('erorr')
         return False
e1=tk.Entry(frame3)
e2=tk.Entry(frame3,show=r'#',validate='focusout',validatecommand=fanwei)
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)
e1.delete (0,tk.END)
e2.delete (0,tk.END)
e1.insert (0,'这里是账号……')
e2.insert (0,'这里是密码……')
def quzhi():
    print('\n框一：%s'%e1.get())
    print('框二：%s'%e2.get())
cgg=tk.Button(frame3,text='我是按钮cgg,点取得数值！',width=30,command=quzhi)
cgg.grid(row=2,column=1,padx=10,pady=15)


#frame4
sb1=tk.Scrollbar(frame4)
sb1.pack(side=tk.RIGHT,fill=tk.Y)
tlist1=tk.Listbox(frame4,setgrid=True,yscrollcommand=sb1.set)
for i in range(200):
    tlist1.insert(tk.END,i)
tlist1.pack(fill=tk.BOTH)
sb1.config(command=tlist1.yview)

#frame5
tbm=tk.Button(frame5,text='delect',command=lambda x=tlist1:x.delete(tk.ACTIVE))
tbm.pack(padx=10,pady=5)

#frame6
ss1=tk.Scale(frame6,from_=20,to=100)
ss1.pack()
ss2=tk.Scale(frame6,from_=-100,to=100,orient=tk.HORIZONTAL)
ss2.pack()
def show():
        print(ss1.get(),ss2.get())
tk.Button(frame6,text='获得滑块位置',command=show).pack()

#frame7
sb2=tk.Scrollbar(frame7)
sb2.pack(side=tk.RIGHT,fill=tk.Y)
text1=tk.Text(frame7,width=50,height=15,yscrollcommand=sb2.set)
text1.pack(fill=tk.BOTH)
sb2.config(command=text1.yview)
text1.insert(tk.INSERT,'test message!!!\n' )
text1.insert(tk.END,'this is a word!')

#text1
#photo1=tk.PhotoImage(file=r'C:\Users\MISS\Desktop\aola\60.png')
#def show1():
        #text1.image_create(tk.END,image=photo1)
#bb1=tk.Button(text1,text='click here',command=show1)
#text1.window_create(tk.INSERT,window=bb1)



frame0.grid(row=0,column=0,padx=5,pady=6)
frame1.grid(row=0,column=1,padx=5,pady=6)
frame2.grid(row=0,column=2,padx=5,pady=6)
frame3.grid(row=1,column=0,padx=5,pady=6)
frame4.grid(row=1,column=1,padx=5,pady=6)
frame5.grid(row=2,column=1,padx=5,pady=6)
frame6.grid(row=1,column=2,padx=5,pady=6)
frame7.grid(row=0,column=3,padx=5,pady=6)
root.mainloop()
