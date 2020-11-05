import tkinter as tk
class tt:
    def __init__(self,root):
        global photo
        frame = tk.Frame(root)
        frame.pack(side=tk.LEFT,padx=10,pady=10)
        textlabel =tk.Label(frame,text='这是一条输出消息！')
        textlabel.pack(side=tk.TOP,padx=3,pady=3)
        self.an1=tk.Button(frame,text='anniu1',fg='red',bg='white',command=self.hi1)
        self.an1.pack(side=tk.LEFT,padx=5,pady=5)
        self.an2=tk.Button(frame,text='anniu2',fg='red',bg='white',command=self.hi2)
        self.an2.pack(side=tk.LEFT,padx=5,pady=5)
        #photo= tk.PhotoImage(file=r'C:\Users\MISS\Desktop\3.gif')
        #thel=tk.Label(frame,text='这是文字区！',justify=tk.LEFT,image=photo,compound=tk.CENTER,font=('腾祥伯当行楷简',20),fg='red')
        #thel.pack()

    def hi1(self):
        print('我是按钮1，我被点到了……')
    def hi2(self):
        print('我是按钮2，我被点到了……')


root=tk.Tk()
test=tt(root)
root.mainloop()
